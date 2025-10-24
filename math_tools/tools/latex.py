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
