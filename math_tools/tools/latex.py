def enclosed_brace(str):
	return f"{{{str}}}"


def frac(numerator, denominator):
	return f"\\frac{enclosed_brace(numerator)}{enclosed_brace(denominator)}"


def text(str):
	return f"\\text{enclosed_brace(str)}"
