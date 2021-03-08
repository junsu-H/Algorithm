import sys

def solution():
    score_list = [int(sys.stdin.readline().rstrip()) for _ in range(8)]
    
    total = 0
    answer_list = []

    for i in range(5):
        total += max(score_list)
        index = score_list.index(max(score_list))
        answer_list.append(index+1)
        score_list[index] = 0
    
    answer_list.sort()

    print(total)
    print(' '.join(map(str, answer_list)))

solution()