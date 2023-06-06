# receipt

x = int(input()) # 총 금액
n = int(input()) # 물건의 종류

total = 0

for i in range(n):
    price, num = map(int, input().split())
    total += (price * num)
    # item_price_list.append(price)
    # item_num_list.append(num)

if total == x:
    print('Yes')
    # print(total)
    # print(x)
else:
    print('No')
    # print(total)
    # print(x)