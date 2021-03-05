# 타로는 자주 JOI잡화점에서 물건을 산다. JOI잡화점에는 잔돈으로 500원, 100원, 50원, 10원, 5원, 1이 충분히 있고, 언제나 거스름돈 개수가 가장 적게 잔돈을 준다.
# 타로가 JOI잡화점에서 물건을 사고 카운터에서 1000원 지폐를 한장 냈을 때, 받을 잔돈에 포함된 잔돈의 개수를 구하는 프로그램을 작성하시오.
#
# 예를 들어 입력된 예1의 경우에는 아래 그림에서 처럼 4개를 출력해야 한다.
# 500원 1개, 100원, 1개, 10원 2개

budget = 1000
price = int(input())

change = budget - price
count = 0
while change > 0:
    if change // 500 >= 1:
        count = count + (change // 500)
        change = change - 500 * (change // 500)
    elif change // 100 >= 1:
        count = count + (change // 100)
        change = change - 100 * (change // 100)
    elif change // 50 >= 1:
        count = count + (change // 50)
        change = change - 50 * (change // 50)
    elif change // 10 >= 1:
        count = count + (change // 10)
        change = change - 10 * (change // 10)
    elif change // 5 >= 1:
        count = count + (change // 5)
        change = change - 5 * (change // 5)
    elif change // 1 >= 1:
        count = count + (change // 1)
        change = change - 1 * (change // 1)

print(count)
