# 插入排序
import  random
def insertSort(list):
    n = len(list)
    for i in range(n):
        j = i-1
        while j >= 0 and list[i] < list[j]:
            j -= 1
        temp = list[i]
        for v in range(i,j+1,-1):
            list[v] = list[v-1]
        list[j+1] = temp
    return  list
if __name__ == '__main__':
    l = []
    for i in range(10):
        l.append(random.randint(1,100))
    print(l)
    print(insertSort(l))

