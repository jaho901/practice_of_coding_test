import sys
sys.stdin = open('question20.txt')

N = int(input())
arr = [list(input().split()) for _ in range(N)]
exist = False

teacher = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'T':
            teacher.append([i, j])

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def check(x, y):
    real_x, real_y = x, y
    for k in range(4):
        x, y = real_x, real_y
        while True:
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] == 'S':
                    return False
                elif arr[nx][ny] == 'O':
                    exist = True
                    break
                else:
                    x, y = nx, ny
            else:
                break
    return True

def dfs(x, y, cnt):
    global result
    if cnt == 3:
        count = 0
        for z, w in teacher:
            if check(z, w):
                count += 1
            else:
                break
        if count == len(teacher):
            result = 'YES'
        return

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'X':
                arr[i][j] = 'O'
                dfs(i, j, cnt+1)
                arr[i][j] = 'X'

result = 'NO'
dfs(0, 0, 0)
print(result)