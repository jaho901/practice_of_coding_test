import sys
sys.stdin = open('2527.txt')

# 이건 수학문제! 풀지말자!
# 밑에꺼는 퍼왔음...ㅎㅎ

for i in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    # //1번 과정 
    xl = max(x1, x2)
    xr = min(p1, p2)
    yb = max(y1, y2)
    yt = min(q1, q2)
    
    #//2번 과정 
    xdiff = xr - xl
    ydiff = yt - yb 
    
    #//3번 과정 
    if xdiff > 0 and ydiff > 0: 
        print('a') 
    elif xdiff < 0 or ydiff < 0: 
        print('d') 
    elif xdiff == 0 and ydiff == 0: 
        print('c') 
    else: print('b')




    
