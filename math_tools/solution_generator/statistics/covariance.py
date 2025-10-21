def covariance(x, y, labels=None):
	_labels = ("x", "y")
	if len(x) != len(y):
		raise Exception(f"length of x must be the same as y. {len(x)} != {len(y)}")
	
	if labels:
		if len(labels) != 2:
			raise Exception(f"length of labels must exactly be 2")
	else:
		_labels = labels

	# TODO: Implement covariance computation and generate latex here
	