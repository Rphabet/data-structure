# Week 2: Recursive
# print starts


def count_down(n: int) -> None:
    if n == 0: # base case
        print('발사!!!')
    else:
        print(n)
        count_down(n-1)


def print_normal_stars(n: int) -> None:
    if n == 1: # base case
        print('*')
    else:
        print_normal_stars(n - 1)
        print('*' * (n))


def print_reverse_stars(n: int) -> None:
    if n > 0:
        print('*' * n)
        print_reverse_stars(n-1)


if __name__ == '__main__':
    # print_stars(5)
    # count_down(5)
    # print_normal_stars(5)
    print_reverse_stars(5)