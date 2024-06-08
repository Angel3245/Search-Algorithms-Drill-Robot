# Copyright (C) 2024  Jose Ángel Pérez Garrido
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import sys, argparse, csv
from src.shared import make_dirs
from pathlib import Path
from aima.search import breadth_first_graph_search, breadth_first_graph_search_full, depth_first_graph_search, depth_first_graph_search_full, astar_search
from src.heuristic_functions import h1, h2, h3
from src.drillrobot import DrillRobot
from src.filewriter import FileWriter
from src.evaluator import Evaluator

RESULTS_FOLDER_NAME = 'maps'

# Mapping methods and heuristics to their functions
METHODS = {
    'breadth': breadth_first_graph_search_full,
    'depth': depth_first_graph_search_full,
    'astar': astar_search
}

HEURISTICS = {
    'h1': h1,
    'h2': h2,
    'h3': h3
}

def validate_inputs(args):
    if args.method not in METHODS:
        print("Not enough commands or badly written.")
        sys.exit(1)
    if args.method in ('breadth', 'depth') and args.heuristic:
        print("Depth and Breadth search does not need a heuristic function.")
        sys.exit(1)
    if args.method == 'astar':
        if not args.heuristic:
            print("Astar searches need a heuristic to work.")
            sys.exit(1)
        if args.heuristic not in HEURISTICS:
            print("Heuristic does not exist.")
            sys.exit(1)

def execute_method(agent, method_input, heuristic_input):
    if method_input == "astar":
        heuristic_func = HEURISTICS[heuristic_input]
        return agent.solve(METHODS[method_input], heuristic_func)
    else:
        return agent.solve(METHODS[method_input])

def generate_performance_report():
    input_str = f"{Path.cwd()}/{RESULTS_FOLDER_NAME}"
    make_dirs(input_str)

    print("Search algorithms and heuristics functions: {} {} {} {} {} {}".format(
        *METHODS.keys(), *HEURISTICS.keys()))

    # Generate random maps of size 3x3, 5x5, 7x7 and 9x9
    for m_size in [3, 5, 7, 9]:
        FileWriter(input_str, m_size).create_files()
        ev = Evaluator(DrillRobot, list(METHODS.values()), list(HEURISTICS.values()))
        table_performance = ev.evaluate(input_str, m_size)

        print(f"Table for map size: {m_size}x{m_size}")
        print(table_performance, "\n")

        csv_file = f'{input_str}/data{m_size}.csv'
        with open(csv_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(table_performance)
        print(f'CSV file "{csv_file}" has been created.')

def main():
    # Parse args
    parser = argparse.ArgumentParser(description='DrillRobot Search Algorithm')
    parser.add_argument('--input_map', required=True, help='Input file map')
    parser.add_argument('--method', required=False, default="breadth", choices=METHODS.keys(), help='Search method to use')
    parser.add_argument('--heuristic', choices=HEURISTICS.keys(), help='Heuristic function for A* search')
    parser.add_argument('--report', required=False, type=bool, default=False, help='Generate random maps and create an evaluation report of the different search algorithms')

    args = parser.parse_args()
    
    validate_inputs(args)

    # Create agent
    agent = DrillRobot(args.input_map)

    if args.report:
        generate_performance_report()
    else:
        is_solved, solution, explored, frontier = execute_method(agent, args.method, args.heuristic)

        print("Total number of items in explored list:", len(explored))
        print("Total number of items in frontier:", len(frontier))
        print("Cost:", solution.path_cost)
        print("Depth:", solution.depth)
        print("Solution found!" if is_solved else "Solution not found")

        path = ", ".join(step.name for step in solution.solution())
        print("Solution Path:", path)

if __name__ == "__main__":
    main()
