def solution(data):
    string = []
    number = []

    for i in data:
        if 48 <= ord(i) <= 57:
            number.append(i)
        elif ord(i) >= 65:
            string.append(i)

    string = sorted(string)
    total = 0
    for i in number:
        total += int(i)

    result = ''.join(string) + str(total)
    return result


data = list(map(str, input()))

print(solution(data))


# K1KA5CB7
# AJKDLSI412K4JSJ9D
