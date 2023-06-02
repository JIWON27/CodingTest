n, k = map(int, input().split())
price = []
cnt = 0
for i in range(0,n):
    price.append(int(input()))
price.sort(reverse=True)
for coin in price:
    if k // coin != 0:
        cnt += k // coin
        k = k % coin
print(cnt)
        


