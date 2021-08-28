import sys
sys.stdin = open('2559.txt')

data = [list(map(int, input().split())) for _ in range(5)]

arr = []
for _ in range(5):
    a = list(map(int, input().split()))
    arr += a

result = 0
result1 = [0]*5
result2 = [0]*5
result3 = [0]
result4 = [0]

for k in range(len(arr)):
    a = True
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == arr[k]:
                result1[i] += 1
                result2[j] += 1
                if i == j:
                    result3[0] += 1
                if i == 5-j-1:
                    result4[0] += 1
                a = False
                break
        if not a:
            break
    if result1.count(5) + result2.count(5) + result3.count(5) + result4.count(5) >= 3:
        result = k
        break
print(result+1)


