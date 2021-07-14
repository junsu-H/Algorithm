# 방문 길이

def solution(dirs):
    # U, D, L, R
    dx = [-1, 1, 0, 0] 
    dy = [0, 0, -1, 1]
    
    direction = {
        'U': 0,
        'D': 1,
        'L': 2,
        'R': 3
    }
    
    visited = set()

    x, y = 0, 0
    answer = 0

    for key in dirs:
        value = direction[key]
        nx = x + dx[value]
        ny = y + dy[value]
        if nx < -5 or nx > 5 or ny < -5 or ny > 5:
            continue
        
        if (x, y, nx, ny) not in visited:
            visited.add((x, y, nx, ny))
            visited.add((nx, ny, x, y))
            answer += 1 
        x = nx
        y = ny

    return answer


dirs = "LULLLLLLU"
print(solution(dirs))

dirs = "ULURRDLLU"	
print(solution(dirs))