from .lib import ProbabilityEquation


class SimpleProbability(ProbabilityEquation):
	def __init__(self, fav_outcomes, all_outcomes):
		super().__init__(fav_outcomes, all_outcomes)

	@property
	def result(self):
		pass

	@property
	def latex(self):
		pass
