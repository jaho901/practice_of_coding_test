import sys
sys.stdin = open('1448.txt')

N = int(input())
number = []
for _ in range(N):
    number.append(int(input()))
number = sorted(number)

# for문을 통한 그리디
result = False
for i in range(len(number)-1, 1, -1):
    if number[i] < number[i-1] + number[i-2]:
        print(number[i] + number[i-1] + number[i-2])
        result = True
        break
if result == False:
    print(-1)
    
# while문을 통한 그리디
while True:
    if number[-1] >= number[-2] + number[-3]:
        if len(number) > 3:
            number.pop()
        elif len(number) == 3:
            print(-1)
            break
    else:
        print(number[-1] + number[-2] + number[-3])
        break