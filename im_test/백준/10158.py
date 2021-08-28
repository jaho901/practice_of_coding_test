N, M = map(int, input().split())
x, y = map(int, input().split())
cnt = 8

def result(x, N, cnt):
    if cnt > N*2:
        cnt = cnt % (N*2)
    
    while cnt == 0:
        while x == N:
            x += 1
            cnt -= 1
            if cnt == 0:
                break

        while x == 0:
            x -= 1
            cnt -= 1

    
    

    

        