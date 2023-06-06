# n바이트

n = int(input())

if n <= 4:
    print('long int')
elif n % 4 == 0:
    print((n // 4) * 'long ' + 'int')
else:
    print((n//4 + 1) * 'long ' + 'int')
# if n % 4 != 0:
#     print((n//4) * 'long ' + 'int')
# else:
#     print((n//4 - 1) * 'long ' + 'int')
