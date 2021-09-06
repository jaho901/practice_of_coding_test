import sys
sys.stdin = open('1461.txt')

def cal(data):
    result = []
    for i in range(0, len(data), K):
        result.append(abs(data[i]))
    return result

N, K = map(int, input().split())
location = list(map(int, input().split()))
ne_lo = []
po_lo = []
for i in location:
    if i < 0:
        ne_lo.append(i)
    else:
        po_lo.append(i)
ne_lo = sorted(ne_lo)
po_lo = sorted(po_lo, reverse=True)

total = []

total += cal(ne_lo)
total += cal(po_lo)
total = sorted(total)

ans = 0
ans += total.pop()
ans += sum(total)*2
print(ans)


