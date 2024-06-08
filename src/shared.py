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

import sys
import os

def make_dirs(path):
    # Create directory at given path 
    if not os.path.exists(path):
        os.makedirs(path)

def blockPrint():
    # Disable print
    sys.stdout = open(os.devnull, 'w')

def enablePrint():
    # Enable print
    sys.stdout = sys.__stdout__
