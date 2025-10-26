from .mean import mean
from math_tools.tools.latex import new_line


def variance(data, label=None, population="full", tabs=1):
	kwargs = locals()
	output = "\\begin{gather*}\n"
	_mean_latex, _mean = mean(**kwargs)
	output += _mean_latex
	output += "\\end{gather*}"
	
	return output
