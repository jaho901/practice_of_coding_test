## 1712
# 손익분기점

A, B, C = map(int, input().split())

if C > B:
    result = (A / (C - B)) + 1

else:
    result = -1

print(int(result))





















