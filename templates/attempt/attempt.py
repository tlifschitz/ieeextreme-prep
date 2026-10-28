# Your attempt. Copy this file into the problem folder as attempt.py, then check it with
#   python3 scripts/verify.py "<problem>"
import sys

input = sys.stdin.readline  # keeps the trailing "\n": use .split() or .rstrip("\n")
# Big inputs: read every token at once instead (not for interactive problems):
#   data = sys.stdin.buffer.read().split()
if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)  # Python 3.11+ refuses to print ints over 4300 digits


def solve():
    pass  # read the input with input() and print the answer


def main():
    solve()


main()

# Deep recursion: replace main() above with
#   import threading
#   sys.setrecursionlimit(1 << 25)
#   threading.stack_size(1 << 27)
#   threading.Thread(target=main).start()
