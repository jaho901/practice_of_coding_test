def rich(N, M):
    share = N // M
    rest = N % M
    result = [share, rest]
    for i in result:
        print(i)

n, m = map(int, input().split())
rich(n, m)