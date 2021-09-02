def solution(s):
    minimum = len(s)
    length = len(s) // 2
    cnt = 1
    for n in range(1, length + 1):
        result = []
        for i in range(len(s)):
            if n * (i + 2) <= len(s):
                if s[n * i:n * (i + 1)] == s[n * (i + 1):n * (i + 2)]:
                    cnt += 1
                elif s[n * i:n * (i + 1)] != s[n * (i + 1):n * (i + 2)]:
                    if cnt > 1:
                        result.append(cnt)
                    result.append(s[n * i:n * (i + 1)])
                    cnt = 1

            else:
                if cnt > 1:
                    result.append(cnt)
                result.append(s[n * i:n * (i + 1)])
                if len(s[n * (i + 1):]) != 0:
                    result.append(s[n * (i + 1):])
                break
        result = ''.join(map(str, result))
        if minimum > len(result):
            minimum = len(result)
        cnt = 1

    return minimum

print(solution(input()))

