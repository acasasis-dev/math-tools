from math_tools.common.equation import Equation


class ProbabilityEquation(Equation):
	def __init__(self, fav_outcomes, all_outcomes, given_outcomes=None, environment=True):
		self.fav_outcomes = fav_outcomes
		self.all_outcomes = all_outcomes
		self.given_outcomes = given_outcomes
		self.environment = environment
