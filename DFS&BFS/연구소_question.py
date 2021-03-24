from sys import stdin
from itertools import combinations as combi
from collections import deque
import copy
from time import time
# brute force algorithm을 알았어야함.

def find_2(graph):
    for i in range(row):
        for j in range(column):
            if '2' == graph[i][j]:
                pos_2.append([i, j])

# spreading virus
def bfs(r, c, step):
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
    for a, b, c in combi(range(1, row * column), 3):
        x1, y1 = a % column, a // column
        x2, y2 = b % column, b // column
        x3, y3 = c % column, c // column
        if graph[y1][x1] == '0' and graph[y2][x2] == '0' and graph[y3][x3] == '0':
            graph[y1][x1] = '1'
            graph[y2][x2] = '1'
            graph[y3][x3] = '1'
            step = copy.deepcopy(graph)
            for vy, vx in pos_2:
                bfs(vy, vx, step)
            graph[y1][x1] = '0'
            graph[y2][x2] = '0'
            graph[y3][x3] = '0'
            # for i in step:
            #     print(i)
            tmp = 0
            for i in step:
                tmp += i.count('0')
            result = max(tmp, result)
            # print(x1, y1, x2, y2, x3, y3, result)
        else:
            continue



st = time()
row, column = map(int, stdin.readline().split())
graph = []
result = 0
result_1 = []
pos_2 = []
for i in range(row):
    graph.append(stdin.readline().split())

cnt = 0
find_2(graph)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

fence()
print(result)
en = time()
print(en-st) # 3.2s
