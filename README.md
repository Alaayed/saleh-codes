# saleh-codes

A personal archive of competitive programming, CTF challenges, coursework, and finance notes.
Not a polished project--more like a well-worn notebook that I keep coming back to.

---

## What's in here

### codeforces/
Codeforces contest submissions. Some clean, some written in the last 30 seconds of a round.
Covers Div. 2/3 rounds and a few global rounds. Fast I/O, hacky tricks, and the occasional
"why did I think this would work" comment left in by accident.

### cp2/ & cp3/
Coursework at Purdue, specifically the competitive programming courses. `cp2` has the
earlier weeks of CS 31100 plus NAQ competition material. `cp3` goes deeper: topics 0–7 covering greedy,
DP, graph theory, min-cost max-flow, and more. A lot of the harder problems in here genuinely
took me a while.

### Data Structures/
Reusable templates I keep pulling out: sparse table, string hashing, min-cost max-flow,
fast factorials. If something shows up in more than one contest, it earns a spot here.

### leetcode/
LeetCode problems across easy/medium/hard, plus weekly contest submissions. Tends to overlap
with CP topics--if I'm drilling a concept, it shows up in both places.

### CTFs/
CTF challenge solutions and notes. Covers binary exploitation (format strings, heap),
crypto, and some misc.

### kaggle/Titanic/
The classic Titanic ML problem. A rough first attempt with pandas and sklearn. Nothing
sophisticated, just getting a feel for the workflow.

### CFA Notes Vault/
Obsidian notes from my CFA Level I prep. Time Value of Money, Rates & Returns,
Equity Securities, and more. Also has some older university exam notes buried in `OLD/`
that I haven't had the heart to delete.

### scratch/
The junk drawer. Quick experiments, half-finished ideas, and one-off scripts that
haven't found a home yet. Useful to have, embarrassing to show.

---

## Languages

**Python** for almost everything. **C++** when Python is too slow or I'm feeling ambitious.
Occasional **C** when a LeetCode problem is easy and I want to suffer slightly.

---

## Running things

Solutions are standalone--no build system, no dependencies (usually).

```bash
# Python
python3 solution.py < input.txt

# C++ 
g++ -std=c++17 -O3 solution.cpp -o solution
./solution < input.txt
```

For the Obsidian notes, open `CFA Notes Vault/` as a vault in [Obsidian](https://obsidian.md).

---

## Disclaimer

A lot of this was written fast--under contest pressure, late at night, or as a quick
experiment I meant to clean up later. Comments are sparse, variable names are sometimes
just `x`, and some solutions are wrong in interesting ways. Use at your own risk.
