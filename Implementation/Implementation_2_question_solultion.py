# 0시 0분 0초 부터 N시 59분 59초까지 3이 들어간 시간을 세시오.
# 5
# 11475
n = int(input())
cnt = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                cnt += 1
print(cnt)
