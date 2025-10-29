from .mean import Mean
from math_tools.tools.latex import new_line, frac, get_sd_symbol
from .lib import StatisticsEquation
from .mean import Mean


class Variance(Mean):
	def __init__(self, data, label=None, population="full", tabs=1, environment=True):
		super().__init__(data, label, population, tabs, False)
		self.environment = environment
		self.init_equation()
	
	def init_equation(self):
		pass

	@property
	def result(self):
		return

	@property
	def latex(self):
		_mean_obj = Mean(
			self.data,
			self.label,
			self.population,
			self.tabs,
			environment=False
		)
		_mean_latex = _mean_obj.latex
		_mean = _mean_obj.result
		output = _mean_latex + f"\t{new_line()}"
		prefix = get_sd_symbol(self.population, self.label, variance=True)
		data_len = len(self.data)
		denominator = data_len if self.population == "full" else data_len - 1
		numerator_first_step = []
		numerator_second_step = []
		squared_deviations = []
		for num in self.data:
			numerator_first_step.append(f"({num} - {_mean})^2")
			numerator_second_step.append(f"({round(num - _mean, 2)})^2")
			squared_deviations.append(round((num - _mean)**2, 2))

		squared_deviations_sum = round(sum(squared_deviations), 2)
		_variance = round(squared_deviations_sum / denominator, 2)
		steps = [
			numerator_first_step,
			numerator_second_step,
			list(map(str, squared_deviations)),
			[str(squared_deviations_sum)],
			str(_variance)
		]
		for i in range(len(steps)):
			output += f"{"\t" * self.tabs}{prefix} "
			if i == len(steps) - 1:
				output += f"{steps[i]} \n"
			else:
				output += (
					f"{frac(
						" + ".join(steps[i]),
						denominator
					)} {new_line()}"
				)

		if self.environment:
			output = (
				"\\begin{gather*}\n"
				f"{output}"
				"\\end{gather*}"
			)

		return output
