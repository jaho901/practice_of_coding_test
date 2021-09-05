key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

# 90도씩 회전시키는 함수
def turn(arr):
    data = []
    for ze in zip(*arr):
        data.append(list(ze[::-1]))
    return data


## 자물쇠와 열쇠
def solution(key, lock):
    M, N = len(key), len(lock)
    # 키가 돌아다닐수있는 모든 영역을 -1로 잡고 lock에 상하좌우로 추가하였다.
    for i in range(N):
        lock[i] = [-1] * (M - 1) + lock[i] + [-1] * (M - 1)
    lock = [[-1] * (N + 2 * (M - 1)) for _ in range(M - 1)] + lock + [[-1] * (N + 2 * (M - 1)) for _ in range(M - 1)]
    result = False
    # 총 90도, 180도, 270도, 360도를 돌기때문에 4번 반복을 시켰고,
    for _ in range(4):
        # 일단 회전시키고 보자
        key = turn(key)
        # 키가 돌아다닐수 있는 영역이 열과 행으로 각각 (M-1) + N 씩 이동 가능
        for i in range(0, (M - 1) + N):
            for j in range(0, (M - 1) + N):
                total = 0
                # key가 1이면서 lock이 0인 경우 그 인덱스를 담을 리스트
                index = []
                # key도 1이고 lock도 1인 경우 맞물리니 불가능합 그 때의 인덱스를 담을 리스트
                index_2 = []
                # 모든 키의 행과 열을 반복하자
                for k in range(M):
                    for l in range(M):
                        # key와 lock이 딱 맞는 경우
                        if lock[i + k][j + l] == 0 and key[k][l] == 1:
                            lock[i + k][j + l] = 1
                            row = i + k
                            col = j + l
                            index.append([row, col])
                        # 홈이 맞물릴 경우 ( 그냥 break시키면 될거같은데 코드가 또 고장날까봐 걍 돌림 )
                        elif lock[i+k][j+l] == 1 and key[k][l] == 1:
                            lock[i+k][j+l] = 2
                            row = i + k
                            col = j + l
                            index_2.append([row, col])
                # lock이 존재하는 부분만 반복문돌리면서 1인 값을 구하고
                for x in range(M-1, N + M-1):
                    total += lock[x].count(1)
                # 그 total이 자물쇠 영역의 넓이와 동일한 경우 result를 True로 바꾸고 멈춘다.
                if total == N * N:
                    result = True
                    break
                # 아닐경우 다시 원상태로 돌린다! (1 or 2로 바꾼 부분을 다시 0 or 1로 변경)
                else:
                    for idx in range(len(index)):
                        lock[index[idx][0]][index[idx][1]] = 0
                    for idx2 in range(len(index_2)):
                        lock[index_2[idx2][0]][index_2[idx2][1]] = 1
            if result:
                break
        if result:
            break
    return result


print(solution(key, lock))

