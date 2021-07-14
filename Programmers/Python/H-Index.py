# H-Index Level 2 

def solution(citations):
    citations.sort(reverse=True)
    answer = 0
    for i in range(len(citations)):
        if citations[i] > answer:
            answer += 1
        elif citations[i] == answer:
            break
    return answer

citations = [3, 0, 6, 1, 5]	
print(solution(citations))