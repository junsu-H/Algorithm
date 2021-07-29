# BOJ_4673 셀프 넘버

def solution():
    temp = range(1, 10001)
    self_list = []
    for i in range(1, 10000):
        self_num = i
        for j in str(i):
            self_num += int(j)
        if self_num <= 10000:
            self_list.append(self_num)

    answer = sorted(list(set(temp)-set(self_list)))

    for s in answer:
        print(s)

solution()