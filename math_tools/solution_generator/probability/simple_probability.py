from .lib import ProbabilityEquation

from math_tools.tools.latex import text, frac, new_line


class SimpleProbability(ProbabilityEquation):
	def __init__(self, fav_outcomes, all_outcomes, label, tabs=1):
		super().__init__(fav_outcomes, all_outcomes, label=label, tabs=tabs)

	@property
	def result(self):
		if type(self.all_outcomes) in [list, tuple]:
			all_outcomes = sum(self.all_outcomes)
		else:
			all_outcomes = self.all_outcomes
		return round(round(self.fav_outcomes / all_outcomes, 2) * 100, 2)

	@property
	def latex(self):
		prefix = f"{"\t" * self.tabs}P({text(self.label)}) = "
		if type(self.all_outcomes) in [list, tuple]:
			mid = f"{frac(self.fav_outcomes, " + ".join(list(map(str, self.all_outcomes))))} = {frac(self.fav_outcomes, round(sum(self.all_outcomes), 2))}"
			suffix = f" = {round(self.fav_outcomes / sum(self.all_outcomes), 2)} = {self.result}\\% {new_line()}"
		else:
			mid = frac(self.fav_outcomes, self.all_outcomes)
			suffix = f" = {round(self.fav_outcomes / self.all_outcomes, 2)} = {self.result}\\% {new_line()}"
		self.output = f"{prefix}{mid}{suffix}"

		return super(ProbabilityEquation, self).latex
