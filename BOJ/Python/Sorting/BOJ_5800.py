import sys

def solution():
    n = int(sys.stdin.readline().rstrip())

    for i in range(n):
        class_list = list(map(int, sys.stdin.readline().rstrip().split()))
        del class_list[0]
        class_list.sort()
        print("Class " + str((i+1)))

        diff = []
        for j in range(len(class_list) - 1):
                diff.append(class_list[j+1] - class_list[j])

        print("Max " + str(max(class_list)) + ", Min " + str(min(class_list)) + ", Largest gap " + str(max(diff)))

solution()