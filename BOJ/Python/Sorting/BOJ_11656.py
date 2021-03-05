import sys

def solution():
    string = sys.stdin.readline().rstrip()
    array = [string[i:] for i in range(len(string))]
    
    print('\n'.join(sorted(array)))
    
solution()