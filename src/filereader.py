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

from .state import State

class FileReader:

    def __init__(self,filename) -> None:
        # File with the information
        self.filename = filename

        # Read the information from the file
        with open(self.filename, 'r') as fp:
            self.matrix_size = self.read_map_size(fp)
            self.matrix = self.read_map(fp)
            self.initial_state = self.read_initial_state(fp)
            self.goal_state = self.read_goal_state(fp)


    def read_map_size(self,fp):
        # Read first line to find and return the number of rows and columns
        rows, cols = map(int, fp.readline().split())
        return (rows, cols)
        

    def read_map(self,fp):
        # Read the map data and save it in a matrix
        matrix = []
        for i in range(self.matrix_size[0]):
            row = list(map(int, fp.readline().split()))
            matrix.append(row)
        return matrix
        

    def read_initial_state(self, fp):
        # Read the initial position and orientation of the robot and save it on a tuple
        initial = tuple(map(int, fp.readline().split()))
        return State(initial[0], initial[1], initial[2])
        

    def read_goal_state(self, fp):
        # Read the target position and orientation of the robot and save it on a tuple
        target = tuple(map(int, fp.readline().split()))
        return State(target[0], target[1], target[2])
    

