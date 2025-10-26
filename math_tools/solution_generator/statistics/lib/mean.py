from statistics import mean as m
from math_tools.tools.latex import frac, new_line, mu, x_bar


def mean(data, label=None, population="full", tabs=1, environment=True):
	if population not in ["full", "sample"]:
		raise Exception("Invalid population")

	points_mean = round(m(data), 2)
	points_stringified = " + ".join(list(map(str, data)))
	points_len = len(data)
	prefix = mu(label) if population == "full" else x_bar(label)
	output = f"{'\t' * tabs}{prefix} = {frac(points_stringified, points_len)} = {frac(sum(data), points_len)} = {points_mean} {new_line()}"
	if environment:
		output = (
			"\\begin{gather*} \n"
			f"{output}"
			"\\end{gather*}"
		)

	return output
