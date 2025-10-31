from math_tools.tools.latex import frac, text, new_line
from .lib import StatisticsEquation
from .mean import Mean


class Correlation(StatisticsEquation):
	def __init__(self, data, label=("x", "y"), population="full", tabs=1, environment=True):
		super().__init__(data, label, population, tabs, environment)
		