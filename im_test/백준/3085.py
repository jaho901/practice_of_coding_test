import sys
sys.stdin = open('3085.txt')

N = int(input())
data = [list(input()) for _ in range(N)]


def check():
    ans = 1

    # 가로 체크
    for i in range(N):
        cnt = 1
        x = data[i][0]
        for j in range(1, N):
            if x == data[i][j]:
                cnt += 1
            else:
                cnt = 1
                x = data[i][j]
            if ans < cnt:
                ans = cnt
    # 세로 체크
    for i in range(N):
        cnt = 1
        y = data[0][i]
        for j in range(1, N):
            if y == data[j][i]:
                cnt += 1
            else:
                cnt = 1
                y = data[j][i]
            if ans < cnt:
                ans = cnt
    return ans


# 이제 서로 다른 2개씩 바꿔가면서 체크해보자
result = 0
for i in range(N):
    for j in range(N):
        # i가 N-1보다 작다는말은 가로끝가지 갔다는 의미
        if j < N-1:
            if data[i][j] != data[i][j+1]:
                data[i][j], data[i][j+1] = data[i][j+1], data[i][j]
                ans = check()
                if result < ans:
                    result = ans
                # 원위치 시키기
                data[i][j], data[i][j+1] = data[i][j+1], data[i][j]
        # j가 N-1보다 작다는말은 세로끝가지 갔다는 의미
        if i < N-1:
            if data[i][j] != data[i+1][j]:
                data[i][j], data[i+1][j] = data[i+1][j], data[i][j]
                ans = check()
                if result < ans:
                    result = ans
                # 원위치 시키기
                data[i][j], data[i+1][j] = data[i+1][j], data[i][j]
print(result)