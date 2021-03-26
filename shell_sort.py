#希尔排序
#我感觉这个排序不咋滴
import random

def ShellSort(list):

    n = len(list)
    gap = n // 2
    if n < 2:
        return  list
    while gap != 0 :
        for i in range(0,gap):
            head = i
            while head + gap < n:
                tail = head
                temp = list[head + gap]
                while tail >= i and temp<list[tail]:
                    list[tail + gap] = list[tail]
                    tail = tail - gap
                list[tail+gap] = temp
                head = head + gap
        gap = gap // 2
    return list

if __name__ == '__main__':
    a =[11,11]
    for _ in range(10):
        a.append(random.randint(0,100))
    print(a)
    print(ShellSort(a))