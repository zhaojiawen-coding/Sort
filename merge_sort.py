#归并排序
import random

def MergeSort(list,left,right):

    if right - left <= 1:
        return
    mid = (left + right) // 2
    MergeSort(list,left,mid)
    MergeSort(list,mid,right)

    tem_list = []
    a_index = 0
    b_index = 0
    while a_index < mid- left and b_index < right-mid:
        if list[left+a_index] < list[mid+b_index]:
            tem_list.append(list[left+a_index])
            a_index += 1
        else:
            tem_list.append(list[mid+b_index])
            b_index += 1
    if a_index < mid -left:
        tem_list += list[left+a_index:mid]
    else:
        tem_list += list[mid+b_index:right]

    list[left:right] = tem_list

    return list




if __name__ == '__main__':

    a = [11,11]
    for i in range(10):
        a.append(random.randint(1,100))
    print(a)
    print(MergeSort(a,0,len(a)))