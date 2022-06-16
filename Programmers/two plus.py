numbers = [2, 1, 3, 4, 1]
answer=[]
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        ans = numbers[i] + numbers[j]
        answer.append(ans)
        answer=list(set(answer))
print(answer)