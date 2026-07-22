# Darb — Company Section Backend Outline (DARB-1197)

> Wiring plan for the client-portal **Company** section. Frontend lives on
> `origin/saleh/darb-1197-company-section` (UI-only, runs on stub data in
> `app/client/(active)/company/_components/company-data.ts`).
> Written 2026-07-21. **Revised 2026-07-22 for the V3 (JUL 2026) redesign
> commit `46c31f92`** — invite sheet with email/phone modes, real Create Team
> flow, team details sheet, slimmed teams table.

## UI contract to satisfy (V3)

- **`CompanyMember`**: `{ id, firstName, lastName, email, status: 'ACTIVE'|'PENDING', role: 'ADMIN'|'EMPLOYEE'|'AUDITOR'|'ACCOUNTANT'|'VIEWER'|'MANAGER', team, funds: string[], phone, joinedAt, vehicleAccess: 'ALL_VEHICLES'|'ASSIGNED_ONLY', vehicles?: string[] }`
  - `vehicles` entries are display labels like `"1234 - ABC (Hino Dutro)"` (plate — name (make/model)), shown in the member details sheet.
- **`CompanyTeam`**: `{ id, name, memberCount, spendPercent, spendThisMonth, managerName, extraManagers, memberInitials, assignedVehicles: number|'ALL'|null, funds: string[] }`
  - V3 table renders only: name+count, **spendThisMonth**, manager (+N), member avatars, assigned vehicles. `spendPercent` and group-funds columns were **removed from the table** (fields still exist in the type; `spendThisMonth` also shows in the team details sheet).
- **Invite** (`InviteMemberSheet`, replaces the old dialog): `{ role: 'AUDITOR'|'EMPLOYEE'|'ADMIN'|'MANAGER', firstName, lastName, email?, phone?, assignToVehicles }` with a `mode: 'EMAIL'|'PHONE'` tab — exactly one of email/phone is sent.
  - `employeeId` field and `isManager` toggle are **gone**; MANAGER is a first-class invitable role now.
  - ACCOUNTANT renders as a "Coming Soon" card (not invitable); VIEWER no longer invitable; **AUDITOR is now invitable**.
  - Vehicles toggle only shows for EMPLOYEE role.
- **Create Team** (`CreateTeamSheet`, now a real flow): `{ name, leaderIds: number[], memberIds: number[] }` — note **multiple leaders**.
- **Team details** (`TeamDetailsSheet`): leaders, members, spendThisMonth per team.
- **Other mutations**: resend invitation (single + bulk), delete member (single + bulk). "Edit Profile" (member) and "Edit team" still stubs.
- Member details tabs `alerts / violations / transactions` still `emptyTab` placeholders; the vehicles tab now renders `member.vehicles`.

## Key backend facts

- "Teams" = existing `Group` model (`prisma/schema/group.prisma`) — full CRUD already in `lib/actions/client/groups.ts`.
- Members are a **union of two tables**: `Employee` (drivers) and `User` (portal users: CLIENT / ACCOUNT_MANAGER / MANAGER / VIEWER).
- Reusable pieces: `createEmployee` (`lib/actions/client/client.ts:180`), `deleteEmployee` (`client.ts:825`), `inviteViewer` (`client.ts:1098`), `deleteManagerCompletely` (`groups.ts:567`), `createGroup` / `assignMembersToGroup` (`groups.ts`), `sendEmployeeWelcomeSMS` (`lib/actions/client/notifications.ts`).
- `Transaction.groupIdAtAuthTime` exists for team spend aggregation.
- **No backend representation** for: `PENDING` member state, `AUDITOR` role, "Funds", multi-leader teams.

---

## 0. Schema changes (decide first)

1. **Pending status** — nothing models "invited but hasn't joined." Drivers get a Clerk user immediately at creation, so `Employee.userId == null` won't work. Recommended: add `firstSignInAt DateTime?` to `User`, set via the Clerk webhook/login path; `status = firstSignInAt ? ACTIVE : PENDING`. (Alternative: read Clerk `lastSignInAt` at list time — simpler but slow/rate-limited.)
2. **Roles** — V3 mapping both ways:
   - `EMPLOYEE` ↔ `Employee` row (role DRIVER), invited **by phone**
   - `ADMIN` ↔ `User.role CLIENT` / `ACCOUNT_MANAGER`, invited by email
   - `MANAGER` ↔ `UserRole.MANAGER` (+ group ownership), invited by email
   - `AUDITOR` ↔ **new** — add `UserRole.AUDITOR` (read-only-ish; decide `can()` permissions in `lib/config/permissions`) — or map onto VIEWER for v1 if product agrees
   - `VIEWER` ↔ `User.role VIEWER` — display-only in V3 (existing viewers still appear in the list)
   - `ACCOUNTANT` ↔ deferred ("Coming Soon" card) — nothing to build yet
   - Backend should validate mode/role combos (e.g. EMPLOYEE requires phone; portal roles require email).
3. **Multi-leader teams** — `CreateTeamValues.leaderIds` is an array but `Group.ownerId` is a single owner. Options: keep `ownerId` as primary + add a `GroupLeader` join table, or restrict UI to 1 leader for v1. **Decide with product before building createTeam.**
4. **Funds** — no `Fund` model exists. Off the teams table in V3, but the members table still shows an "Associated Funds" column. Either hide for v1 or map to names of budgeted groups (`Group.name` where `budget != null`). **Flag with product.**

## 1. Read services — new file `lib/services/company.ts`

Reads live in `lib/services/`; the page/SWR calls them via thin actions.

