import sys
n = int(sys.stdin.readline())
list_plus = []; list_1 = []; list_0 = []; list_11 = []; list_minus = []

while n > 0:
    n = n - 1
    a = int(sys.stdin.readline())
    if a > 1:
        list_plus.append(a)
    elif a == 1:
        list_1.append(a)
    elif a == 0:
        list_0.append(a)
    elif a == -1:
        list_11.append(a)
    else:
        list_minus.append(a)

list_plus.sort()
list_plus.reverse()
list_minus.sort()
sum_plus = 0
# calculating by seperating situation odd or even number
for i in range(len(list_plus) // 2):
    sum_plus += list_plus[2 * i] * list_plus[2 * i + 1]
# when the number of positive is odd
if len(list_plus) % 2 != 0:
    sum_plus = sum_plus + list_plus[-1]

sum_minus = 0
# calculating by seperating situation odd or even number
for i in range(len(list_minus) // 2):
    sum_minus = sum_minus + list_minus[2 * i] * list_minus[2 * i + 1]
# when the number of negative is odd
if len(list_minus) % 2 != 0:
    if len(list_11) > 0:
        sum_minus = sum_minus + list_minus[-1] * list_11.pop()
    elif len(list_0) > 0:
        sum_minus = sum_minus
        list_0.pop()
    else:
        sum_minus = sum_minus + list_minus[-1]
# existence and nonexistence of 0
sum_11 = 0
if len(list_11) > 0:
    if len(list_11) % 2 == 0:
        sum_11 = len(list_11) // 2
    else:
        if len(list_0) > 0:
            sum_11 = len(list_11) // 2
        else:
            sum_11 = len(list_11) // 2 - 1

print(sum_plus + sum_minus + sum(list_1) + sum_11)
