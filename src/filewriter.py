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

import random
from .state import State

class FileWriter:

    def __init__(self, folder, matrix_size):
        self.folder = folder
        self.matrix_size = matrix_size

    def create_files(self):
        # Create 10 matrixes of the given size
        for i in range(1, 11):  # 1...10

            # String to get the location of the folder
            foldr_str = str.format(
                "{}/{}x{}_{}.txt", self.folder, self.matrix_size, self.matrix_size, i
            )

            # Write the information in the file
            with open(foldr_str, 'w') as fp:
                self.write_map_size(fp)
                self.write_map(fp)
                self.write_initial_state(fp)
                self.write_goal_state(fp)

    def write_map_size(self, fp):
        # Write map size in proper format to file
        fp.write(str(self.matrix_size)+" "+str(self.matrix_size) + "\n")

    def write_map(self, fp):
        # Go through the rows of the matrix
        for i in range(0, self.matrix_size):
            numbers = []

            # Go through the columns of the matrix
            for j in range(0, self.matrix_size):
                # Generate a random value for the row i and column j
                elem_val = str(random.randint(1, 9))
                numbers.append(elem_val)

            # Join all numbers of the line in a string
            line = " ".join([num for num in numbers])
            # Write the line of map in proper format to file
            fp.write(line + "\n")

    def write_initial_state(self, fp):
        # Write initial state in proper format to file
        fp.write("0 0 0\n")

    def write_goal_state(self, fp):
        # Write goal state in proper format to file
        fp.write(str.format("{} {} {}", self.matrix_size-1, self.matrix_size-1, 8))
