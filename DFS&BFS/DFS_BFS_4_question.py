# 문제
# 세로 R칸, 가로 C칸으로 된 표 모양의 보드가 있다. 보드의 각 칸에는 대문자 알파벳이 하나씩 적혀 있고, 좌측 상단 칸 (1행 1열) 에는 말이 놓여 있다.
# 말은 상하좌우로 인접한 네 칸 중의 한 칸으로 이동할 수 있는데, 새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 모든 칸에 적혀 있는 알파벳과는 달라야 한다.
# 즉, 같은 알파벳이 적힌 칸을 두 번 지날 수 없다.
# 좌측 상단에서 시작해서, 말이 최대한 몇 칸을 지날 수 있는지를 구하는 프로그램을 작성하시오. 말이 지나는 칸은 좌측 상단의 칸도 포함된다.
# 입력
# 첫째 줄에 R과 C가 빈칸을 사이에 두고 주어진다. (1 ≤ R,C ≤ 20) 둘째 줄부터 R개의 줄에 걸쳐서 보드에 적혀 있는 C개의 대문자 알파벳들이 빈칸 없이 주어진다.
# 출력
# 첫째 줄에 말이 지날 수 있는 최대의 칸 수를 출력한다.
# definitely back tracking necessary
# 2 4
# CAAB
# ADCB
# output
# 3
# 3 4
# ABBC
# ECED
# FGDH

from sys import stdin
def back(r, c):
    global result
    check = 0
    if not (ord(graph[r][c])) in trace:
        trace.append(ord(graph[r][c]))
        for i in range(4):
            nx = c + dx[i]
            ny = r + dy[i]
            if 0 <= ny < row and 0 <= nx < column and not ord(graph[ny][nx]) in trace:
                back(ny, nx)
            else:
                check += 1
        if check == 4:
            result = max(len(trace), result)
    else:
        check += 1
row, column = list(map(int, stdin.readline().split()))
graph = []

for i in range(row):
    graph.append(list(map(str, stdin.readline()))[:-1])

trace = []
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
result = 0

back(0,0)
print(result)


3 3
ABC
EAF
KGF
0 0
0 1
0 2
1 2
['A', 'B', 'C', 'F']
1 0
2 0
2 1
['A', 'B', 'C', 'F', 'E', 'K', 'G']
7
# if you look at the output, at the turning point 
# so when you the function start, the state should start with present state.


# this version has run time over error.
from sys import stdin, setrecursionlimit
setrecursionlimit(10000)
def bt(r, c, trace):
    global result
    check = 0
    for i in range(4):
        nx = c + dx[i]
        ny = r + dy[i]
        if 0 <= ny < row and 0 <= nx < column and not graph[ny][nx] in trace:
            bt(ny, nx, trace + graph[ny][nx])
        else:
            check += 1
    if check == 4:
        result = max(len(trace), result)

row, column = list(map(int, stdin.readline().split()))
graph = []
for i in range(row):
    graph.append(list(map(str, stdin.readline()))[:-1])

trace = graph[0][0]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
result = 0

bt(0, 0, trace)
print(result)
