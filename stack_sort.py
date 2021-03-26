#堆排序
import random

def StackSort(list):
    n = len(list)
    init_stack(list)

    for i in range(n-1):
        temp = list[0]
        list[0] = list[-(i+1)]
        list[-(i+1)] = temp

        check_node(list,0,step=i+1)


    return list






# 初始化一个堆 时间是n
def init_stack(list):

    n = len(list)

    for i in range(n-1,0,-1):
        father_node = (i-1) // 2
        if list[father_node]<list[i]:
            temp = list[i]
            list[i] = list[father_node]
            list[father_node] = temp
            check_node(list,i)


def check_node(lists,index,step = 0):
    """
    检查某个节点是否符合大顶堆的结构
    :param lists: 判断的list
    :param index: 判断点的index
    :param step: 堆顶移动到最末尾的次数
    :return:
    """
    n = len(lists)
    length = n - step
    if 2*index+1 >= length:
        return
    if 2*index+2 < length:
        if lists[2*index+2] >= lists[2*index+1] and lists[2*index+2] > lists[index]:
            temp = lists[index]
            lists[index] = lists[2*index+2]
            lists[2*index+2] = temp
            check_node(lists,2*index+2,step)
        elif lists[2*index+1] > lists[2*index+2] and lists[2*index+1] > lists[index]:
            temp = lists[index]
            lists[index] = lists[2*index+1]
            lists[2*index+1]  = temp
            check_node(lists,2*index+1,step)
    else:
        if lists[2*index+1] > lists[index]:
            temp = lists[index]
            lists[index] = lists[2*index+1]
            lists[2*index+1] = temp
            check_node(lists,2*index+1,step)
        else:
            return

if __name__ == '__main__':
    a = [11,11,16,77,33,2,2]
    for i in range(10):
        a.append(random.randint(1,100))
    print(a)
    print(StackSort(a))





