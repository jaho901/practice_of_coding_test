
def gj(num):
    num_list = list(map(int, num.split()))
    sum_num = 0
    for i in num_list:
        sum_num += i**2

    result = sum_num % 10
    return result

a = input()
print(gj(a))


