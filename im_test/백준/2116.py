import sys
sys.stdin = open('2116.txt')

N = int(input())

data = []
# 주사위마다 가지고 있는 쌍을 딕셔너리에 넣고 data에 추가해준다.
# 그럼 data에는 총 N개의 주사위의 정보를 담은 딕셔너리가 담기게 된다.
for _ in range(N):
    sub = list(input().split())
    dic = {
        int(sub[0]):int(sub[5]),
        int(sub[1]):int(sub[3]),
        int(sub[2]):int(sub[4]),
        int(sub[3]):int(sub[1]),
        int(sub[4]):int(sub[2]),
        int(sub[5]):int(sub[0])
    }
    data.append(dic)

# 가장 아래 주사위의 윗면이 1 ~ 6인 경우를 모두 number에 담았다.
number = []
for i in range(1, 7):
    # sub = [가장 아래의 주사위 아랫면, 윗면의 값]
    sub = [[data[0][i], i]]
    idx = i
    # 그 위의 주사위들의 아랫면과 윗면을 차례대로 sub에 추가해준다.
    for j in range(1, N):
        # n = [전 주사위의 윗면값이 아랫면으로 가게 지정해주고, 새로운 주사위의 윗면값]
        n = [idx, data[j][idx]]
        # 다시 그 윗면값을 idx로 지정해줘서 다음 주사위 아랫면으로 가게해준다!!
        idx = data[j][idx]
        sub.append(n)
    # 추가한 sub를 최종 number 리스트에 추가!!
    number.append(sub)


result = []
for i in number:
    total = 0
    for j in i:
        if 6 in j:
            # 윗면, 아랫면이 5와 6으로 이루어져있으면
            # 그 옆면의 최댓값은 4가 된다!!
            if j == [5, 6] or j == [6, 5]:
                total += 4
            # 그 외에 6만 존재할 경우 최댓값은 5가 된다.
            else:
                total += 5
        # 윗면, 아랫면에 6이 존재하지 않으면 4개의 옆면의 최댓값은 6이 된다.
        else:
            total += 6
    result.append(total)
print(max(result))

