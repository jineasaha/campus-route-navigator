import csv
from pathlib import Path

ROUTE_CASES = [
    ("Reception", "Library"),
    ("Canteen", "New Building 2"),
    ("Entry Gate 1", "CSE Laboratory"),
    ("Auditorium Hall", "CSE_AKC Seminar Hall"),
    ("Library", "Canteen"),
    ("CSE_Reflxon Room", "Entry Gate 2"),
    ("Parking Area", "New Building 1"),
    ("Entry Gate 2", "CSE_AKC Seminar Hall")
]

def run_cases(campus, agents, filename="output/results.csv"):
    results = []
    for start, finish in ROUTE_CASES:
        for agent in agents:
            answer = agent.route(start, finish)
            results.append({
                "start": start,
                "destination": finish,
                "agent": agent.title,
                "path": " -> ".join(answer.path) if answer.path else "No route",
                "cost_m": answer.cost,
                "nodes_explored": answer.explored,
                "time_seconds": f"{answer.seconds:.8f}"
            })
    destination = Path(filename)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)
    return results
