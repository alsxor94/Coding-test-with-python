from sys import stdin

def dfs_cal(cnt, result, plus, minus, multi, divide):
    global max_sum, min_sum, count
    if cnt == n[0]:
        max_sum = max(max_sum, result)
        min_sum = min(min_sum, result)
        return
    if plus:
        dfs_cal(cnt + 1, result + num[cnt], plus - 1, minus, multi, divide)
    if minus:
        dfs_cal(cnt + 1, result - num[cnt], plus, minus - 1, multi, divide)
    if multi:
        dfs_cal(cnt + 1, result * num[cnt], plus, minus, multi - 1, divide)
    if divide:
        dfs_cal(cnt + 1, -(-result // num[cnt]) if result < 0 else result // num[cnt], plus, minus, multi, divide - 1)

n = list(map(int, stdin.readline().split()))
num = list(map(int, stdin.readline().split()))
# + 0  - 1 * 2 // 3
ope = list(map(int, stdin.readline().split()))
max_sum = -10**9
min_sum = 10**9
dfs_cal(1, num[0], ope[0], ope[1], ope[2], ope[3])
print(max_sum)
print(min_sum)
