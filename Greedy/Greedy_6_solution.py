import sys
n = int(sys.stdin.readline())
list_plus = []
list_minus = []
while True:
    n = n - 1
    a = int(sys.stdin.readline())
    if a >= 0:
        list_plus.append(a)
    else:
        list_minus.append(a)
    if n == 0:
        break

list_plus.sort()
list_minus.sort()

sum_plus = 0
if len(list_plus) % 2 == 0:
    for i in range(len(list_plus) // 2):
        sum_plus += list_plus[2 * i] * list_plus[2 * i+1]
else:
    for i in range((len(list_plus) - 1) // 2):
        sum_plus += list_plus[2 * i + 1] * list_plus[2 * (i + 1)]
    sum_plus = sum_plus + list_plus[0]


sum_minus = 0
if len(list_minus) % 2 == 0:
    for i in range(len(list_minus) // 2):
        sum_minus += list_minus[2 * i] * list_minus[2 * i+1]
else:
    for i in range((len(list_minus) - 1) // 2):
        sum_minus += list_minus[2 * i + 1] * list_minus[2 * (i + 1)]
    sum_minus = sum_minus + list_minus[0]

print(sum_plus + sum_minus)
