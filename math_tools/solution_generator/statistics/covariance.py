from statistics import mean

def points_mean_solution_latex(points, points_label):
	points_mean = mean(points)
	points_stringified = " + ".join(list(map(str, points)))
	points_len = len(points)
	return (
		f"\t\\sigma_{{\\text{{{points_label}}}}} = \\frac{{{points_stringified}}}{{{points_len}}} = \\frac{{{sum(points)}}}{{{points_len}}} = {points_mean} \\\\\n"
	)

def covariance(x, y, labels=("x", "y")):
	output = "\\begin{gather*}\n"
	if len(x) != len(y):
		raise Exception(f"length of x must be the same as y. {len(x)} != {len(y)}")
	
	if labels:
		if len(labels) != 2:
			raise Exception(f"length of labels must exactly be 2")

	x_label, y_label = labels
	
	output += points_mean_solution_latex(x, x_label)
	output += points_mean_solution_latex(y, y_label)

	output += "\\end{gather*}"
	return output
