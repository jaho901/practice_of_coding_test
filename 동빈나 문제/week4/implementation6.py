n = 5
build_frame = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]
# build_frame = [[0,0,0,1], [2,0,0,1], [4,0,0,1], [0,1,1,1], [1,1,1,1], [2,1,1,1], [3,1,1,1], [2,0,0,0], [1,1,1,0], [2,2,0,1]]
arr = [[0]*(n+1) for _ in range(n+1)]
for i in build_frame:
    if i[3] == 1:
        if i[2] == 0:
            if i[1] == 0 or arr[i[1]-1][i[0]] == 1 or arr[i[1]][i[0]-1] == 2:
                arr[i[1]][i[0]] = 1
            else:
                continue
        elif i[2] == 1:
            if arr[i[1]-1][i[0]] == 1 or arr[i[1]][i[0]-1] == 2:
                arr[i[1]][i[0]] = 2
    elif i[3] == 0:
        if i[2] == 0:
            if arr[i[1]][i[0]+1] == 2:
                continue
            elif arr[i[1]-1][i[0]+1] == 1:
                continue
            else:
                arr[i[1]][i[0]] = 0
        elif i[2] == 1:
            if arr[i[1]+1][i[0]-1] == 2 and arr[i[1]+1][i[0]] == 2:
                arr[i[1]][i[0]] = 0
            else:
                continue
    

# def solution(n, build_frame):
    

# solution(n, build_frame)
for i in arr:
    print(*i)



    