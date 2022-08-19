# BOJ_1919 에너그램 만들기 B2

from sys import stdin

input = stdin.readline

first = [0] * 26
second = [0] * 26
answer = 0

for i in input().rstrip():
	first[ord(i)-97] += 1

for i in input().rstrip():
	second[ord(i)-97] += 1

for i in range(26):
	answer += abs(first[i] - second[i])

print(answer)