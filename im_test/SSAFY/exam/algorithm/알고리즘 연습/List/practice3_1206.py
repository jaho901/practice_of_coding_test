import sys
sys.stdin = open('practice3.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    # 최종 결과값
    result = 0

    # 범위에서 앞 뒤 2칸 제외
    for i in range(2, N-2):
        # 각 층간의 높이 차이 중, 가장 차이가 적은 값
        minimum = 246
        # 현재 위치를 기준으로 앞 뒤 2칸씩 봐야함으로 범위 5 지정
        for j in range(5):
            if j != 2:  # 현재 내 위치에서는 비교가 불가능!
                # 현재 내위치의 2칸 앞부터 차례대로 5번씩 계산
                if data[i] - data[i - 2 + j] < minimum:
                    minimum = data[i] - data[i - 2 + j] # 계속해서 갱신

        # 그 차이가 양수면 최종 결과값으로 저장
        if minimum > 0:
            result += minimum

    print(result)