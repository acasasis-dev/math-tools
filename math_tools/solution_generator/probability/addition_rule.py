from math_tools.common.equation import Equation


class AdditionRule(Equation):
	def __init__(self, prob_a, prob_b, prob_a_n_b, all_outcomes, label, tabs, environment):
		super().__init__(label, tabs, environment)
		self.prob_a = prob_a
		self.prob_b = prob_b
		self.prob_a_n_b = prob_a_n_b
		self.all_outcomes = all_outcomes

		if type(label) in [list, tuple]:
			if len(label) != 2:
				raise Exception("label must be a list/tuple with a length of 2")
		else:
			raise Exception("label must be a list/tuple")
		
	def result(self):
		return round(((self.prob_a + self.prob_b) - self.prob_a_n_b) / self.all_outcomes, 2)

	def latex(self):
		output = f"P()"
