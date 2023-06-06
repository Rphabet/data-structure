# 버블 정렬 알고리즘 구현 (알고리즘 개선 2)
# 정렬된 원소를 제외한 나머지만 비교/교환 하도록 스캔 범위 제한

from typing import MutableSequence


def bubble_sort(a: MutableSequence) -> None:
    """버블 정렬 (스캔 범위 제한)"""
    n = len(a)
    k = 0
    while k < n - 1:
        last = n - 1
        for j in range(n-1, k, -1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                last = j

        k = last  # k를 last로 설정하여 스캔 범위를 줄여줌


if __name__ == '__main__':
    print('버블 정렬을 수행...')
    num = int(input('원소 수를 입력하세요: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    bubble_sort(x)  # 배열 x를 버블 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')