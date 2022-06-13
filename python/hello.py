num = int(input())

for i in range(1, num + 1):
    num_list = list(map(int, input().split()))
    sum_count = 0
    for j in num_list:
        sum_count += j
        ans = sum_count / len(num_list)
    print(f"#{i} {round(ans)}")
