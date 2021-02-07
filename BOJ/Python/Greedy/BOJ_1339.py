import sys

def solution():
    number = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    words = []
    alpha_dic = {}
    answer = 0

    for _ in range(int(sys.stdin.readline().rstrip())):
        words.append(sys.stdin.readline().rstrip())
    
    for word in words:
        count = 0
        for s in word:
            if s not in alpha_dic:
                alpha_dic[s] = 10 ** (len(word)-count-1)
            elif s in alpha_dic:
                alpha_dic[s] += 10 ** (len(word)-count-1)
            count += 1

    alpha_list = sorted(list(alpha_dic.values()), reverse=True)
    
    for i in range(len(alpha_list)):
        answer += alpha_list[i] * number[i]

    print(answer)

solution()