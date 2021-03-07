# 문제 이해가 안되서 못 풀겠네.

# 맵 크기는 n*m이며 상하좌우로 이동 가능하며 바다로는 움직일 수 없다. 위치표시는 a,b로 하며 북쪽으로부터 떨어진 칸의 갯수, 서쪽으로부터 떨어진 칸의 개수이다.
# 1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향(반시계 방향으로 90도 회전한 방향)부터 차례대로 갈 곳을 정한다.
# 2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음 왼쪽으로 한 칸을 전진한다.
#    왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만 수행하고 1단계로 돌아간다.
# 3. 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우에는, 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다.
#    단, 이때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다.
# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1
# 3 output
# 방향설정은 반시계방향
# 기준에서 왼쪽에 안 가봤으면 왼쪽으로 1이동
# 전부 가봣으면
# 기존 방향 -1이동, 더 이상 이동이 불가능할 때, 멈춤

from sys import stdin
n, m = map(int, stdin.readline().split())
pos_x, pos_y, present_dir = map(int, stdin.readline().split())
dirc_ccw = [(3, 2, 1), (0, 3, 2), (1, 0, 3), (2, 1, 0)]# dir 0 north 1 east 2 south 3 west
# 0 land 1 sea
map = []
for i in range(n):
    map.append(stdin.readline().split())

print(n, m)
print(pos_x, pos_y, present_dir)
print(map)
cnt = 0
while True:
    # step 1 to 2
    for i in dirc_ccw[present_dir]:
        if i == 0:
            temp_y = pos_y - 1
            if temp_y >= 0 and map[temp_y][pos_x] == '0':
                map[pos_y][pos_x] = '2'
                pos_y = temp_y
                cnt += 1
        elif i == 1:
            temp_x = pos_x + 1
            if temp_x <= m and map[pos_y][temp_x] == '0':
                map[pos_y][pos_x] = '2'
                pos_x = temp_x
                cnt += 1
        elif i == 2:
            temp_y = pos_y + 1
            if temp_y <= n or map[temp_y][pos_x] == '0':
                map[pos_y][pos_x] = '2'
                pos_y = temp_y
                cnt += 1
        elif i == 3:
            temp_x = pos_x - 1
            if temp_x >= 0 and map[pos_y][temp_x] == '0':
                map[pos_y][pos_x] = '2'
                pos_x = temp_x
                cnt += 1
# step 3
if present_dir = present_dir
