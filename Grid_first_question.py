# 큰 수의 법칙
# 첫째 줄에 N( 2 <= N <= 1000), M( 2 <= M <= 10000), K( 2 <= K <= 10000)의 자연수가 주어지며, 각 자연수는 공백으로 구분한다.
# 둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각각의 자연수는 1이상 10000이하의 수로 주어진다.
# 입력으로 주어지는 K는 항상 M보다 작거나 같다.

# condition
# 첫째 줄에 동빈이는 큰 수의 법칙에 따라 더해진 답을 출력한다.

# example
# 5	8	3
# 2	4	5	4	6

# print	46

import time
import random
import numpy as np

start_time = time.time()

N = random.randrange(2, 1000)#making N number of list
N_arr = np.empty(N)
M = random.randrange(2, 10000)#adding number Mth
K = random.randrange(2, 10000)#maximum number of adding counts of each index number


# N = random.randint(2, 5)#making N number of list
# N_arr = np.empty(N)
# M = random.randint(2, 10)#adding number Mth
# K = random.randint(2, M)#maximum number of adding counts of each index number
#top2까지만 구하고, top1*K+top2+... 이런식으로 계산하면됨.

# 1. define N, M, K by random.randint
# 2. make a N_arr
# 3. check number of max, if the number of max is over 2, then the anser will be max * K
# 4. if the max number is one, then find top2, making a equation.

for i in range(N):
    a = random.randint(2, 1000)#연습할땐, 1000말고 적은걸로 바꾸기
    N_arr[i] = a
# print(N_arr)
# print(N, M, K)

top_1 = np.max(N_arr)
top_1_index = np.where(top_1 == N_arr)[0]
# print(len(top_1_index))
# print(top_1_index)

top_1 = np.max(N_arr)
top_1_index = np.where(top_1 == N_arr)[0]
# print(len(top_1_index))
# print(top_1_index)

if len(top_1_index) > 1:
    print('output: ',top_1*M)
else:
    N_arr = np.delete(N_arr, top_1_index[0])
#     print('N_arr:',N_arr)
    top_2 = max(N_arr)
#     print('top_2', top_2)
    count = M//(K+1)
#     print(count)
    left = M%(K+1)
#     print(left)
#     print(top_1*K*count + top_2*count + top_1*left)
end_time = time.time()
print(end_time - start_time)
