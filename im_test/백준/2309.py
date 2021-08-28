import sys
sys.stdin = open('2309.txt')

# 합이 100이 되었을 때 나오는 결과 생성
def recur(cur=0, total=0, cnt=0):
    global ans

    # 종료 조건 = 합이 100이면서 일곱명의 난쟁이를 선택한 경우
    if total == 100 and cnt == 7:
        # 글로벌 ans에 result를 저장해준다.
        # 얕은 복사법 사용!! 왜냐 -> result가 바뀔때마다 ans또한 바껴지기 때문!!
        ans = result[:]
        return

    if cur == 9:
        return

    # 빽트래킹!!! 이미 합이 100을 넘은 경우 & 난쟁이 명수가 7을 넘은 경우 return!!!
    if total > 100:
        return

    if cnt > 7:
        return

    result.append(data[cur])
    recur(cur + 1, total + data[cur], cnt + 1)
    result.pop()
    recur(cur + 1, total, cnt)


# 아홉 난쟁이의 키를 담을 리스트
data = []
for _ in range(9):
    data.append(int(input()))

data = sorted(data)
result = []
ans = []

recur(0, 0, 0)
for i in ans:
    print(i)
    
    
    
'''
# 신의 코드 # 투 포인터 => 숙지는 해두자! 

arr = [int(input()) for i in range(9)]
arr.sort()

s = 0
e = len(arr) - 1
tot = sum(arr)
ts, te = 0, 0

while s <= e:
    if tot - arr[s] - arr[e] == 100:
        ts = s
        te = e
        break

    elif tot - arr[s] - arr[e] > 100:
        s += 1

    else:
        e -= 1

for i in range(len(arr)):
    if i != ts and i != te:
        print(arr[i])
'''    

