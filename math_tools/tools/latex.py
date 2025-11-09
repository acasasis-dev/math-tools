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
	return f"\\bar{enclosed_brace(text(label))}"


def mu(label):
	return f"\\mu_{text(label)}" if label else f"\\mu"


def x_bar(label):
	return f"{bar("x")}_{text(label)}" if label else f"{bar("x")}"


def get_sd_symbol(population, label, variance=False):
	prefix = f"{sigma() if population == "full" else f"s"}{"^2" if variance else ""}"
	if label and type(label) in [list, tuple]:
		x, y = label
		if len(x) + len(y) == 2:
			return f"{prefix}{"_" + text(f"{x}{y}")} = "
		else:
			return f"{prefix}{"_" + text(f"[{x}, {y}]")}  = "
	elif label:
		return f"{prefix}{"_" + text(label)} = "
	else:
		return f"{prefix} = "


def get_mean_symbol(population, label=None):
	prefix = mu(label) if population == "full" else x_bar(label)
	return f"{prefix} = "


def sqrt(num):
	return f"\\sqrt{enclosed_brace(num)}"


cap = "\\cap"
cup = "\\cup"
percent = "\%"
