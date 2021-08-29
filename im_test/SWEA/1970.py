import sys
sys.stdin = open('1970.txt')

T = int(input())
for tc in range(1, T+1):
    money = int(input())

    # 모든 돈의 리스트
    m_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    # 결과를 넣을 리스트
    result = [0] * 8
    for i in range(len(m_list)):
        # 만약에 해당하는 돈으로 나눴을 때 몫이 존재한다면
        if money // m_list[i] > 0:
            # 그 몫을 result에 추가해주고
            result[i] += money//m_list[i]
            # 나머지를 money로 초기화시켜준다
            money = money % m_list[i]

    result = ' '.join(map(str, result))
    print('#{}'.format(tc))
    print(result)

