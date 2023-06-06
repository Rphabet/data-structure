# fibonacci using iteration

x = int(input())


def fib(a: int) -> int:
    if a < 2:
        return a

    last = 0
    current = 1

    for i in range(2, a + 1):
        last, current = current, last + current

    return current

print(fib(x))