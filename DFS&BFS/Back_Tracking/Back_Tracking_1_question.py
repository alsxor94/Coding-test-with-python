# 문제
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
#
# 1부터 N까지 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.
# 고른 수열은 비내림차순이어야 한다.
# 길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.
# 입력
# 첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)
#
# 출력
# 한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.
#
# 수열은 사전 순으로 증가하는 순서로 출력해야 한다.
#
# 예제 입력 1  복사
# 3 1
# 예제 출력 1  복사
# 1
# 2
# 3

from sys import stdin
#왜 마지막께 반복 될까?
def dfs_back(depth, phase):
	if depth == num:
		print(*arr)
		return

	for i in range(phase, end):
		arr[depth] = i + 1
		dfs_back(depth + 1, i) ### i 쓰는게 핵심!!!

end, num = map(int, stdin.readline().split())
arr = [0] * num
dfs_back(0, 0)
