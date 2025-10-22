from statistics import mean
from math_tools.tools.latex import frac, text, sigma, new_line


def points_mean_solution_latex(points, points_label):
	points_mean = mean(points)
	points_stringified = " + ".join(list(map(str, points)))
	points_len = len(points)
	return (
		f"\t{sigma(text(points_label))} = {frac(points_stringified, points_len)} = {frac(sum(points), points_len)} = {points_mean} {new_line()}"
	), points_mean

def covariance(x, y, labels=("x", "y")):
	output = "\\begin{gather*}\n"
	if len(x) != len(y):
		raise Exception(f"length of x must be the same as y. {len(x)} != {len(y)}")
	
	if len(labels) != 2:
		raise Exception(f"length of labels must exactly be 2")

	x_label, y_label = labels

	x_latex, x_mean = points_mean_solution_latex(x, x_label)
	output += x_latex
	y_latex, y_mean = points_mean_solution_latex(y, y_label)
	output += y_latex
	output += f"\t{new_line()}"
	cov_prefix = f"\tCov[{text(x_label)}, {text(y_label)}] = "
	output += cov_prefix
	cov_numerator = []
	cov_numerator_products = []
	for i in range(len(x)):
		cov_numerator.append(f"({round(x[i] - x_mean, 2)})({round(y[i] - y_mean, 2)})")
		cov_numerator_products.append(round((x[i] - x_mean) * (y[i] - y_mean), 2))
	
	output += f"{frac(" + ".join(cov_numerator), f'{len(x)} - 1')} {new_line()}"
	output += cov_prefix
	output += f"{frac(" + ".join(list(map(str, cov_numerator_products))), len(x) - 1)} {new_line()}"
	output += cov_prefix
	output += f"\\frac{{{round(sum(cov_numerator_products), 2)}}}{{{len(x) - 1}}} {new_line()}"
	output += cov_prefix
	cov = round(sum(cov_numerator_products) / (len(x) - 1), 2)
	output += f"{cov} \n"

	output += "\\end{gather*}"
	return output
