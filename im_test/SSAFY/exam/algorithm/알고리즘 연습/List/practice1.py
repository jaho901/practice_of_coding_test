import sys
sys.stdin = open('practice1.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    number = list(map(int, input().split()))
    # print(number)

    # 최종 결과값
    result = 0

    # 전체 리스트 순회
    for i in range(N):
        # i 번째 최대 낙차 값
        max_height = len(number) - (i + 1)

        # i 다음 행부터 박스 끝까지 반복
        for j in range(i+1, len(number)):
            # i보다 j가 더 큰 경우 최대 낙차값 -1
            if number[i] <= number[j]:
                max_height -= 1
            
        # 최종 최대 낙차값 도출
        if result <= max_height:
            result = max_height
    
    print('#{} {}'.format(tc, result))

