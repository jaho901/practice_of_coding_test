import sys
sys.stdin = open('practice2.txt')

T = int(input())

for tc in range(1, T+1):
    word = int(input())
    result = ''

    # 아래와 같은 값을 왜 지정해주었냐?? ==> 음수 양수 여부 확인 및 조치를 위해
    is_negative = False

    # 음수인 경우 바꿔준다!!
    if word < 0:
        word = word * -1
        is_negative = True

    while word > 0:
        result = chr(word % 10 + 48) + result
        word = word // 10

    # if문 다음에 아래와 같이 조건을 안써준거는 묵음형태다 (is_negative:) = (is_negative==True:)
    if is_negative:
        result = '-' + result

    print('#{} {} {}'.format(tc, result, type(result)))

