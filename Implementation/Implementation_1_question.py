#상화좌우
# 5
# R R R U D D
# 3 4

from sys import stdin

n = int(stdin.readline())
direction = list(stdin.readline().split())
x = 1; y =1
for i in direction:
    if i == 'R':
        if x + 1 <= n:
            x += 1
    elif i == 'L':
        if x - 1 > 0:
            x -= 1
    elif i == 'D':
        if y + 1 <= n:
            y += 1
        print('D', y)
    elif i == 'U':
        if y - 1 > 0:
            y -= 1
print(y, x)
