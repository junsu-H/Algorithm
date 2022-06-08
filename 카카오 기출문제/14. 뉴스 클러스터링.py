from collections import defaultdict

def solution(N, stages):
    denominator = len(stages)  # 분모

    fail_dic = defaultdict(int)

    for i in range(1, N+1):
        cnt = stages.count(i)
        fail = 0

        if cnt != 0:
            fail = cnt/denominator

        fail_dic[i] = fail
        denominator -= cnt

    answer = sorted(fail_dic, key = lambda x: -fail_dic[x])

    return answer

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))

N = 4
stages = [4,4,4,4,4]
print(solution(N, stages))
