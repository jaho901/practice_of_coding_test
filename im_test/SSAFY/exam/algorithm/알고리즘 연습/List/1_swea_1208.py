import sys
sys.stdin = open('1_swea_1208.txt')

def search(data):
    max_V = [data[0], 0]
    min_V = [data[0], 0]
    # 최댓값과 최소값의 위치와 해당하는 값 추출하는 함수 생성
    for i in range(len(data)):
        if data[i] > max_V[0]:
            max_V[0], max_V[1] = data[i], i
        if data[i] < min_V[0]:
            min_V[0], min_V[1] = data[i], i

    return max_V, min_V

for tc in range(1, 11):
    n = int(input())
    data = list(map(int, input().split()))

    max_V, min_V = search(data)
    # 총 상자를 다 이동시키면서 최댓값과 최솟값의 차이가 1이상인 경우
    while n and abs(max_V[0] - min_V[0]) > 1:
        # 최댓값에 존재하는 상자를 최솟값의 위치로 이동
        data[max_V[1]] -= 1
        data[min_V[1]] += 1
        n -= 1
        max_V, min_V = search(data)

    print('#{} {}'.format(tc, max_V[0] - min_V[0]))
