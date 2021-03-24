from itertools import combinations as combi
from collections import deque
import copy
from time import time

def find_2(graph):
    for i in range(row):
        for j in range(column):
            if '2' == graph[i][j]:
                pos_2.append([i, j])

# spreading virus
def bfs(r, c, step):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append((r, c))
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= row or nx < 0 or nx >= column or step[ny][nx] == '1':
                continue
            if step[ny][nx] == '0':
                step[ny][nx] = '2'
                queue.append((ny, nx))

# 다른 사람들은 벽을 채울 수 있는 가짓 수를 다 찾아서 함. combination implementation.
def fence():
    global result
    find_2(graph)
    for a, b, c in combi(range(0, row * column - 1), 3):
        x1, y1 = a % column, a // column
        x2, y2 = b % column, b // column
        x3, y3 = c % column, c // column

        step = copy.deepcopy(graph)
        if step[y1][x1] == '0' and step[y2][x2] == '0' and step[y3][x3] == '0':
            step[y1][x1] ,step[y2][x2], step[y3][x3] = '1', '1', '1'
            for vy, vx in pos_2:
                bfs(vy, vx, step)
            tmp = 0
            for i in step:
                tmp += i.count('0')
            result = max(tmp, result)
        else:
            continue



row, column = map(int, input().split())
st = time()
graph = []
result = 0
pos_2 = []
for i in range(row):
    graph.append(input().split())

fence()
print(result)
en = time()
print(en-st) # 2.56s 예제3
