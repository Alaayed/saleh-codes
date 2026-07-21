# Darb — Company Section Backend Outline (DARB-1197)

> Wiring plan for the client-portal **Company** section. Frontend lives on
> `origin/saleh/darb-1197-company-section` (UI-only, runs on stub data in
> `app/client/(active)/company/_components/company-data.ts`).
> Written 2026-07-21.

## UI contract to satisfy

- **`CompanyMember`**: `{ id, firstName, lastName, email, status: 'ACTIVE'|'PENDING', role: 'ADMIN'|'EMPLOYEE'|'AUDITOR'|'ACCOUNTANT'|'VIEWER', team, funds: string[], phone, joinedAt, vehicleAccess: 'ALL_VEHICLES'|'ASSIGNED_ONLY' }`
- **`CompanyTeam`**: `{ id, name, memberCount, spendPercent, spendThisMonth, managerName, extraManagers, memberInitials, assignedVehicles: number|'ALL'|null, funds: string[] }`
- **Mutations the UI fires**: invite member (`role, isManager, assignToVehicles, firstName, lastName, phone, employeeId?`), resend invitation (single + bulk), delete member (single + bulk). "Edit member", "Edit team", and "Create Team" are still stub toasts.
- Details-sheet tabs `vehicles / alerts / violations / transactions` render `emptyTab` placeholders — no data contract yet.

## Key backend facts

- "Teams" = existing `Group` model (`prisma/schema/group.prisma`) — full CRUD already in `lib/actions/client/groups.ts`.
- Members are a **union of two tables**: `Employee` (drivers) and `User` (portal users: CLIENT / ACCOUNT_MANAGER / MANAGER / VIEWER).
- Reusable pieces: `createEmployee` (`lib/actions/client/client.ts:180`), `deleteEmployee` (`client.ts:825`), `inviteViewer` (`client.ts:1098`), `deleteManagerCompletely` (`groups.ts:567`), `sendEmployeeWelcomeSMS` (`lib/actions/client/notifications.ts`).
- `Transaction.groupIdAtAuthTime` exists for team spend aggregation.
- **No backend representation at all** for: `PENDING` member state, `ACCOUNTANT`/`AUDITOR` roles, and "Funds".

---

## 0. Schema changes (decide first)

1. **Pending status** — nothing models "invited but hasn't joined." Drivers get a Clerk user immediately at creation, so `Employee.userId == null` won't work. Recommended: add `firstSignInAt DateTime?` to `User`, set via the Clerk webhook/login path; `status = firstSignInAt ? ACTIVE : PENDING`. (Alternative: read Clerk `lastSignInAt` at list time — simpler but slow/rate-limited.)
2. **Roles** — add `ACCOUNTANT` (invitable in the UI) to `UserRole`; `AUDITOR` is display-only for now, so map it or drop it. Mapping layer both ways:
   - `EMPLOYEE` ↔ `Employee` row (role DRIVER)
   - `ADMIN` ↔ `User.role CLIENT` / `ACCOUNT_MANAGER`
   - `VIEWER` ↔ `User.role VIEWER`
   - `ACCOUNTANT` ↔ new `UserRole.ACCOUNTANT` (needs a `can()` permission entry in `lib/config/permissions` too)
   - `isManager` toggle ↔ `UserRole.MANAGER` / `Employee.role MANAGER` + group ownership
3. **Funds** — no `Fund` model exists anywhere. Either hide the columns for v1, or map "funds" to names of budgeted groups the member belongs to (`Group.name` where `budget != null`). **Flag with product before building.**

## 1. Read services — new file `lib/services/company.ts`

Reads live in `lib/services/`; the page/SWR calls them via thin actions.

```typescript
// Unified member list: merges Employees (drivers) + Users (portal roles),
// scoped to clientId, ACTIVE-status rows only, MANAGER-scoped by groupId
// like getEmployees does (lib/services/client.ts:937).
getCompanyMembers(user: UserMetadataDetails): Promise<CompanyMemberDTO[]>

// Pending tab: same list filtered to status === 'PENDING' (or derive
// client-side — the UI already derives pendingInvites from members).

// Teams tab: Group + budget + _count (already in getGroups) PLUS:
//  - spendThisMonth: sum(Transaction.amount) where groupIdAtAuthTime = group.id
//    and createdAt in current month (one groupBy query for all groups)
//  - spendPercent: group spend / client total spend this month
//  - managerName/extraManagers: from Group.owner + any co-managers
//  - memberInitials: first 2 employees' initials + memberCount
getCompanyTeams(user: UserMetadataDetails): Promise<CompanyTeamDTO[]>
```

