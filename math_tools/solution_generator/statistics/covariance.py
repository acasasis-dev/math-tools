from math_tools.tools.latex import frac, text, new_line
from .lib import Equation
from .mean import Mean


class Covariance(Equation):
	def __init__(self, x, y, labels=("x", "y"), environment=True):
		self.x = x
		self.y = y
		self.labels = labels
		self.environment = environment

	@property
	def latex(self):
		if len(self.x) != len(self.y):
			raise Exception(f"length of x must be the same as y. {len(self.x)} != {len(self.y)}")
		
		if len(self.labels) != 2:
			raise Exception(f"length of labels must exactly be 2")

		x_label, y_label = self.labels

		x_mean_obj = Mean(self.x, x_label, environment=False)
		x_latex = x_mean_obj.latex
		x_mean = x_mean_obj.result
		output = x_latex
		y_mean_obj = Mean(self.y, y_label, environment=False)
		y_latex = y_mean_obj.latex
		y_mean = y_mean_obj.result
		output += y_latex
		output += f"\t{new_line()}"
		cov_prefix = f"\tCov[{text(x_label)}, {text(y_label)}] = "
		output += cov_prefix
		cov_numerator = []
		cov_numerator_products = []
		for i in range(len(self.x)):
			cov_numerator.append(f"({round(self.x[i] - x_mean, 2)})({round(self.y[i] - y_mean, 2)})")
			cov_numerator_products.append(round((self.x[i] - x_mean) * (self.y[i] - y_mean), 2))
		
		cov_solving_steps = [
			f"{frac(" + ".join(cov_numerator), f'{len(self.x)} - 1')} {new_line()}",
			f"{frac(" + ".join(list(map(str, cov_numerator_products))), len(self.x) - 1)} {new_line()}",
			f"{frac(round(sum(cov_numerator_products), 2), len(self.x) - 1)} {new_line()}",
			f"{round(sum(cov_numerator_products) / (len(self.x) - 1), 2)} \n"
		]

		output += f"{cov_prefix}".join(cov_solving_steps)

		if self.environment:
			output = (
				"\\begin{gather*}\n"
				f"{output}"
				"\\end{gather*}"
			)

		return output
