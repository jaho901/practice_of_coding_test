import sys
sys.stdin = open('2563.txt')

arr = [[0]*100 for _ in range(100)]

N = int(input())
# 총 N번의 input 좌표를 받을 것이다.
for _ in range(N):
    # 받은 input값을 x, y로 저장
    x, y = map(int, input().split())
    # 무조건 색종이의 크기는 너비, 높이가 10이므로
    # x부터 x+10까지, y부터 y+10까지 반복문 돌린다.
    for i in range(x, x+10):
        for j in range(y, y+10):
            # 이미 색종이가 존재하는 부분은 넘기고
            if arr[i][j] == 1:
                pass
            # 아니면 그 자리에 1을 채워넣는다.
            else:
                arr[i][j] += 1

result = 0
# 1이 존재하는 모든 위치를 확인하고 result에 더해준다.
for k in range(len(arr)):
    for l in range(len(arr[0])):
          if arr[k][l] == 1:
              result += 1

print(result)