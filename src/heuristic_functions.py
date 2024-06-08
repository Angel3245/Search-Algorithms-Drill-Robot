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

# Estimate cost based on Euclidean distance to the goal state
def h1(self, node):
    dx = (self.goal.x - node.state.x)**2
    dy = (self.goal.y - node.state.y)**2
    
    # Returns the length of a line between two points
    return ( dx + dy )**0.5

# Estimate cost based on Manhattan distance to the goal state
def h2(self, node):
    dx = abs(self.goal.x - node.state.x)
    dy = abs(self.goal.y - node.state.y)

    # Returns the sum of distances between x and y coordinates
    return dx + dy

# Estimate cost based on weighted distance Manhattan to the goal state
def h3(self, node):
    state_x = node.state.x
    state_y = node.state.y

    target_x = self.goal.x
    target_y = self.goal.y

    weights = 0

    while state_x != target_x:
        if state_x < target_x:
            # Go right
            state_x += 1
            weights += self.map[state_x][state_y]
        else:
            # Go left
            state_x -= 1
            weights += self.map[state_x][state_y]

    while state_y != target_y:
        if state_y < target_y:
            # Go down
            state_y += 1
            weights += self.map[state_x][state_y]
        else:
            # Go up
            state_y -= 1
            weights += self.map[state_x][state_y]

    # Returns the weighted distance between the state and the goal by adding the costs of the subsoil
    return weights
