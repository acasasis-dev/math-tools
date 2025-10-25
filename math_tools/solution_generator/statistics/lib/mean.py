from statistics import mean as m
from math_tools.tools.latex import bar, frac, new_line, mu, x_bar


def mean(data, label=None, population="full", tabs=1):
	if population not in ["full", "sample"]:
		raise Exception("Invalid population")

	points_mean = m(data)
	points_stringified = " + ".join(list(map(str, data)))
	points_len = len(data)
	prefix = mu(label) if population == "full" else x_bar
	return f"{'\t' * tabs}{prefix} = {frac(points_stringified, points_len)} = {frac(sum(data), points_len)} = {points_mean} {new_line()}", points_mean
