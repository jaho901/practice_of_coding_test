def minus(number):
    a, b = map(int, number.split())
    result = a - b
    return result

num = input()
# print(map(int, num.split()))
print(minus(num))
