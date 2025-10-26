from .mean import mean
from math_tools.tools.latex import new_line, sigma, frac, text


def variance(data, label=None, population="full", tabs=1):
	kwargs = locals()
	output = "\\begin{gather*}\n"
	_mean_latex, _mean = mean(**kwargs)
	output += _mean_latex + f"\t{new_line()}"
	prefix = f"{sigma() if population == "full" else f"s^2"}"
	prefix = f"{prefix}{"_" + text(label) if label else ""} = "
	data_len = len(data)
	denominator = data_len if population == "full" else data_len - 1
	numerator_first_step = []
	numerator_second_step = []
	squared_deviations = []
	for num in data:
		numerator_first_step.append(f"({num} - {_mean})^2")
		numerator_second_step.append(f"({round(num - _mean, 2)})^2")
		squared_deviations.append(round((num - _mean)**2, 2))

	steps = [
		numerator_first_step,
		numerator_second_step,
		list(map(str, squared_deviations)),
		[str(sum(squared_deviations))],
		str(round(sum(squared_deviations) / denominator, 2))
	]
	for i in range(len(steps)):
		output += f"{"\t" * tabs}{prefix} "
		if i == len(steps) - 1:
			output += f"{steps[i]} \n"
		else:
			output += (
				f"{frac(
					" + ".join(steps[i]),
					denominator
				)} {new_line()}"
			)

	output += "\\end{gather*}"

	return output
