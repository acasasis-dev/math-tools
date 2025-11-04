from .lib import ProbabilityEquation


class SimpleProbability(ProbabilityEquation):
	def __init__(self, fav_outcomes, all_outcomes, label, tabs=1):
		super().__init__(fav_outcomes, all_outcomes, label=label, tabs=tabs)

	@property
	def result(self):
		return round(self.fav_outcomes / self.all_outcomes, 2)

	@property
	def latex(self):
		return super(ProbabilityEquation, self).latex
