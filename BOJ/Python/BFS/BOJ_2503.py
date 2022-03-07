# BOJ_2503 숫자 야구

from itertools import permutations

N = int(input())
per = list(permutations(list(range(1, 10)), 3))

for _ in range(N):
    num, s, b = map(int, input().split())
    num = list(map(int, str(num)))

    rm_cnt = 0

    for i in range(len(per)):
        i -= rm_cnt # remove한 것들 range에서 빼기 위함.

        s_cnt = 0
        b_cnt = 0

        for j in range(3):
            if num[j] in per[i]:
                if j == per[i].index(num[j]):
                    s_cnt += 1
                else:
                    b_cnt += 1
        
        if s_cnt != s or b_cnt != b:
            per.remove(per[i])
            rm_cnt += 1

print(len(per))