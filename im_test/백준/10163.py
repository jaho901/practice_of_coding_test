import sys
sys.stdin = open('10163.txt')

n = int(input())
arr = [[0] * 1001 for _ in range(1001)]
result = []
for i in range(n):
    lx, ly, w, h = map(int, input().split())
    # 반복되는 위치라도 뒤의 색종이 값을 덮어씌어주면서 반복문 실행
    for j in range(ly, ly+h):
        for k in range(lx, lx+w):
            arr[j][k] = i + 1

    # arr는 1001인데 존재하는 위치에서만 돌리기 위해 계속해서 추가해준다.
    result.append(ly)
    result.append(h)
    
for y in range(n):
    sub = 0
    # 그러면 여기서 0, 1001까지 계속 돌릴 필요가 없이 범위를 아래와 같이 지정해주면
    # 시간이 매우 단축됨을 알 수 있다.
    for x in range(result[y*2], result[y*2] + result[y*2+1]):
        # (y+1)이 뭐냐면 1, 2, 3, 4 ... 의 값들의 개수를 찾는 것이다!!
        sub += arr[x].count(y+1)
    print(sub)









