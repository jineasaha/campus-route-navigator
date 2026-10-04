# AI Campus Route Navigator — Alternate Implementation

An object-oriented implementation comparing PATHFINDER (Greedy Best-First Search) and ORBIT (A* Search).

## Requirements
Python 3.9 or later. Only the Python standard library is used.

## Run the navigator
```bash
python main.py
```
Enter the starting location and destination exactly as named in `campus.json`.

To pass locations directly:
```bash
python main.py --start "Reception" --goal "Library"
```

To run all route comparisons and regenerate the CSV:
```bash
python main.py --experiment
```

The measurements are written to `output/results.csv`.

## Project files
- `campus.json` — graph locations and approximate walking costs
- `network.py` — graph loading, heuristic, and CSE movement restrictions
- `routing.py` — priority-queue search implementation
- `bots.py` — PATHFINDER and ORBIT agent classes
- `trials.py` — test routes and CSV output
- `main.py` — command-line interface
- `REPORT.md` — brief report

The connections and distances are estimates interpreted from the assignment map. Verify them against campus walkways before submission.
