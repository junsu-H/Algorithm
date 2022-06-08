# 8. 크레인 인형뽑기 게임

def solution(board, moves):
    answer = 0
    stack = []
    N = len(board)

    for move in moves:
        for i in range(N):
            if board[i][move-1] > 0:
                stack.append(board[i][move-1])
                board[i][move-1] = 0

                if len(stack) >= 2:
                    if stack[-1] == stack[-2]:
                        answer += 2
                        stack.pop()
                        stack.pop()
                break

    return answer

board = [
        [0,0,0,0,0],
        [0,0,1,0,3],
        [0,2,5,0,1],
        [4,2,4,4,2],
        [3,5,1,3,1]
        ]
moves =	[1,5,3,5,1,2,1,4]

print(solution(board, moves))

