#冒泡排序

import random
def bubbleSort(list):

    n = len(list)

    for i in range(n-1):
        for j in range(n-i-1):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp

    return list

if __name__ == '__main__':
    l = []
    for i in range(10):
        l.append(random.randint(1,100))
    print(l)
    print(bubbleSort(l))


