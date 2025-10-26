from math_tools.tools.latex import frac, text, new_line
from .mean import mean

from statistics import mean as m


def covariance(x, y, labels=("x", "y"), environment=True):
	if len(x) != len(y):
		raise Exception(f"length of x must be the same as y. {len(x)} != {len(y)}")
	
	if len(labels) != 2:
		raise Exception(f"length of labels must exactly be 2")

	x_label, y_label = labels

	x_latex = mean(x, x_label, environment=False)
	x_mean = m(x)
	output = x_latex
	y_latex = mean(y, y_label, environment=False)
	y_mean = m(y)
	output += y_latex
	output += f"\t{new_line()}"
	cov_prefix = f"\tCov[{text(x_label)}, {text(y_label)}] = "
	output += cov_prefix
	cov_numerator = []
	cov_numerator_products = []
	for i in range(len(x)):
		cov_numerator.append(f"({round(x[i] - x_mean, 2)})({round(y[i] - y_mean, 2)})")
		cov_numerator_products.append(round((x[i] - x_mean) * (y[i] - y_mean), 2))
	
	cov_solving_steps = [
		f"{frac(" + ".join(cov_numerator), f'{len(x)} - 1')} {new_line()}",
		f"{frac(" + ".join(list(map(str, cov_numerator_products))), len(x) - 1)} {new_line()}",
		f"{frac(round(sum(cov_numerator_products), 2), len(x) - 1)} {new_line()}",
		f"{round(sum(cov_numerator_products) / (len(x) - 1), 2)} \n"
	]

	output += f"{cov_prefix}".join(cov_solving_steps)

	if environment:
		output = (
			"\\begin{gather*}\n"
			f"{output}"
			"\\end{gather*}"
		)

	return output
