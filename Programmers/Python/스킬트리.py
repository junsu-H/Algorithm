# 스킬트리

def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_list = list(skill)

        for s in skills:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        
        # for에서 break 안 걸리면
        else:
            answer += 1
    
    return answer

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"] 

print(solution(skill, skill_trees))