'''
data = list(map(int, input().split()))
result = 0
for i in range(len(data)):
  result += data[i]**2
result = result % 10
print(result)
'''
'''
N = int(input())
data = list(map(int, input().split()))
data = list(set(data))
data = sorted(data)
print(*data)
'''
'''
T = int(input())

def find(N):
  if N == 1:
    return 1
  elif N == 2:
    return 2
  elif N == 3:
    return 4
  else:
    return find(N-1) + find(N-2) + find(N-3)

for _ in range(1, T+1):
    result = 0
    N = int(input())
    result += find(N)
    print(result)
'''

'''
SELECT upload_date FROM VIDEO_INFO
ORDER BY upload_date DESC LIMIT 1;
'''