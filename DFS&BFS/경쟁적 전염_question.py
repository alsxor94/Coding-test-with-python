from collections import deque
from sys import stdin
# [1pos, 2pos, ...]
def find_num():
    for i in range(num_max):
        # seperate number at the same time, the virus can exist more than 1
        queue.append(i+1) # seperate 1,2,3, ...
        for row in range(n):
            for col in range(n):
                if graph[row][col] == '{}'.format(i+1):
                    queue.append((row, col))



# bfs, how to divide spread timing?
def spread():
    global sec
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        # 원하는 시간에 멈추고 출력
        check = queue.popleft()
        if type(check) == type(1):
            sec += 1
            if sec // num_max == s:
                if graph[tar_y - 1][tar_x - 1] == '0':
                    print(0)
                    break
                else:
                    print(int(graph[tar_y - 1][tar_x - 1]))
                    break
            # seperate num
            queue.append(check)
            continue
        # speard
        y, x = check
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[ny][nx] == '0':
                graph[ny][nx] = graph[y][x]
                queue.append((ny, nx))

n, num_max = map(int, stdin.readline().split())
graph = []
for i in range(n):
    graph.append(stdin.readline().split())
s, tar_y, tar_x = map(int, stdin.readline().split())
sec = -1

num_pos =[]
queue = deque()
find_num()
spread()
