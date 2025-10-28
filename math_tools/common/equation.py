from abc import ABC, abstractmethod


class Equation(ABC):
	@property
	@abstractmethod
	def latex(self):
		pass
