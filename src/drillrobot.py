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

from .miningproblem import MiningProblem
from .filereader import FileReader
from aima.search import SimpleProblemSolvingAgentProgram

class DrillRobot(SimpleProblemSolvingAgentProgram):

    def __init__(self, txtfilepath):
        reader = FileReader(txtfilepath)

        super().__init__(reader.initial_state)
        self.matrix_size = reader.matrix_size
        self.map = reader.matrix
        self.goal = reader.goal_state

    def solve(self, search_algorithm, h=None):
        """Formulate a problem, then search for a sequence
        of actions to solve it."""
        problem = self.formulate_problem(h)
        self.seq = self.search(problem, search_algorithm)
        return self.seq

    def formulate_problem(self, h):
        return MiningProblem(self.state, self.map, self.matrix_size, h, self.goal)

    def search(self, problem, search_algorithm):
        return search_algorithm(problem)
