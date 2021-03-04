# step1. N -1
# step2. N / K , must bedivisible
# choose step 1 or 2
# input
# N K 2 <= N, K <= 100000
# output
# executed times of step1 executed times of step2

n, k = map(int, input().split())
count_1 = 0
count_2 = 0
while n > 1:
    if n / k == n // k :
        n = n / k
        count_1 += 1
        print(n)
        print(count_1)
    else:
        count_2 += n % k
        n = n - n % k
        print(n)
        print(count_2)
        if n == 0:
            count_2 -= 1
print('number of step1', count_1, ',', 'number of step2',count_2, ',', 'total number of step', ',', count_1 + count_2)
