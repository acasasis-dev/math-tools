from .lib import StatisticsEquation


class GroupedDataMean(StatisticsEquation):
	def __init__(self, data, label=("x", "y"), population="full", tabs=1, environment=True):
		super().__init__(data, label, population, tabs, environment)
		if self.data and len(self.data) != 2:
			raise Exception(f"length of data must exactly be 2")
		elif self.data:
			self.x, self.y = data
		else:
			self.x, self.y = [[], []]

		if len(self.label) != 2:
			raise Exception(f"length of labels must exactly be 2")
			 
		self.x_label, self.y_label = self.label
		self.label = f"{self.x_label}{self.y_label}" if len(self.x_label) + len(self.y_label) == 2 else f"[{self.x_label}, {self.y_label}]"
		self.denominator = sum(self.y) - (1 if population == "sample" else 0)
		self.midpoints = [start + ((end - start) / 2) for start, end in self.x]
		self.numerator = round(sum([num * self.midpoints[i] for i, num in enumerate(self.y)]), 2)

	@property
	def result(self):
		pass

	@property
	def latex(self):
		pass
