import sys
sys.stdin = open('4466.txt')

# 재귀문제!!!
# def recur(cur=0, total=0, cnt=0):
#     global ans
#
#     if cnt == K:
#         ans = max(ans, total)
#         return
#
#     if cur == N:
#         return
#
#     recur(cur + 1, total + data[cur], cnt + 1)
#     recur(cur + 1, total, cnt)


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    data = list(map(int, input().split()))
    # 최댓값 K개 더하기!!
    data = sorted(data, reverse = True)
    # ans = 0
    # recur(0, 0, 0)
    print('#{} {}'.format(tc, sum(data[:K])))
        

