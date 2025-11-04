from math_tools.tools.latex import frac, text, new_line
from .lib import StatisticsEquation
from .mean import Mean


class Covariance(StatisticsEquation):
	def __init__(self, data, label=("x", "y"), population="full", tabs=1, environment=True):
		super().__init__(data, label, population, tabs, environment)
		if len(self.data) != 2:
			raise Exception(f"length of data must exactly be 2")
		
		self.x, self.y = data
		if len(self.x) != len(self.y):
			raise Exception(f"length of x must be the same as y. {len(self.x)} != {len(self.y)}")
		
		if len(self.label) != 2:
			raise Exception(f"length of labels must exactly be 2")
		
		self.x_label, self.y_label = self.label

		x_mean_obj = Mean(self.x, self.x_label, environment=False)
		self.x_latex = x_mean_obj.latex
		self.x_mean = x_mean_obj.result
		y_mean_obj = Mean(self.y, self.y_label, environment=False)
		self.y_latex = y_mean_obj.latex
		self.y_mean = y_mean_obj.result
		self.data_len = len(self.x)
		self.denominator = self.data_len if self.population == "full" else self.data_len - 1
		self.cov_numerator_products = []
		for i in range(len(self.x)):
			self.cov_numerator_products.append(round((self.x[i] - self.x_mean) * (self.y[i] - self.y_mean), 2))

	@property
	def result(self):
		
		return round(sum(self.cov_numerator_products) / self.denominator, 2)

	@property
	def latex(self):
		output = self.x_latex
		output += self.y_latex
		output += f"\t{new_line()}"
		cov_prefix = f"\tCov[{text(self.x_label)}, {text(self.y_label)}] = "
		output += cov_prefix
		cov_numerator = []
		for i in range(len(self.x)):
			cov_numerator.append(f"({round(self.x[i] - self.x_mean, 2)})({round(self.y[i] - self.y_mean, 2)})")
		
		cov_solving_steps = [
			f"{frac(" + ".join(cov_numerator), self.denominator)} {new_line()}",
			f"{frac(" + ".join(list(map(str, self.cov_numerator_products))), self.denominator)} {new_line()}",
			f"{frac(round(sum(self.cov_numerator_products), 2), self.denominator)} {new_line()}",
			f"{self.result} \n"
		]

		output += f"{cov_prefix}".join(cov_solving_steps)
		self.output = output

		return super(StatisticsEquation, self).latex
