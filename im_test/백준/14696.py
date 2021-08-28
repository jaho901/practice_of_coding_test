import sys
sys.stdin = open('14696.txt')

N = int(input())
# 총 게임 횟수 N번을 실행한다.
for i in range(N):
    first = list(map(int, input().split()))
    second = list(map(int, input().split()))
    # A와 B가 내는 딱지의 그림의 총 수는 필요가 없기 때문에 삭제한다.
    first = first[1:]
    second = second[1:]
    # 별의 개수가 다르다면
    if first.count(4) != second.count(4):
        # 별의 개수가 큰 쪽을 반환
        if first.count(4) > second.count(4):
            print('A')
        else:
            print('B')
    # 별의 개수가 같다면
    else:
        # 동그라미의 개수가 다르다면
        if first.count(3) != second.count(3):
            # 동그라미 개수가 큰 쪽을 반환
            if first.count(3) > second.count(3):
                print('A')
            else:
                print('B')
        # 동그라미 개수가 같다면
        else:
            # 네모의 개수가 다르다면
            if first.count(2) != second.count(2):
                # 네모 개수가 큰 쪽을 반환
                if first.count(2) > second.count(2):
                    print('A')
                else:
                    print('B')
            # 네모 개수가 같다면
            else:
                # 세모 개수가 다르다면
                if first.count(1) != second.count(1):
                    # 세모 개수가 큰 족을 반환
                    if first.count(1) > second.count(1):
                        print('A')
                    else:
                        print('B')
                # 세모 개수가 같다면 D를 반환
                else:
                    print('D')