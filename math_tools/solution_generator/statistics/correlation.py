from .lib import StatisticsEquation
from .covariance import Covariance
from .standard_deviation import StandardDeviation
from math_tools.tools.latex import new_line, text, frac, get_sd_symbol

class Correlation(StatisticsEquation):
	def __init__(self, data=[], label=("x", "y"), population="full", tabs=1, environment=True, covariance=None, x_sd=None, y_sd=None):
		super().__init__(data, label, population, tabs, environment)
		if self.data and len(self.data) != 2:
			raise Exception(f"length of data must exactly be 2")
		elif self.data:
			self.x, self.y = data
		else:
			self.x, self.y = [[], []]

		if len(self.label) != 2:
			raise Exception(f"length of labels must exactly be 2")
			
		self.x_label, self.y_label = self.label

		sd_symbol = get_sd_symbol(population, label)
		if len(self.x) != len(self.y):
				raise Exception(f"length of x must be the same as y. {len(self.x)} != {len(self.y)}")
		
		if not covariance:
			_covariance = Covariance(
				self.data,
				self.label,
				self.population,
				self.tabs,
				False
			)
			self.covariance = _covariance.result
			self.covariance_latex = _covariance.latex
		else:
			self.covariance = covariance
			self.covariance_latex = f"{"\t" * tabs}Cov[x,y] = {covariance}"

		if not x_sd:
			_x_sd = StandardDeviation(
				self.x,
				self.label,
				self.population,
				self.tabs,
				False
			)
			self.x_sd = _x_sd.result
			self.x_sd_latex = _x_sd.latex
		else:
			self.x_sd = x_sd
			self.x_sd_latex = f"{"\t" * tabs}{sd_symbol}{x_sd}"

		if not y_sd:
			_y_sd = StandardDeviation(
				self.y,
				self.label,
				self.population,
				self.tabs,
				False
			)
			self.y_sd = _y_sd.result
			self.y_sd_latex = _y_sd.latex
		else:
			self.y_sd = y_sd
			self.y_sd_latex = f"{"\t" * tabs}{sd_symbol}{y_sd}"
	
	@property
	def result(self):
		return round(self.covariance / (self.x_sd * self.y_sd), 2)

	@property
	def latex(self):
		output = self.covariance_latex + f"{new_line() * 2}"
		output += self.x_sd_latex + new_line()
		output += self.y_sd_latex + new_line()
		prefix = f"\\rho_{text("".join(self.label))}" if self.population == "full" else f"r_{text("".join(self.label))}"
		output += f"{"\t" * self.tabs}{prefix} = {frac(self.covariance, f"({self.x_sd})({self.y_sd})")} {new_line()}"
		output += f"{"\t" * self.tabs}{prefix} = {frac(self.covariance, round(self.x_sd * self.y_sd, 2))} {new_line()}"
		output += f"{'\t' * self.tabs}{prefix} = {self.result} \n"
		
		if self.environment:
			output = (
				"\\begin{gather*}\n"
				f"{output}"
				"\\end{gather*}"
			)

		return output
