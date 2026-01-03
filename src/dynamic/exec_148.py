"""Dangerous eval/exec usage."""

def calculate(expression):
    """DANGEROUS: eval with user input."""
    return eval(expression)

def execute(code):
    """DANGEROUS: exec with user input."""
    exec(code)
