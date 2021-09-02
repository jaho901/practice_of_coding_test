# 큰 수의 법칙

# N, M, K를 공백으로 구분하여 입력받기
# N : 숫자 길이, M : 총 더할 숫자의 길이, K : 연속으로 나올 수의 길이
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

# 입력받은 수 정렬하기
data.sort()
maximum = data[-1]
second = data[-2]


result = 0

'''
while True:
    # 가장 큰 수를 K번 더하기
    for i in range(k):
        if m == 0:
            break
        result += result
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)
'''

count = int(m // (k+1)) * k
count += m % (k + 1)

result = 0
result += (count) * maximum
result += (m - count) * second

print(result)

