import sys
sys.stdin = open('input.txt', encoding='UTF-8')

N = int(input())
result = 0
data = []
for i in range(N):
    data.append(list(map(int, input().split())))
data = sorted(data)
idx = [i[0] for i in data]
value = [i[1] for i in data]
n = 0
value1 = value[:]
max_1 = []
for i in range(len(value1)):
    maximum = max(value1)
    if value1[i] == maximum:
        max_1.append(i)
        value1[i] = 0
    else:
        value1[i] = 0
height = value[0]
maximum = max(value)
max_idx = value.index(maximum)
k = 0
print(data)

while k < N:
    if k < max_idx:
        if height < value[k + 1]:
            n += idx[k + 1] - idx[k]
            result += n * height
            height = value[k + 1]
            n = 0
        else:
            n += idx[k + 1] - idx[k]
        k += 1

    elif k == max_idx:
        result += value[max_idx]
        n = 0
        max_1.pop(0)
        k += 1

    else:
        if k == max_1[0]:
            n += idx[k] - idx[k-1]
            result += n * value[k]
            max_1.pop(0)
            n = 0
        else:
            n += idx[k] - idx[k-1]
        k += 1

print(result)

