#快速排序
import  random

#方法一 截断再拼接，感觉有点蠢，见谅。
# def QuickSort(list):
#     n = len(list)
#
#     if n == 0:
#         return []
#     if n ==1:
#         return list
#     curr = 1
#     for i in range(1,n):
#         if list[i] < list[0]:
#             temp = list[i]
#             list[i] = list[curr]
#             list[curr] = temp
#             curr += 1
#     temp = list[curr-1]
#     list[curr-1] = list[0]
#     list[0] = temp
#     left = QuickSort(list[:curr-1])
#     right = QuickSort(list[curr:])
#
#
#     return left + [list[curr-1]] + right


#方法二 直接传入list与指针
def QuickSort(list,left,right):

    if right - left <= 1:
        return
    curr = 1
    for i in range(left+1,right):
        if list[i] < list[left]:
            temp = list[left+curr]
            list[left+curr] = list[i]
            list[i] = temp
            curr += 1
    temp = list[left]
    list[left] = list[left+curr-1]
    list[left+curr-1] = temp
    QuickSort(list,left,left+curr-1)
    QuickSort(list,left+curr,right)

    return list


if __name__ == '__main__':

    a = [11,11]
    for i in range(10):
        a.append(random.randint(1,100))
    print(a)
    # print(QuickSort(a))
    print(QuickSort(a,0,len(a)))