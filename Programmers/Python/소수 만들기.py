
from itertools import combinations

def is_prime(tmp):
    for i in range(2, tmp):
        if tmp % i == 0:
            return False
    return True
    

def solution(nums):
    answer = 0
    
    # 3중 for문으로 풀기 
    # for i in range(0, len(nums)-2):
    #     for j in range(i+1, len(nums)-1):
    #         for k in range(j+1, len(nums)):
    #             tmp = nums[i]+nums[j]+nums[k]
    #             if is_prime(tmp):
    #                 answer += 1
    
    comb = list(combinations(nums, 3))
    for i in comb:
        if is_prime(sum(i)):
            answer += 1

    return answer

nums = 	[1, 2, 7, 6, 4]
print(solution(nums))