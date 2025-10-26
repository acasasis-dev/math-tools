from .mean import mean
from math_tools.tools.latex import new_line, sigma


def variance(data, label=None, population="full", tabs=1):
	kwargs = locals()
	output = "\\begin{gather*}\n"
	_mean_latex, _mean = mean(**kwargs)
	output += _mean_latex
	prefix = f"{sigma() if population == "full" else "s^2"} = "
	numerator_first_step = []
	numerator_second_step = []
	squared_deviations = []
	for num in data:
		numerator_first_step.append(f"({num} - {_mean})^2")
		numerator_second_step.append(f"({round(num - _mean, 2)})^2")
		squared_deviations.append(round((num - _mean)**2, 2))

	output += "\\end{gather*}"

	return output
