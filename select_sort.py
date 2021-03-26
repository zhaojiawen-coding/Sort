#选择排序
import random
def SelectSort(list):

    n = len(list)

    for i in range(n-1):
        index = i
        for j in range(i+1,n):
            if list[j] < list[index]:
                index = j
        temp = list[i]
        list[i] = list[index]
        list[index] = temp

    return list

if __name__ == '__main__':
    a = [11,11]
    for i in range(10):
        a.append(random.randint(1,100))
    print(a)
    print(SelectSort(a))

