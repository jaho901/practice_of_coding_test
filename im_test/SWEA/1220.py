import sys
sys.stdin = open('1220.txt')

T = 10
for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0

    # N극을 중심으로 가장 밑에값은 항상 2가 존재하기때문에 N-1개를 확인한다!
    for i in range(N-1):
        for j in range(N):
            # 만약에 해당하는 값이 1일 경우
            if data[i][j] == 1:
                # 그 다음값이 2이면 바로 cnt에 1을 추가해준다.
                if data[i+1][j] == 2:
                    cnt += 1
                # 만약에 그 다음값이 0이면 그 값과 1의 위치를 바꿔준다.
                elif data[i+1][j] == 0:
                    data[i+1][j] = data[i][j]
    
    # 어차피 1 ~ 2 ~ 2 인 경우 어차피 2와 2 사이에 1이 존재하지않으므로 넘어가게된다!

    print('#{} {}'.format(tc, cnt))


        



