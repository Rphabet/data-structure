# def count_int(n: int, v: int, *num) -> None:
#     """
#
#     :param n: Total number n in num
#     :param v: number that is subject to find
#     :param num: variable length argument of numbers
#     :return: None
#     """
#     if n != len(num):
#         print('WRONG LENGTH')
#     else:
#         print(n, len(num))
#         count = 0
#         for i in num:
#             print(i)
#             if v == i:
#                 count += 1
#             else:
#                 continue
#
#         print(count)

def count_int(num: list, v: int) -> None:
    # count = 0
    # for i in num:
    #     if v == i:
    #         count += 1
    count = num.count(v)
    print(count)


if __name__ == '__main__':
    n = int(input())
    num = list(map(int, input().split()))
    v = int(input())
    count_int(num, v)