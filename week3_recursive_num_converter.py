def decimal_converter(n, base):
    num_string = "0123456789ABCDEF"
    q, r = divmod(n, base)

    if q == 0:
        return num_string[r]
    else:
        return decimal_converter(q, base) + num_string[r]


if __name__ == '__main__':
    num = int(input('10진수 입력 --> '))

    print('2진수 : ', decimal_converter(num, 2))
    print('8진수 : ', decimal_converter(num, 8))
    print('16진수 : ', decimal_converter(num, 16))
