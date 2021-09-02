# 1이 될때까지

n, k = map(int, input().split())
result = 0

# n = 25, k = 3

while n > 1:
    if n % k == 0:
        n = n / k
        result += 1
    else:
        n = n - 1
        result += 1


print(result)
