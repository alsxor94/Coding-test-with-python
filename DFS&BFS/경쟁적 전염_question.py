from collections import deque

# [1pos, 2pos, ...]
def find_num():
    for i in range(num_max):
        for row in range(n):
            for col in range(n):
                if graph[row][col] == '{}'.format(i+1):
                    # num_pos.append([row, col])
                    queue.append(i+1)
                    queue.append((row, col))
                    break


# bfs, how to divide spread timing?
def spread():
    global sec
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        if sec //3 == s:
            print(graph[tar_y - 1][tar_x - 1])
            break
        check = queue.popleft()
        if type(check) == type(1):
            sec += 1
            queue.append(check) #  because of this it never stop
            continue
        y, x = check
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[ny][nx] == '0':
                graph[ny][nx] = graph[y][x]
                queue.append((ny, nx))
        print(sec)
        if sec // 3 == s:
            pass
            # for i in graph:
            #     print(i)
            # print('answer:{}'.format(graph[tar_y - 1][tar_x - 1]))

n, num_max = map(int, input().split())
graph = []
for i in range(n):
    graph.append(input().split())
s, tar_y, tar_x = map(int, input().split())
sec = 0

# print(graph)
# print(s, tar_x, tar_y)

num_pos =[]
queue = deque()
find_num()
# for i in queue:
#     print(type(i) == type(1))
#     print(i)
spread()
# 시간 초과 및 틀림.
