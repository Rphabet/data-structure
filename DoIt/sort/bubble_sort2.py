# 버블 정렬 알고리즘 (알고리즘 개선 버전)
# 교환 횟수에 따라 중단 방식을 적용

from typing import MutableSequence


def bubble_sort(a: MutableSequence) -> None:
    """버블 정렬 (교환 횟수에 따른 중단)"""
    n = len(a)
    for i in range(n-1):
        exchng = 0  # 패스에서 교환 횟수
        for j in range(n-1, i, -1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                exchng += 1
        if exchng == 0:
            break


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