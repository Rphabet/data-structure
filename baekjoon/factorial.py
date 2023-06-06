# factorial

x = int(input())


def factorial(a: int) -> int:
    if a == 0:  # base case
        return 1
    else:
        return a * factorial(a - 1)


print(factorial(x))