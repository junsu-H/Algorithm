# BOJ_1107 리모컨

N = int(input())
M = int(input())
channel = set(map(str, range(10)))

if M:
    channel -= set(map(str, input().split()))

# +, -로만 채널을 변경했을 때
answer = abs(100 - N) 

for num in range(1000001):
    num = str(num)

    for j in range(len(num)):
        if num[j] not in channel:
            break

        elif j == len(num) - 1:
            # len(num) -> 채널, abs(int(num) - N) -> +, -
            answer = min(answer, abs(int(num) - N) + len(num))

print(answer)