Notes:

- `CompanyMemberDTO` needs a **composite id** (`employee:123` / `user:clerk_abc`) since it merges two tables — the UI's `id: number` will need loosening, and delete/resend route on it.
- `joinedAt` → `Employee.createdAt` / `User.createdAt`; `team` → `Employee.group.name` or owned group for managers; `vehicleAccess` → `Employee.vehicleAccessType` (users: `ALL_VEHICLES`).
- Convert Prisma `Decimal` to `number` before returning (see `getGroups` at `groups.ts:76`).

## 2. Server actions — new `lib/actions/client/company.ts` + `company.validation.ts`

Writes on `authClientWriteActionClient`, reads on `authClientActionClient`, `revalidatePath('/client/company')` after mutations.

```typescript
// Reads (thin wrappers over the services above)
getCompanyMembersAction   // actionName: 'getCompanyMembers'
getCompanyTeamsAction     // actionName: 'getCompanyTeams'

// Invite — branches on role:
//  EMPLOYEE  → reuse createEmployee path: phone-dedupe (normalizePhoneNumber),
//              employee row, createUserForEmployeeDriver, sendEmployeeWelcomeSMS.
//              employeeId form field → Employee.externalReference.
//              assignToVehicles → vehicleAccessType ASSIGNED_ONLY (dialog has
//              no vehicle picker yet, so it only sets the mode).
//  ADMIN/VIEWER/ACCOUNTANT → user-invite path like inviteViewer
//              (createUserForViewer + welcome email/SMS).
//  isManager → MANAGER role variant (see AddAccountManagerForm flow).
inviteCompanyMember(input: InviteMemberSchema)

// Resend — takes memberIds[], re-sends sendEmployeeWelcomeSMS (drivers) or
// welcome email (portal users). Per-member 1-minute rate limit, mirroring
// resendCardActivationCall (lib/actions/client/card.ts:1009).
resendCompanyInvitation({ memberIds: string[] })

// Delete — takes memberIds[], routes each: employee → deleteEmployee logic
// (guards: active cards/vehicles), manager → deleteManagerCompletely,
// viewer → existing viewer deletion. Soft-delete (ARCHIVED/INACTIVE),
// never hard delete.
deleteCompanyMembers({ memberIds: string[] })
```

Validation: `inviteMemberSchema` = zod object matching `InviteMemberValues`, with `saudiPhoneSchema` for phone (dialog already uses it client-side — share the schema).

## 3. Cross-cutting

- **Entity audit**: add a thin wrapper (`lib/services/member-audit.ts` following `policy-audit.ts`) and log invite/delete/role changes with `changeContext: 'COMPANY_MEMBER_*'`. Users already get `UserAuditLog`; employees currently get nothing.
- **Permissions**: gate page + write actions with `can(role, 'employees', ...)` / `PermissionGate` like the existing team page; decide what `ACCOUNTANT` can see.
- **Frontend swap**: `CompanyView` replaces `useState(MOCK_MEMBERS)` with SWR on the read actions; `handleInvite/handleResend/handleDelete` call the actions and `mutate()`. `page.tsx` can prefetch server-side like `team/page.tsx`.

## 4. Explicitly deferred (stubs in the UI, no contract yet)

- Edit member / edit team / Create Team buttons (Create Team can link to the existing groups flow).
- Details-sheet tabs: vehicles, alerts, violations, transactions — each eventually needs a per-member read (`getMemberVehicles`, `getMemberAlerts(employeeId)`, …); existing alert/violation/transaction services are already employee-scoped, so these are thin filters.

## Suggested build order

1. Schema decisions (§0)
2. `getCompanyMembers` + wire Members/Pending tabs
3. Invite
4. Resend / delete
5. `getCompanyTeams`

Riskiest design call: **composite member ID + pending-status definition** — settle before writing any queries; every action's input shape depends on it.
