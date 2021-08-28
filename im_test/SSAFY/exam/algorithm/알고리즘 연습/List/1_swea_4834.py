import sys
sys.stdin = open('1_swea_4834.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card = list(map(int, input()))

    # 카드 수 카운트용 리스트 생성 (0 ~ 9)
    card_list = [0]*10

    # 카드 수 카운팅
    for i in card:
        card_list[i] += 1

    # 반복문 인덱스
    idx = 0
    # 제일 큰 카드의 위치
    max_idx = 0

    while idx != 10:    # 범위는 카드 리스트가 10개기 때문에
        # 크거나 같다로 표현하여 가장 뒤에 있는 값을 추출!
        if card_list[idx] >= card_list[max_idx]:
            max_idx = idx
        idx += 1
    print(max_idx, card_list[max_idx])