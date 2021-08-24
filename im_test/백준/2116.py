import sys
sys.stdin = open('2116.txt')

N = int(input())

data = []
for _ in range(N):
    sub = list(input().split())
    dic = {
        int(sub[0]):int(sub[5]),
        int(sub[1]):int(sub[3]),
        int(sub[2]):int(sub[4]),
        int(sub[3]):int(sub[1]),
        int(sub[4]):int(sub[2]),
        int(sub[5]):int(sub[0])
    }
    data.append(dic)
print(data)
number = []
for i in range(1, 7):
    sub = [[data[0][i], i]]
    idx = i
    for j in range(1, N):
        n = [idx, data[j][idx]]
        idx = data[j][idx]
        sub.append(n)
    number.append(sub)
print
result = []

for i in number:
    total = 0
    for j in i:
        if 6 in j:
            if j == [5, 6] or j == [6, 5]:
                total += 4
            else:
                total += 5
        else:
            total += 6
    result.append(total)
print(max(result))

