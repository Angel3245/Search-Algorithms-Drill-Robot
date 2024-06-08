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

from .actions import *
from aima.search import *

class MiningProblem(Problem):
    def __init__(self, initial, map, matrix_size, h_function=None, goal=None):
        self.initial = initial
        self.goal = goal
        self.actions_list = [MoveForwardAction(), ClockwiseAction(), CounterClockwiseAction()]
        self.map = map
        self.matrix_size = matrix_size
        self.h_function = h_function


    def actions(self, state):
        """Returns a list of the actions that can be executed in state."""
        # Current positions of the state
        x = state.x
        y = state.y
        # Current orientation of the state
        o = state.orientation

        # Map row and column limits
        max_x = self.matrix_size[0]-1
        max_y = self.matrix_size[1]-1

        # List of possible actions to perform depending on the current state
        actions = []
                
        # If not exceeding the limits of the map moving forwards
        if 0 <= x+state.movement[0] <= max_x and 0 <= y+state.movement[1] <= max_y:
            # Add it to the list of possible actions
            actions.append(self.actions_list[0])
        else:
            print(f"{state}: Action unavailable: {self.actions_list[0].name}")

        # Add CounterClockwise and Clockwise to the list of actions
        actions.append(self.actions_list[1])
        actions.append(self.actions_list[2])

        return actions
    


    def result(self, state, action):
        """Executes an action in a state and returns its result"""
        if not action in self.actions_list:
            raise ValueError(f"Invalid action: {action}")

        print(action)
        new_state = action.execute(state)
        return new_state


    def goal_test(self, state):
        """Determines whether a given state s is a goal state g"""
        return state.x == self.goal.x and state.y == self.goal.y


    def path_cost(self, c, state1, action, state2):
        """Returns the sum of the costs of the accumulated actions along the path (c)
        plus the cost of the actual action (taking action to get from state1 to state2)"""
        if action.name == self.actions_list[0].name:
            cost_edge = self.map[state2.x][state2.y]
            action_cost = cost_edge
        else:
            action_cost = 1

        return c + action_cost
       


    def h(self, node):
        """Returns least possible cost to reach a goal for the given state."""
        if(self.h_function == None):
            return None
        
        return self.h_function(self,node)
    

    def value(self, state):
        """Returns the hardness of the subsoil rock at state location in the matrix coding of the terrain map."""
        return self.map[state.x][state.y]


    def __str__(self):
        return f"Starting Problem at: {self.initial}. Goal at: {self.goal}"