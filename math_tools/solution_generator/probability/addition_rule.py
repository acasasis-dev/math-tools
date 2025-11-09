from math_tools.common.equation import Equation


class AdditionRule(Equation):
	def __init__(self, prob_a, prob_b, prob_a_n_b, label, tabs, environment):
		super().__init__(label, tabs, environment)
		self.prob_a = prob_a
		self.prob_b = prob_b
		self.prob_a_n_b = prob_a_n_b

	def result(self):
		pass

	def latex(self):
		pass
