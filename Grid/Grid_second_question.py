# input
# 3 3
# 3 1 2
# 4 1 4
# 2 2 2
# output
# 2
# input
# 2 4
# 7 3 1 8
# 3 3 3 4
# output
# 3
# condition
# at the 1st line, giving two numbers, N, M, first column cards number is N, row number is M, 1 <= N, M <= 100
# from 2nd line, showing the card number in each row.
import time
import numpy as np
start_time = time.time()

n, m = map(int, input().split())
deck = np.zeros((n, m))
print(deck)

for i in range(n):
    temp_a = input().split()
    deck[i] = temp_a

deck_temp = np.zeros((n, 3))
a = []
for i in range(len(deck)):
    temp_min_index = np.argmin(deck[i])
    temp_min_val = np.min(deck[i])
    temp = [i, temp_min_val, temp_min_index] # number of row, min_value, index of it
    deck_temp[i] = temp
    a.append(temp_min_val)

index = np.argmax(a)
print('number of row',deck_temp[index][0], 'min_value', deck_temp[index][1], 'index of it', '(', index, deck_temp[index][2], ')')
#행들중 가장 작은 넘들 중에 큰넘이 되는 인덱스 찾기


end_time = time.time()
print(end_time - start_time)
