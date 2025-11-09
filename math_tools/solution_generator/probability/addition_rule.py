from math_tools.common.equation import Equation

from math_tools.tools.latex import text, frac, new_line, cap, cup


class AdditionRule(Equation):
	def __init__(self, prob_a, prob_b, prob_a_n_b, all_outcomes, label=["A", "B"], tabs=1, environment=True):
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
		
		self.prob_a_label, self.prob_b_label = label
		
	@property
	def result(self):
		return round(((self.prob_a + self.prob_b) - self.prob_a_n_b) / self.all_outcomes, 2)

	@property
	def latex(self):
		prefix = "\t" * self.tabs
		prob_a_frac = frac(self.prob_a, self.all_outcomes)
		prob_b_frac = frac(self.prob_b, self.all_outcomes)
		prob_a_n_b_frac = frac(self.prob_a_n_b, self.all_outcomes)
		output = f"{prefix}P({text(self.prob_a_label)}) = {prob_a_frac} {new_line()}"
		output += f"{prefix}P({text(self.prob_b_label)}) = {prob_b_frac} {new_line()}"
		output += f"{prefix}P({text(self.prob_a_label)} {cap} {text(self.prob_b_label)}) = {prob_a_n_b_frac} {new_line()}"
		prefix = f"{prefix}P({text(self.prob_a_label)} {cup} {text(self.prob_b_label)}) = "
		output += f"{prefix}{prob_a_frac} + {prob_b_frac} - {prob_a_n_b_frac}"
		self.output = output

		return super().latex
