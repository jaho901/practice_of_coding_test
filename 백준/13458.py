import sys
sys.stdin = open('13458.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    B, C = map(int, input().split())

    result = 0
    for i in range(len(A)):
        if A[i] - B > 0:
            A[i] -= B
        else:
            A[i] = 0
    result += len(A)

    for i in range(len(A)):
        if A[i] > 0:
            if A[i] % C == 0:
                result += A[i]//C
            else:
                result += (A[i] // C) + 1

    print(result)