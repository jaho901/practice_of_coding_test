import sys
sys.stdin = open('18310.txt')

N = int(input())
data = list(map(int, input().split()))
data.sort()

def dist(c):
    total = 0
    for i in range(len(data)):
        total += abs(data[c] - data[i])
    return total

if len(data)%2 == 1:
    print(data[len(data)//2])
else:
    a, b = len(data)//2-1, len(data)//2
    if dist(a) >= dist(b):
        print(data[a])
    else:
        print(data[b])