import sys
sys.stdin = open('practice2.txt')

T = int(input())
for tc in range(1, T+1):
    string = input()
 
    # triplet이든 run이든 값을 1씩 증가시킴
    idx = 0
    # 모든 한 자리 수가 들어가는 리스트
    result = [0] * 10
    # 주어진 string중에서 존재하는위치에 1씩 추가
    for i in range(0, len(string)):
        result[int(string[i])] += 1

    # triplet인지 확인
    for i in range(len(result)):
        # 3보다 큰 수일때
        if result[i] >= 3:
            # 예를 들어 4나 5일 수도 있으니깐 몫만 추가
            idx += result[i] // 3
            # 그 값에서 3 or 6을 뺀 나머지를 그 자리에 저장
            result[i] -= result[i]//3 * 3

    # run인지 확인
    for i in range(0, len(result)-2):
        # 3자리가 연속으로 같은 경우
        if result[i] == result[i+1] == result[i+2]:
            # 그 자리의 값을 추가
            idx += result[i]
            # 1234가 다 존재할 때 i=1인 경우 2와 3일때 0을 해줘야지 중복안됨
            result[i+1] = 0
            result[i+2] = 0

    print(idx)


    