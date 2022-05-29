def calc(a, b):
    count = int(a % b)
    sum = 0
    sum += count
    return sum


T = int(input())
for i in range(1, T + 1):
    N = int(input())
    case = list(map(int, input().split()))

    for j in range(N):
        for k in range(len(case)):
            print(f"#{i} {calc(case[j], case[k])}")
