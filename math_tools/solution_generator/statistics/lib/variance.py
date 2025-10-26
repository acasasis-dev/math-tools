from .mean import mean
from math_tools.tools.latex import new_line, sigma, frac, text


def variance(data, label=None, population="full", tabs=1):
	kwargs = locals()
	output = "\\begin{gather*}\n"
	_mean_latex, _mean = mean(**kwargs)
	output += _mean_latex + f"\t{new_line()}"
	prefix = f"{sigma(label) if population == "full" else f"s^2_{text(label)}"} = "
	data_len = len(data)
	numerator_first_step = []
	numerator_second_step = []
	squared_deviations = []
	for num in data:
		numerator_first_step.append(f"({num} - {_mean})^2")
		numerator_second_step.append(f"({round(num - _mean, 2)})^2")
		squared_deviations.append(round((num - _mean)**2, 2))

	output += (
		f"{"\t" * tabs}{prefix} "
		f"{
			frac(
				" + ".join(numerator_first_step),
				data_len if population == "full" else f"{data_len} - 1"
			)
		} "
		f"{new_line()}"
	)
	output += "\\end{gather*}"

	return output
