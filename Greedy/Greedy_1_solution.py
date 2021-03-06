# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort()# 입력받은 수 정렬
fisrt = data[n-1]
second = data[n-2]

# 가장 큰 수가 더해지는 횟수 계산
count = m // (k+1) * k
count += m % (k+1)

result = 0
result += count * first # add max number
result += (m - count) * second

print(result)

# Syntax :

# map(fun, iter)
# list(map(fun,list))
# tuple(map(fun, tuple))

# Parameters :

# fun : It is a function to which map passes each element of given iterable.
# iter : It is a iterable which is to be mapped.
