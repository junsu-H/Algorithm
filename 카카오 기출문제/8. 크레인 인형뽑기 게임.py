# 7. 키패드 누르기

def solution(numbers, hand):
    dic = {
              "1": [0, 0], "2": [0, 1], "3": [0, 2],
              "4": [1, 0], "5": [1, 1], "6": [1, 2],
              "7": [2, 0], "8": [2, 1], "9": [2, 2],
              "*": [3, 0], "0": [3, 1], "#": [3, 2]
          }

    answer = ""

    left_x, left_y = dic["*"]       # 왼손 처음 위치
    right_x, right_y = dic["#"]     # 오른손 처음 위치

    for number in numbers:
        number = str(number)
        
        # 1, 4, 7은 왼손으로 누르기
        if number in ["1", "4", "7"]:
            left_x, left_y = dic[number]
            answer += "L"

        # 3, 6, 9는 오른손으로 누르기
        elif number in ["3", "6", "9"]:
            right_x, right_y = dic[number]
            answer += "R"
        
        # 2, 5, 8은 현재 손에서 가까운 손으로 누르기
        else:
            # 2, 5, 8에 해당하는 dictionary value 값
            mid_x, mid_y = dic[number]

            # 어디가 더 가까운지 확인
            left = abs(left_x - mid_x) + abs(left_y - mid_y)
            right = abs(right_x - mid_x) + abs(right_y - mid_y)

            # 거리가 같으면 hand에 따라 처리
            if left == right:
                h = hand[0].upper()
                answer += h
                if h == "R":
                    right_x, right_y = dic[number]  # 오른손으로 눌렀으니 오른손 위치 초기화
                else:
                    left_x, left_y = dic[number]    # 왼손으로 눌렀으니 왼손 위치 초기화
            
            # 오른손이 더 가까울 때
            elif left > right:
                answer += "R"
                right_x, right_y = dic[number]      # 오른손으로 눌렀으니 오른손 위치 초기화
            
            # 왼손이 더 가까울 때
            else:
                answer += "L"
                left_x, left_y = dic[number]        # 왼손으로 눌렀으니 왼손 위치 초기화

    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"

print(solution(numbers, hand))
