T = int(input())

for i in range(1, T + 1):
    n = int(input())
    day = list(map(int, input().split()))
    day = day[::-1]
    daysum = 0
    result = day[0]
    for j in range(1, n):
        if result > day[j]:
            daysum = daysum + result - day[j]
        else:
            result = day[j]

    print(f"#{i} {daysum}")


#https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5LrsUaDxcDFAXc&categoryId=AV5LrsUaDxcDFAXc&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=2&pageSize=10&pageIndex=1&&&&&&&&&&&&&&&&&&&&