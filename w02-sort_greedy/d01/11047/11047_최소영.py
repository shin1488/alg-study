import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coin = int(input())
    coins.append(coin)

coins.sort(reverse=True)
count = 0

for coin in coins:
    if coin <= k:
        count += k // coin
        k = k % coin

print(count)