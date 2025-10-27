from .variance import variance
from math_tools.tools.latex import get_sd_symbol, sqrt, new_line

from statistics import variance as v
from math import sqrt as s


def standard_deviation(data, label=None, population="full", tabs=1, environment=True):
	kwargs = locals()
	kwargs.pop("environment")
	_variance = variance(**kwargs, environment=False)
	output = _variance + new_line()
	prefix = get_sd_symbol(population, label)
	output += f"{"\t" * tabs}{prefix} {sqrt(round(v(data), 2))} {new_line()}"
	output += f"{"\t" * tabs}{prefix} {round(s(round(v(data), 2)), 2)} {new_line()}"
	
	if environment:
		output = (
			"\\begin{gather*}\n"
			f"{output}"
			"\\end{gather*}"
		)
	return output
