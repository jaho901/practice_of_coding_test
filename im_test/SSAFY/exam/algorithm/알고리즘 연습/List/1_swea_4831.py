import sys
sys.stdin = open('1_swea_4831.txt')

T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    station = list(map(int, input().split()))

    # 현재 내 위치
    now = K
    # 충전 횟수
    count = 0
    # 충전한 직전 위치
    charge = 0

    while now < N:
        # 이동했을 때 충전소에 있으면
        if now in station:
            # 충전횟수 1늘리고 현재위치를 충전소위치로 변경
            # 충전한 직전위치도 현재 위치로 변경
            count += 1
            charge = now
            now += K
        # 충전소가 없으면 현재위치를 1씩 빼면서 충전소 찾기
        else:
            now -= 1

        # 충전소를 못찾았으면 == 직전 충전한 위치까지 도달하면
        if charge == now:
            # 충전을 더는 못하니깐 0을 반환하며 멈춤
            count = 0
            break

    print(count)

