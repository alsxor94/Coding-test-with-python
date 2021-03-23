from sys import stdin
from collections import deque
row, column = map(int, stdin.readline().split())

# bfs로 해야할듯? 길이 전부 파악하고, 그 뒤 2 위치 찾아서 거리 가장 가까운 곳에 벽을 세우면 될 듯.
# --> 논리가 틀림.

def find_2(graph):
    for i in range(row):
        for j in range(column):
            if '2' == graph[i][j]:
                pos_2.append([i, j])

def bfs(r, c):
    queue = deque()
    queue.append((r, c))
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= row or nx < 0 or nx >= column or graph[ny][nx] == '1' or graph[ny][nx] == '2':
                continue
            if graph[ny][nx] == '0' and visited[ny][nx] == 0:
                visited[ny][nx] = visited[y][x] + 1
                queue.append((ny, nx))

# 영역의 개념을 어떻게 구현할 수 있을까? 싸였다라는 개념을 어케 넣지?
# 어떻게 벽을 세울까? 무슨 논리로?
def fence():
    return 1




graph = []
pos_2 = []
step = []
for i in range(row):
    graph.append(stdin.readline().split())
    step.append([0]*column)

find_2(graph)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for r, c in pos_2:
    print(r, c)
    visited = []
    for i in range(row):
        visited.append([0] * column)
    bfs(r, c)
    for k in range(row):
        print(visited[k])
        for j in range(column):
            step[k][j] += visited[k][j]

print()
for i in step:
    print(i)
