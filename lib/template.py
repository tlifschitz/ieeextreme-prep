import sys

input = sys.stdin.readline  # keeps the trailing "\n": use .split() or .rstrip("\n")
# Big inputs: read every token at once instead (not for interactive tasks):
#   data = sys.stdin.buffer.read().split(); p = 0  -> int(data[p]); p += 1
if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)  # Python 3.11+ refuses to print ints over 4300 digits


def ints():
    return list(map(int, input().split()))


def solve():
    n = int(input())
    a = ints()
    return " ".join(map(str, sorted(a)))


def main():
    out = []
    T = 1
    # T = int(input())
    for _ in range(T):
        out.append(solve())
    sys.stdout.write("\n".join(map(str, out)) + "\n")


main()

# Deep recursion: replace main() above with
#   import threading
#   sys.setrecursionlimit(1 << 25)
#   threading.stack_size(1 << 27)
#   threading.Thread(target=main).start()
