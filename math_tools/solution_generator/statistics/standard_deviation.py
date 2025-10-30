from .variance import Variance
from math_tools.tools.latex import get_sd_symbol, sqrt, new_line
from .lib import StatisticsEquation
from .variance import Variance
from math import sqrt as s


class StandardDeviation(Variance):
	def __init__(self, data, label=None, population="full", tabs=1, environment=True):
		self._variance_obj = super().__init__(data, label, population, tabs, False)
		self.environment = environment
		_variance_obj = super()
		self._variance_latex = _variance_obj.latex
		self._variance = _variance_obj.result

	@property
	def result(self):
		pass

	@property
	def latex(self):
		output = self._variance_latex + new_line()
		prefix = get_sd_symbol(self.population, self.label)
		output += f"{"\t" * self.tabs}{prefix} {sqrt(round(self._variance, 2))} {new_line()}"
		output += f"{"\t" * self.tabs}{prefix} {round(s(round(self._variance, 2)), 2)} {new_line()}"
		
		if self.environment:
			output = (
				"\\begin{gather*}\n"
				f"{output}"
				"\\end{gather*}"
			)
		return output
