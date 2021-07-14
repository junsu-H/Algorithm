# 기능개발

def solution(progresses, speeds):
    answer = []
    day = 0
    count = 0
    
    while len(progresses) is not 0:
        if progresses[0] + (day * speeds[0]) >= 100:
            count += 1
            progresses.pop(0)
            speeds.pop(0)
        else:
            if count:
                answer.append(count)
                count = 0
            day += 1
        
    answer.append(count)

    return answer


progresses = [93, 30, 55]	
speeds = [1, 30, 5]
print(solution(progresses, speeds))

progresses =  [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
print(solution(progresses, speeds))