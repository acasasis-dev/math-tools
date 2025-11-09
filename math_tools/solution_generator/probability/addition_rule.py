from math_tools.common.equation import Equation


class AdditionRule(Equation):
	def __init__(self, prob_a, prob_b, prob_a_n_b, all_outcomes, label, tabs, environment):
		super().__init__(label, tabs, environment)
		self.prob_a = prob_a
		self.prob_b = prob_b
		self.prob_a_n_b = prob_a_n_b
		self.all_outcomes = all_outcomes

	def result(self):
		return round(((self.prob_a + self.prob_b) - self.prob_a_n_b) / self.all_outcomes, 2)

	def latex(self):
		pass
