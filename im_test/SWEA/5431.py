import sys
sys.stdin = open('5431.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    # 과제를 제출한 학생의 명단
    data = list(map(int, input().split()))

    # 모든 학생의 명단
    student = [i for i in range(1, N+1)]
    
    # 과제를 제출한 학생을 제외시키기
    for i in data:
        if i in student:
            idx = student.index(i)
            student.pop(idx)

    student = ' '.join(map(str, student))
    print('#{} {}'.format(tc, student))

