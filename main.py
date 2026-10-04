import argparse
import textwrap

from network import CampusNetwork
from bots import Pathfinder, Orbit
from trials import run_cases

def print_result(agent, start, finish):
    result = agent.route(start, finish)
    print()
    print("+" + "-" * 58 + "+")
    print(f"| {agent.title:<56} |")
    print("+" + "-" * 58 + "+")
    print("Route           :", " -> ".join(result.path) if result.path else "No valid route")
    print("Total cost      :", f"{result.cost} m" if result.path else "N/A")
    print("Nodes explored  :", result.explored)
    print(f"Execution time  : {result.seconds:.6f} s")
    print("+" + "-" * 58 + "+")

def main():
    parser = argparse.ArgumentParser(description="AI Campus Route Navigator")
    parser.add_argument("--start")
    parser.add_argument("--goal")
    parser.add_argument("--experiment", action="store_true")
    options = parser.parse_args()

    campus = CampusNetwork()
    agents = [Pathfinder(campus), Orbit(campus)]

    if options.experiment:
        data = run_cases(campus, agents)
        print()
        print("=" * 60)
        print("CAMPUS ROUTE EXPERIMENT")
        print("=" * 60)
        print(f"Agent-runs completed : {len(data)}")
        print("CSV saved at         : output/results.csv")
        print("=" * 60)
        return

    print()
    print("=" * 60)
    print("AI CAMPUS ROUTE NAVIGATOR")
    print("=" * 60)
    print(textwrap.fill(" | ".join(campus.places), width=76))
    start = options.start or input("\nStarting location: ").strip()
    finish = options.goal or input("Destination: ").strip()

    if start not in campus.places or finish not in campus.places:
        print("Invalid location. Select names from the list above.")
        return

    print()
    print(f"Journey: {start} -> {finish}")
    for agent in agents:
        print_result(agent, start, finish)

if __name__ == "__main__":
    main()
