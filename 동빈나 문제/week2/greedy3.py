'''
0001100 -> 0다음에 1이 나오면 연속으로 나오는 1을 한 묶음
00110100 -> 1 2번
110100011101 -> 0 3번
연속으로 중복됨을 없애면 된다.

'''
'''
def solution(string):
    string_list = list(string)
    result = []
    if string_list[0] == '0':
        result.append('0')
        for i in range(len(string_list)-1):
            if string_list[i] == string_list[i+1]:
                continue
            else:
                result.append(string_list[i+1])
    elif string_list[0] == '1':
        result.append('1')
        for i in range(len(string_list)-1):
            if string_list[i] == string_list[i+1]:
                continue
            else:
                result.append(string_list[i+1])

    a0 = result.count('0')
    a1 = result.count('1')

    if a0 > a1:
        return a1
    elif a0 < a1:
        return a0
'''

def solution(s):
    prev=''
    cnt = 0
    for i in s:
        if i != prev:
            cnt += 1
            prev = i
    return (cnt)//2

a = input()

print(solution(a))












