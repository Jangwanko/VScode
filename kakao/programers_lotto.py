def solution(lottos, win_nums):
    answer = []
    zero=0
    for i in lottos:
        if i in win_nums:
            zero+=1

    return answer


print(solution)

'''자기 번호와 당첨번호의 교집합을 구해서 최소 당첨등수를  구한다.

    차집합을 통하여 0의 갯수에 따라 최대 당첨등수를 구한다.
    2개 5등 3개 4등 4개 3등 5개 2등 6개 1등
    전부다 0이있다면 최소6 최대 1등'''
