from sys import stdin, setrecursionlimit
setrecursionlimit(10000)
# recursion error
def dfs(r, c):
    if 0 <= r < row and 0 <= c < column:
        if graph[r][c] == 1:
            graph[r][c] = 0
            dfs(r + 1, c)
            dfs(r + 1, c + 1)
            dfs(r, c + 1)
            dfs(r - 1, c + 1)
            dfs(r - 1, c)
            dfs(r - 1, c - 1)
            dfs(r, c - 1)
            dfs(r + 1, c - 1)
            return True
        return False
    return False

data = []
while True:
    column, row = list(map(int, stdin.readline().split()))
    if row == 0:
        data.append([column, row])
        break
    data.append([column, row])
    for i in range(row):
        data.append(list(map(int, stdin.readline().split())))

result = []
while True:
    column, row = data.pop(0)
    graph = []
    cnt = 0
    if row == 0 and column == 0:
        break
    else:
        for i in range(row):
            graph.append(data.pop(0))
        for i in range(row):
            for j in range(column):
                if dfs(i, j) == True:
                    cnt += 1
    result += [cnt]
for i in result:
    print(i)
