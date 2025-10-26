def enclosed_brace(str):
	return f"{{{str}}}"


def frac(numerator, denominator):
	return f"\\frac{enclosed_brace(numerator)}{enclosed_brace(denominator)}"


def text(str):
	return f"\\text{enclosed_brace(str)}"


def sigma(label=None):
	return f"\\sigma_{enclosed_brace(text(str))}" if label else f"\\sigma"


def new_line():
	return "\\\\ \n"


def bar(label):
	return f"\\bar{enclosed_brace(label)}"


def mu(label):
	return f"\\mu_{text(label)}" if label else f"\\mu"


def x_bar(label):
	return f"{bar(enclosed_brace("x"))}_{text(label)}" if label else f"{bar(enclosed_brace("x"))}"


def get_sd_symbol(population, label, variance=False):
	prefix = f"{sigma() if population == "full" else f"s"}{"^2" if variance else ""}"
	return f"{prefix}{"_" + text(label) if label else ""} = "
