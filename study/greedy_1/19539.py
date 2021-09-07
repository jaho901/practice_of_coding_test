import sys
sys.stdin = open('19539.txt')

N = int(input())
trees = list(map(int, input().split()))
print(trees)
while True:
    maximum = max(trees)
    minimum = min(trees)
    max_idx = trees.index(maximum)
    min_idx = trees.index(minimum)
    if minimum*2 > maximum:
        n = maximum // 2
        trees[max_idx] = trees[max_idx] - 2*n
        trees[min_idx] = trees[min_idx] - n
    else:
        n = minimum
        trees[max_idx] = trees[max_idx] - 2*n
        trees[min_idx] = trees[min_idx] - n
    
    if trees.count(0) + trees.count(1) + trees.count(2) == N:
        if trees.count(0) == N:
            print('YES')
            break
        else:
            print('NO')
            break
