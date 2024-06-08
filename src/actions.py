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

class Action:
    def __init__(self, name=''):
        self._name = name
          
    def execute(self,state):
        # Execute the action and return the new state
        raise NotImplemented
    
    @property
    def name(self):
        # The name of the action
        return self._name
    
    def __repr__(self):
        # The representation of the action
        return f"Operator {self._name}"
    


class MoveForwardAction(Action):
    def __init__(self):
        super().__init__(self.__class__.__name__)
        
    def execute(self,state):
        # Calculate the new position based on the current position and orientation
        x=state.position[0]+state.movement[0]
        y=state.position[1]+state.movement[1]
        # New state after moving a position forward
        return State(x, y, state.orientation)
        
    

class ClockwiseAction(Action):
    def __init__(self):
        super().__init__(self.__class__.__name__)
    
    def execute(self,state):
        # Calculate the new orientation based on the current one
        # Uses the modulus to limit orientation to the range (0, 1, 2, ... 7)
        orient = (state.orientation + 1) % 8
        # New state after rotating 45 degrees clockwise
        return State(state.x, state.y, orient)
    

    
class CounterClockwiseAction(Action):
    def __init__(self):
        super().__init__(self.__class__.__name__)
        
    def execute(self,state):
        # Calculate the new orientation based on the current one
        # Uses the modulus to limit orientation to the range (0, 1, 2, ... 7)
        orient = (state.orientation - 1) % 8
        # New state after rotating 45 degrees counterclockwise
        return State(state.x, state.y, orient)