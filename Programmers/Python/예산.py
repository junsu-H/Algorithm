# 예산

def solution(d, budget):
    d.sort()
    answer = 0

    for i in d:
        if budget >= i:
            budget -= i
            answer += 1
        else:
            break
    return answer

d = [1, 3, 2, 5, 4]
budget = 9
print(solution(d, budget))

d = [2, 2, 3, 3]
budget = 10
print(solution(d, budget))