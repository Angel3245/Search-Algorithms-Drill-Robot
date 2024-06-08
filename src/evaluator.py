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

from aima.search import breadth_first_graph_search, depth_first_graph_search, astar_search
from .heuristic_functions import h1, h2
from .shared import blockPrint, enablePrint
import time

class Evaluator:

    def __init__(self, agent, search_funcs, heuris_funcs=[h1,h2]):
        self.agent = agent
        self.search_funcs = search_funcs
        self.heuris_funcs = heuris_funcs

        # Create a initial table with fields to 0
        rows = len(search_funcs)+len(heuris_funcs) -1
        self.table_performance = [[0] * 5] * rows


    def evaluate(self, input_folder, m_size):
        # Prevent prints for being shown in terminal
        blockPrint()

        start_time = time.time()
        # Initializate the variables
        d, g, nE, nF, cont_solv = 0, 0, 0, 0, 0

        # For each of the 10 maps of a given size
        for i in range(1, 11): #1...10   

            # Take the map for the agent
            fileinput_str = str.format("{}/{}x{}_{}.txt", input_folder, m_size, m_size, i)
            agent = self.agent(fileinput_str)

            # Control variables to cycle through all the algorithms and heuristics
            actual_algorithm = 0
            only_once = True

            # For each of the algorithms and heuristics
            for search_f in self.search_funcs:
                for heuris_f in self.heuris_funcs:

                    # If it is the astar algorithm, the heuristics are taken into account, if not, no
                    if(search_f == astar_search):
                        # Get solution       
                        is_solved, solution, explored, frontier = agent.solve(search_f, heuris_f)
                    
                    elif only_once:
                        only_once = not only_once
                        # Get solution
                        is_solved, solution, explored, frontier = agent.solve(search_f)
                    
                    else:
                        only_once = not only_once
                        break

                    # Get previous values in table performance
                    d,g,nE,nF,cont_solv = self.table_performance[actual_algorithm]

                    # Update table performance
                    if(is_solved):
                        cont_solv += 1
                        d += solution.depth
                        g += solution.path_cost
                        nE += len(explored)
                        nF += len(frontier)

                    self.table_performance[actual_algorithm] = [d,g,nE,nF,cont_solv]
                    
                    # Go to next algorithm
                    actual_algorithm += 1


        # Compute averages (divide by the number of solved problems)
        for i in range(0,len(self.table_performance)):
            d, g,nE,nF,cont_solv = self.table_performance[i]
            self.table_performance[i] = [d/cont_solv, g/cont_solv,nE/cont_solv,nF/cont_solv]

        elapsed_time = time.time() - start_time
        
        # Enable prints in terminal
        enablePrint()
        
        print(f'Results found in {elapsed_time:.2f} seconds.')
        
        return self.table_performance