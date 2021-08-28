import sys
sys.stdin = open('2605.txt')

N = int(input())
# N명의 학생이 뽑은 번호의 리스트
data = list(map(int, input().split()))
# N명의 학생이 줄을 선 순서를 나타낼 결과
result = []
# 학생은 1번부터 N번까지
for i in range(1, N+1):
    # 그 학생이 뽑은 번호를 idx로 저장
    idx = data[i-1]
    # 그 학생을 총 길이에서 idx만큼 뺀 위치에 insert 시키기
    result.insert(len(result)-idx, i)

print(*result)
