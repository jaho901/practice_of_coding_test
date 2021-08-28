import sys
sys.stdin = open('13300.txt')

N, K = map(int, input().split())
# 반도 1~6학년까지 고정이고 성별도 0, 1로 고정이기 때문에 딕셔너리를
# 아래와 같이 만들 수 있다.
data = {
    '1_0' : 0,
    '1_1' : 0,
    '2_0' : 0,
    '2_1' : 0,
    '3_0' : 0,
    '3_1' : 0,
    '4_0' : 0,
    '4_1' : 0,
    '5_0' : 0,
    '5_1' : 0,
    '6_0' : 0,
    '6_1' : 0,
}

# input 값들을 받아서 딕셔너리의 key와 동일한 형태로 만들고
# 해당하는 key와 연결된 value 값에 1씩 더해준다.
for i in range(N):
    sex, grade = input().split()
    a = grade + '_' + sex
    data[a] += 1

result = 0

# 그리고 K인원끼리 방 배정을 주고 그 방 개수를 result에 더해준다.
for v in data.values():
    if v % K > 0:
        result += v // K + 1
    else:
        result += v // K

print(result)