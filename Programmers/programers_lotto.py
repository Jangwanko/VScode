def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]

    cnt_0 = lottos.count(0)  # lottos 안의 0의 개수를 반환
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1

    return rank[cnt_0 + ans], rank[ans]


'''자기 번호와 당첨번호의 교집합을 구해서 최소 당첨등수를  구한다.

    차집합을 통하여 0의 갯수에 따라 최대 당첨등수를 구한다.
    2개 5등 3개 4등 4개 3등 5개 2등 6개 1등
    전부다 0이있다면 최소6 최대 1등'''
