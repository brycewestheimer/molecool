"""
molecool
A Python package for analyzing and visualizing molecular structures. for MSF bootcamp.
"""

# Add imports here
from .functions import *
from .atom_data import atomic_weights, atom_colors
from .measure import calculate_angle, calculate_distance
from .visualize import draw_molecule, bond_histogram
from .molecule import build_bond_list

# Import I/O subpackage
import molecool.io

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
