# 피보나치 수열 recursive version

n = int(input())


def fib(a: int) -> int:
    if a == 0:
        return 0
    elif a == 1:
        return 1
    else:
        return fib(a - 1) + fib(a - 2)


print(fib(n))