# BOJ_1929 소수 구하기

from sys import flags, stdin

input = stdin.readline

def is_prime(m, n):
    n += 1
    primes = [True] * n
    for i in range(2, n):
        if primes[i]:
            for j in range(2*i, n, i):
                primes[j] = False

    for i in range(m, n):
        if i != 1 and primes[i]:
            print(i)

def solution():
    m, n = map(int, input().rstrip().split())
    is_prime(m, n)

solution()