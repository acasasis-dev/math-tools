from abc import ABC, abstractmethod


class Equation(ABC):
	@property
	@abstractmethod
	def result(self):
		pass

	@property
	@abstractmethod
	def latex(self):
		pass
