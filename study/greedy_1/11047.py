import sys
sys.stdin = open('11047.txt')

N, K = map(int, input().split())
money = []
for _ in range(N):
    money.append(int(input()))

result = 0
for i in range(len(money)-1, -1, -1):
    if money[i] > K:
        continue
    if K == 0:
        break
    result += K // money[i]
    K = K % money[i]
print(result)