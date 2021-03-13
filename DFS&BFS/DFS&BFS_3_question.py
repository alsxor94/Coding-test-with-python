# N*M 크기의 얼음 틀이 있다. 구멍이 뚫려있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다. 구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어있는 경우 서로 연결되어 있는 것으로 간주한다.
# 이때 얼음 틀의 모양이 주어졌을 때, 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하시오.
# 15 14
# 00000111100000
# 11111101111110
# 11011101101110
# 11011101100000
# 11011111111111
# 11011111111100
# 11000000011111
# 01111111111111
# 00000000011111
# 01111111111000
# 00011111111000
# 00000001111000
# 11111111110011
# 11100011111111
# 11100011111111
# output
# 8

# DFS로 빠르게 읽어서 찾아야할 듯. --> 시작을 0으로 읽을텐데 읽은 부분들을 어떻게 바꿀 것인가
from sys import stdin

# DFS
def dfs(r, c):
    if 0 <= r < row and 0 <= c < column:
        if graph[r][c] == 0:
            graph[r][c] = 1
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)
            return True
        return False
    return False

# making graph
row, column = map(int, stdin.readline().split())
graph = []
for i in range(row):
    graph.append(list(map(int, stdin.readline()[:-1])))

# print(graph)
result = 0
for i in range(row):
    for j in range(column):
        if dfs(i, j) == True:
            result += 1
            print(i, j)

print(graph)
print(cnt)
### 런타임 에러 (RecursionError) 뜸
