# 공 넣기

def insert_ball(init_list: list, input_list: list) -> None:
    """

    :param size: size of the array
    :param init_list: initial list of size n
    :param input_list: input_list
    :return:
    """
    i, j = input_list[0], input_list[1]
    for idx in range(i, j+1):
        init_list[idx-1] = input_list[-1]


if __name__ == '__main__':
    n, m = map(int, input().split())  # 바구니 & 공 개수 N, 공을 넣는 횟수
    result = [0] * n
    for _ in range(m):
        num_list = list(map(int, input().split()))  # 시작 바구니 번호, 끝 바구니 번호, 넣을 공 번호
        # pass # 함수가 들어가면 됨
        insert_ball(result, num_list)
    for num in result:
        print(num, end=' ')