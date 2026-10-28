import sys


def ask(*args):
    """Print a query line, flush, and return the judge's reply line (stripped)."""
    print(*args, flush=True)
    return sys.stdin.readline().strip()
