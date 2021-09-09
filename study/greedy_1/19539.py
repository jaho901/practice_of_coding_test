import sys
sys.stdin = open('19539.txt')

N = int(input())
trees = list(map(int, input().split()))
length = N
total = sum(trees)
turn = total // 3
if total % 3 != 0:
    print('NO')

else:
    for i in trees:
        turn -= (i//2)
    if turn > 0:
        print('NO')
    else:
        print('YES')
