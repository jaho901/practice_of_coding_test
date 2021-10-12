import sys
sys.stdin = open('1748.txt')

N = input()

mod = [9, 90, 900, 9000, 90000, 900000, 9000000, 90000000, 900000000, 9000000000]
length = len(N)
result = 0
N = int(N)
# print(length)
if length == 1:
    result = N
else:
    for i in range(length-1):
    # 9 + 90*2 + 21*3 = 252
        result += mod[i]*(i+1)
    N -= 10**(length-1)
    result += (N+1)*length
print(result)