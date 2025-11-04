from .lib import StatisticsEquation
from math_tools.tools.latex import new_line, frac, get_sd_symbol
from .mean import Mean


class Variance(StatisticsEquation):
	def __init__(self, data, label=None, population="full", tabs=1, environment=True):
		super().__init__(data, label, population, tabs, environment)
		_mean_obj = Mean(
			self.data,
			self.label,
			self.population,
			self.tabs,
			False
		)
		self._mean = _mean_obj.result
		self.data_len = len(self.data)
		self.denominator = self.data_len if self.population == "full" else self.data_len - 1
		self.squared_deviations = list(map(lambda num: round((num - self._mean)**2, 2), self.data))
		self.squared_deviations_sum = round((sum(self.squared_deviations)), 2)
		self._mean_latex = _mean_obj.latex

	@property
	def result(self):
		return round(self.squared_deviations_sum / self.denominator, 2)

	@property
	def latex(self):
		output = self._mean_latex + f"\t{new_line()}"
		prefix = get_sd_symbol(self.population, self.label, variance=True)
		numerator_first_step = []
		numerator_second_step = []
		for num in self.data:
			numerator_first_step.append(f"({num} - {self._mean})^2")
			numerator_second_step.append(f"({round(num - self._mean, 2)})^2")

		steps = [
			numerator_first_step,
			numerator_second_step,
			list(map(str, self.squared_deviations)),
			[str(self.squared_deviations_sum)],
			str(self.result)
		]
		for i in range(len(steps)):
			output += f"{"\t" * self.tabs}{prefix} "
			if i == len(steps) - 1:
				output += f"{steps[i]} \n"
			else:
				output += (
					f"{frac(
						" + ".join(steps[i]),
						self.denominator
					)} {new_line()}"
				)

		self.output = output

		return super(StatisticsEquation, self).latex
