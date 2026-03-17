import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import csv

# --- Read CSV ---
filename = "is_belief_in_god_necessary_to_be_moral__views_differ_widely_by_country_data_2026-03-05.csv"

raw_rows = []
with open(filename, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        raw_rows.append(row)

# Parse data rows (skip header lines, stop at Note/empty)
data = []
prev_group = None
for row in raw_rows:
    if len(row) < 4:
        continue
    country, group, not_nec, nec = row[0], row[1], row[2], row[3]
    if not country or country in ('', 'Group') or not not_nec.lstrip('-').isdigit():
        continue
    # Insert divider when group changes
    if prev_group is not None and group != prev_group:
        data.append((None, None, None, None))
    data.append((country, group, int(not_nec), int(nec)))
    prev_group = group

# Colors matching Pew style
DARK_BLUE  = "#1a6496"   # Not necessary
LIGHT_BLUE = "#8abbd6"   # Necessary

fig_height = 0.38 * len(data) + 2.5
fig, ax = plt.subplots(figsize=(7.5, fig_height))

y_positions = list(range(len(data)))
bar_height = 0.72

for i, row in enumerate(data):
    country, group, not_nec, nec = row
    if country is None:
        continue

    y = y_positions[i]

    # "Not necessary" bar goes LEFT from center (negative x)
    ax.barh(y, -not_nec, height=bar_height, color=DARK_BLUE,
            left=0, align='center')

    # "Necessary" bar goes RIGHT from center
    ax.barh(y,  nec,     height=bar_height, color=LIGHT_BLUE,
            left=0, align='center')

    # Labels — only show if bar is wide enough
    if not_nec and not_nec >= 5:
        ax.text(-not_nec / 2, y, str(not_nec),
                ha='center', va='center', fontsize=8.5,
                color='white', fontweight='bold')

    if nec and nec >= 5:
        ax.text(nec / 2, y, str(nec),
                ha='center', va='center', fontsize=8.5,
                color='white', fontweight='bold')

# Country labels on y-axis
ytick_positions = [i for i, r in enumerate(data) if r[0] is not None]
ytick_labels    = [r[0] for r in data if r[0] is not None]
ax.set_yticks(ytick_positions)
ax.set_yticklabels(ytick_labels, fontsize=9)
ax.yaxis.set_tick_params(length=0)

# Draw thin dotted dividers between groups
divider_ys = [i - 0.5 for i, r in enumerate(data) if r[0] is None]
for dy in divider_ys:
    ax.axhline(y=dy, color='#cccccc', linewidth=0.8, linestyle='dotted')

# Spine / axis cleanup — Pew uses no visible x-axis
ax.set_xlim(-102, 102)
ax.set_ylim(-0.8, len(data) - 0.2)
ax.axvline(0, color='white', linewidth=1.2, zorder=3)
ax.set_xticks([])
for spine in ax.spines.values():
    spine.set_visible(False)

# Column header labels at top
top_y = len(data) - 0.3
ax.text(-30, top_y, "Not necessary", ha='center', va='bottom',
        fontsize=9.5, color=DARK_BLUE, fontweight='bold')
ax.text( 30, top_y, "Necessary",     ha='center', va='bottom',
        fontsize=9.5, color=LIGHT_BLUE, fontweight='bold')

# Title + subtitle
fig.text(0.02, 0.995,
         "Is belief in God necessary to be moral? Views differ widely by country",
         ha='left', va='top', fontsize=11, fontweight='bold', wrap=True)
fig.text(0.02, 0.975,
         "% who say it is __ to believe in God in order to be moral and have good values",
         ha='left', va='top', fontsize=8.5, color='#444444', style='italic')

# Footer
fig.text(0.02, 0.01,
         "Note: Those who did not answer are not shown.\n"
         "Source: Spring 2025 Global Attitudes Survey.\n"
         "PEW RESEARCH CENTER",
         ha='left', va='bottom', fontsize=7.5, color='#555555')

plt.subplots_adjust(left=0.22, right=0.97, top=0.93, bottom=0.06)
plt.savefig("god_morality_chart.pdf", bbox_inches='tight', pad_inches=0.15)
print("Saved god_morality_chart.pdf")