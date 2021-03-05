# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())

result = 0
# 한 줄씩 입력 받아 확인하기
for i in range(n):
    data = list(map(int, input().split()))
    # i행에서 '가장 작은 수' 찾기
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
        
    # 행들을 돌면서 행에서 가장 작은 수중 가장 큰 수 남기기
    result = max(result, min_value)

print(result) # 최종 답안 출력
#이렇게 하면 몇 번째 행인지 알 수 없고, 더 구체적인 값을 찾을 수 없어서. 좋지 않다고 할 수 있다.
#하지만 원하는 값만 찾기 위해서는 가장 빠른 방법.
