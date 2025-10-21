from statistics import mean

def points_mean_solution_latex(points, points_label):
	points_mean = mean(points)
	points_stringified = " + ".join(list(map(str, points)))
	points_len = len(points)
	return (
		f"\t\\sigma_{{\\text{{{points_label}}}}} = \\frac{{{points_stringified}}}{{{points_len}}} = \\frac{{{sum(points)}}}{{{points_len}}} = {points_mean} \\\\\n"
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
	output += "\t\\\\\n"
	cov_prefix = f"\tCov[\\text{{{x_label}}}, \\text{{{y_label}}}] = "
	output += cov_prefix
	cov_numerator = []
	cov_numerator_products = []
	for i in range(len(x)):
		cov_numerator.append(f"({x[i] - x_mean})({y[i] - y_mean})")
		cov_numerator_products.append((x[i] - x_mean) * (y[i] - y_mean))
	
	output += f"\\frac{{{" + ".join(cov_numerator)}}}{{{len(x)} - 1}} \\\\ \n"
	output += cov_prefix
	output += f"\\frac{{{" + ".join(list(map(str, cov_numerator_products)))}}}{{{len(x) - 1}}} \\\\ \n"
	output += cov_prefix
	output += f"\\frac{{{sum(cov_numerator_products)}}}{{{len(x) - 1}}} \\\\ \n"
	output += cov_prefix
	output += f"{sum(cov_numerator_products) / (len(x) - 1)} \n"

	output += "\\end{gather*}"
	return output
