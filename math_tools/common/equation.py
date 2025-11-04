from abc import ABC, abstractmethod


class Equation(ABC):
	@property
	@abstractmethod
	def result(self):
		pass

	@property
	@abstractmethod
	def latex(self):
		if self.environment:
			self.output = (
				"\\begin{gather*} \n"
				f"{self.output}"
				"\\end{gather*}"
			)

		return self.output
