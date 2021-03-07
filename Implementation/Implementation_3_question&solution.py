# 8*8 체스판에서 위치가 주어졌을 때, 나이트가 움직일 수 있는 경우의 수를 출력

pos = input()
y = int(pos[1])
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
x = alpha.index(pos[0]) + 1
cnt = 0
direct = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)]

for i in direct:
    temp_x = x + i[0]
    temp_y = y + i[1]
    if 1 <= temp_x <= 8 and 1 <= temp_y <= 8:
        cnt += 1
print(cnt)
