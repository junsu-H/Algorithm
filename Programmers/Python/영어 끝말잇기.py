# 영어 끝말잇기

def solution(n, words):
    answer = []
    temp = []

    temp.append(words[0])

    for i in range(1, len(words)):
        if words[i] not in temp and words[i-1][-1] == words[i][0]:
            temp.append(words[i])
        else:
            break
    
    if len(temp) == len(words):
        answer = [0,0]
    else:
        number = len(temp)%n + 1
        turn = len(temp)//n + 1
        answer = [number, turn]

    return answer

n=3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
print(solution(n, words))

n = 5
words = ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]
print(solution(n, words))

n=2
words = ["hello", "one", "even", "never", "now", "world", "draw"]
print(solution(n, words))