```typescript
// Unified member list: merges Employees (drivers) + Users (portal roles),
// scoped to clientId, ACTIVE-status rows only, MANAGER-scoped by groupId
// like getEmployees does (lib/services/client.ts:937).
// Include assigned vehicles formatted as "plate - name (make model)"
// for the details sheet's vehicles tab.
getCompanyMembers(user: UserMetadataDetails): Promise<CompanyMemberDTO[]>

// Pending tab: same list filtered to status === 'PENDING' (UI already
// derives pendingInvites from the members array).

// Teams tab (V3): Group + _count (already in getGroups) PLUS:
//  - spendThisMonth: sum(Transaction.amount) where groupIdAtAuthTime = group.id
//    and createdAt in current month (one groupBy query for all groups)
//  - managerName/extraManagers: Group.owner (+ leaders join table if added)
//  - memberInitials: first 2 employees' initials + memberCount
//  - spendPercent no longer rendered — skip the client-total aggregation
getCompanyTeams(user: UserMetadataDetails): Promise<CompanyTeamDTO[]>
```

Notes:

- `CompanyMemberDTO` needs a **composite id** (`employee:123` / `user:clerk_abc`) since it merges two tables — the UI's `id: number` will need loosening, and delete/resend/createTeam member-selection route on it.
- `joinedAt` → `Employee.createdAt` / `User.createdAt`; `team` → `Employee.group.name` or owned group for managers; `vehicleAccess` → `Employee.vehicleAccessType` (users: `ALL_VEHICLES`).
- Convert Prisma `Decimal` to `number` before returning (see `getGroups` at `groups.ts:76`).

## 2. Server actions — new `lib/actions/client/company.ts` + `company.validation.ts`

Writes on `authClientWriteActionClient`, reads on `authClientActionClient`, `revalidatePath('/client/company')` after mutations.

```typescript
// Reads (thin wrappers over the services above)
getCompanyMembersAction   // actionName: 'getCompanyMembers'
getCompanyTeamsAction     // actionName: 'getCompanyTeams'

// Invite — validate mode/role combo, then branch:
//  EMPLOYEE (phone mode) → reuse createEmployee path: phone-dedupe
//              (normalizePhoneNumber), employee row, createUserForEmployeeDriver,
//              sendEmployeeWelcomeSMS. assignToVehicles → vehicleAccessType
//              ASSIGNED_ONLY (sheet has no vehicle picker; just sets the mode).
//  ADMIN / MANAGER / AUDITOR (email mode) → user-invite path like inviteViewer
//              (createUserForViewer-style + Clerk email invitation + welcome email).
//              MANAGER additionally follows the AddAccountManagerForm flow
//              (group ownership wiring).
inviteCompanyMember(input: InviteMemberSchema)

// Create team — wraps existing createGroup (groups.ts:301) then
// assignMembersToGroup for memberIds; leaders per the §0.3 decision
// (ownerId = leaderIds[0] + GroupLeader rows, or single-leader v1).
createCompanyTeam({ name, leaderIds, memberIds })

// Resend — takes memberIds[], re-sends sendEmployeeWelcomeSMS (drivers) or
// welcome/invite email (portal users). Per-member 1-minute rate limit,
// mirroring resendCardActivationCall (lib/actions/client/card.ts:1009).
resendCompanyInvitation({ memberIds: string[] })

// Delete — takes memberIds[], routes each: employee → deleteEmployee logic
// (guards: active cards/vehicles), manager → deleteManagerCompletely,
// viewer → existing viewer deletion. Soft-delete (ARCHIVED/INACTIVE),
// never hard delete.
deleteCompanyMembers({ memberIds: string[] })
```

Validation: `inviteMemberSchema` mirrors the sheet's zod schema — `mode: z.enum(['EMAIL','PHONE'])`, exactly-one-of email/phone (superRefine), `saudiPhoneSchema` for phone, role enum `['AUDITOR','EMPLOYEE','ADMIN','MANAGER']`. Share the schema with the client component.

## 3. Cross-cutting

- **Entity audit**: add a thin wrapper (`lib/services/member-audit.ts` following `policy-audit.ts`) and log invite/delete/role/team changes with `changeContext: 'COMPANY_MEMBER_*'` / `'COMPANY_TEAM_*'`. Users already get `UserAuditLog`; employees currently get nothing.
- **Permissions**: gate page + write actions with `can(role, 'employees', ...)` / `PermissionGate` like the existing team page; define what `AUDITOR` can see before wiring the role.
- **Frontend swap**: `CompanyView` replaces `useState(MOCK_MEMBERS)` with SWR on the read actions; invite/resend/delete/createTeam handlers call the actions and `mutate()`. `page.tsx` can prefetch server-side like `team/page.tsx`.

## 4. Explicitly deferred (stubs in the UI, no contract yet)

- "Edit Profile" (member) and "Edit team" buttons.
- ACCOUNTANT role ("Coming Soon" card).
- Details-sheet tabs: alerts, violations, transactions — each eventually needs a per-member read; existing alert/violation/transaction services are already employee-scoped, so these are thin filters. (Vehicles tab is **no longer deferred** — it renders `member.vehicles` from `getCompanyMembers`.)

## Suggested build order

1. Schema decisions (§0) — pending status, AUDITOR role, multi-leader teams, funds
2. `getCompanyMembers` (incl. vehicles labels) + wire Members/Pending tabs
3. Invite (email + phone paths)
4. Resend / delete
5. `getCompanyTeams` + createCompanyTeam

Riskiest design calls: **composite member ID + pending-status definition** (every action's input shape depends on them) and **multi-leader teams vs. `Group.ownerId`** (blocks createTeam).
