from .lib import ProbabilityEquation

from math_tools.tools.latex import text, frac, new_line


class SimpleProbability(ProbabilityEquation):
	def __init__(self, fav_outcomes, all_outcomes, label, tabs=1):
		super().__init__(fav_outcomes, all_outcomes, label=label, tabs=tabs)

	@property
	def result(self):
		return round(self.fav_outcomes / self.all_outcomes, 2) * 100

	@property
	def latex(self):
		prefix = f"{"\t" * self.tabs}P({text(self.label)}) = "
		self.output = f"{prefix}{frac(self.fav_outcomes, self.all_outcomes)} = {round(self.fav_outcomes / self.all_outcomes, 2)} = {self.result}\\% {new_line()}"

		return super(ProbabilityEquation, self).latex
