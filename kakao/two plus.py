def solution(numbers):
    answer=[]
    for i in range(numbers):
        count=numbers[i]+numbers[len(numbers)]
        answer.append(count)
        answer=sum(answer)
    return answer