# 길이가 N인 수열이 주어졌을 때, 그 수열의 합을 구하려고 한다. 하지만, 그냥 그 수열의 합을 모두 더해서 구하는 것이 아니라, 수열의 두 수를 묶으려고 한다.
# 어떤 수를 묶으려고 할 때, 위치에 상관없이 묶을 수 있다. 하지만, 같은 위치에 있는 수(자기 자신)를 묶는 것은 불가능하다. 그리고 어떤 수를 묶게 되면,
# 수열의 합을 구할 때 묶은 수는 서로 곱한 후에 더한다.
#
# 예를 들면, 어떤 수열이 {0, 1, 2, 4, 3, 5}일 때, 그냥 이 수열의 합을 구하면 0+1+2+4+3+5 = 15이다.
# 하지만, 2와 3을 묶고, 4와 5를 묶게 되면, 0+1+(2*3)+(4*5) = 27이 되어 최대가 된다.
#
# 수열의 모든 수는 단 한번만 묶거나, 아니면 묶지 않아야한다.
#
# 수열이 주어졌을 때, 수열의 각 수를 적절히 묶었을 때, 그 합이 최대가 되게 하는 프로그램을 작성하시오.

# 음수가 짝수 확인 짝수면 음수끼리 곱하기
#
# 3개 이상이면 작은거 2개끼리 더하고 아닌 것끼리

n = int(input())
list_plus = []
list_minus = []
while n > 0:
    n = n - 1
    a = int(input())
    if a >= 0:
        list_plus.append(a)
    else:
        list_minus.append(a)

list_plus.sort()
list_minus.sort()
print(list_plus)
print(list_minus)
sum_plus = 0
if len(list_plus) % 2 == 0:
    for i in range(len(list_plus) // 2):
        sum_plus += list_plus[2 * i] * list_plus[2 * i+1]
else:
    for i in range((len(list_plus) - 1) // 2):
        sum_plus += list_plus[2 * i + 1] * list_plus[2 * (i + 1)]
    sum_plus = sum_plus + list_plus[0]
print(sum_plus)

sum_minus = 0
if len(list_minus) % 2 == 0:
    for i in range(len(list_minus) // 2):
        sum_minus += list_minus[2 * i] * list_minus[2 * i+1]
else:
    for i in range((len(list_minus) - 1) // 2):
        sum_minus += list_minus[2 * i + 1] * list_minus[2 * (i + 1)]
    sum_minus = sum_minus + list_minus[0]
print(sum_minus)
print(sum_plus + sum_minus)
