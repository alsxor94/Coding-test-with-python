# 세계적인 도둑 상덕이는 보석점을 털기로 결심했다.
#
# 상덕이가 털 보석점에는 보석이 총 N개 있다. 각 보석은 무게 Mi와 가격 Vi를 가지고 있다. 상덕이는 가방을 K개 가지고 있고,
# 각 가방에 담을 수 있는 최대 무게는 Ci이다. 가방에는 최대 한 개의 보석만 넣을 수 있다.
#
# 상덕이가 훔칠 수 있는 보석의 최대 가격을 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N과 K가 주어진다. (1 ≤ N, K ≤ 300,000)
#
# 다음 N개 줄에는 각 보석의 정보 Mi와 Vi가 주어진다. (0 ≤ Mi, Vi ≤ 1,000,000)
#
# 다음 K개 줄에는 가방에 담을 수 있는 최대 무게 Ci가 주어진다. (1 ≤ Ci ≤ 100,000,000)
#
# 모든 숫자는 양의 정수이다.

import time
start = time.time()

n, k = map(int, input().split()) # number of jewellery, number of bag
jew_mass = []
jew_val = []
while n > 0:
    n = n - 1
    m, v = map(int, input().split()) # mass, value of jewellery
    jew_mass.append(m)
    jew_val.append(v)

print(jew_mass, jew_val)

bag = []
for i in range(k):
    bag.append(int(input())) # volume of bag
bag.sort()

# 가방마다 무게가 정해져 있고, 어차피 가방 안엔 하나 밖에 못 들어감. 그럼 가치가 젤 높은 걸, 먼저 순서를 찾고, 가방에 들어갈 수 있는 지를 찾고,
# 가치가 가장 높은 것부터, 무게를 가장 적게 옮길 수 있는 가방에 넣으면 됨
summa = 0

while len(bag) > 0:
    max_val_index = jew_val.index(max(jew_val))
    max_val = jew_val.pop(max_val_index)
    max_mass = jew_mass.pop(max_val_index)
    print(max_mass, max_val)
    for i in bag:
        if i >= max_mass:
            summa = summa + max_val
            bag.remove(i)

print(summa)

end = time.time()
print(end - start)

#인풋을 한 번에 받는 방법을 몰랐음
