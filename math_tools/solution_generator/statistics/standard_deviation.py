from .variance import Variance
from math_tools.tools.latex import get_sd_symbol, sqrt, new_line
from .lib import StatisticsEquation
from .variance import Variance
from math import sqrt as s


class StandardDeviation(Variance):
	def __init__(self, data, label=None, population="full", tabs=1, environment=True):
		super().__init__(data, label, population, tabs, False)
		self.environment = environment
		self.init_equation()

	def init_equation(self):
		pass

	@property
	def result(self):
		pass

	@property
	def latex(self):
		_variance_obj = Variance(
			self.data,
			self.label,
			self.population,
			self.tabs,
			environment=False
		)
		_variance_latex = _variance_obj.latex
		_variance = _variance_obj.result
		output = _variance_latex + new_line()
		prefix = get_sd_symbol(self.population, self.label)
		output += f"{"\t" * self.tabs}{prefix} {sqrt(round(_variance, 2))} {new_line()}"
		output += f"{"\t" * self.tabs}{prefix} {round(s(round(_variance, 2)), 2)} {new_line()}"
		
		if self.environment:
			output = (
				"\\begin{gather*}\n"
				f"{output}"
				"\\end{gather*}"
			)
		return output
