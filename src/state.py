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

class State:
            
    # Correspondence between numbers and names of the orientations
    ORIENTATION_NAMES = {0:"North", 1:"Northeast", 2:"East", 3:"Southeast", 4:"South", 
                         5:"Southwest", 6:"West", 7:"Northwest", 8:"Any"}
    
    # Movements to be performed according to the orientation
    ORIENTATION_TRAD = {0:(-1,0), 1:(-1,1), 2:(0,1), 3:(1,1), 4:(1,0), 5:(1,-1), 
                        6:(0,-1), 7:(-1,-1), 8:(0,0)}


    def __init__(self, x: int, y: int, o: int):
        self.position = (x, y)
        self.orientation = o


    @property
    def x(self):
        # The row number of the state
        return self.position[0]

    @property
    def y(self):
        # The column number of the state
        return self.position[1]

    @property
    def movement(self):
        # The movement to be performed according to the orientation of the state
        return self.ORIENTATION_TRAD[self.orientation]

    @property
    def state(self):
        # The position and orientation of the state
        return (self.position, self.orientation)


    def get_orientation(self, orientation):
        # The movement to be performed according to a given orientation
        return self.ORIENTATION_TRAD[orientation]


    def __str__(self):
        # String of the state in proper format
        orient = State.ORIENTATION_NAMES[self.orientation]
        return str.format("({},{},{})", self.position[0], self.position[1], orient)

    def __eq__(self, new_value):
        # If the state is equal to another given state
        return self.position[0] == new_value.position[0] and \
            self.position[1] == new_value.position[1] and \
            self.orientation == new_value.orientation
    
    def __lt__(self, new_value):
        # If the state is less than another given state
        return 0
    
    def __hash__(self):
        # Calculate hash based on state position
        return hash(self.position)