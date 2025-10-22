from statistics import mean as m

def enclosed_brace(str):
	return f"{{{str}}}"


def frac(numerator, denominator):
	return f"\\frac{enclosed_brace(numerator)}{enclosed_brace(denominator)}"


def text(str):
	return f"\\text{enclosed_brace(str)}"


def sigma(str=None):
	return f"\\sigma_{enclosed_brace(str)}"


def new_line():
	return "\\\\ \n"


def bar(label):
	return f"\\bar{enclosed_brace("x")}_{text(label)}"


def mean(data):
	points_mean = m(data)
	points_stringified = " + ".join(list(map(str, data)))
	points_len = len(data)
	return f"{frac(points_stringified, points_len)} = {frac(sum(data), points_len)} = {points_mean}", points_mean
