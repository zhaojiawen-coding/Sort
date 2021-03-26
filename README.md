#选择排序
![选择排序动态图](Pics/选择排序.gif)

基本思想：

    每次选择最小的数，放到对应的位置

时间复杂度：O(n^2)
    
    选n-1次
    第一次 比n-1个数
    第二次 比n-2个数
    ...
    第n-1次 比1个数

空间复杂度：O(1)
    
    只会附加一个temp记录位

#冒泡排序
![冒泡排序](Pics/冒泡排序.gif)

基本思想：

    每次俩俩互相比较，一轮下来选择出一个最大的放到后边

时间负责度：O(n^2)

    n-1轮比较
    第一轮 n-1 (每一个和后一个比，n-1个数）
    第二轮 n-2 (每一个和后一个比，但是最后一个已经固定，共n-2个数）
    ...
    第n-1轮 1

空间复杂度：O(1)

    只会附加一个temp记录位

#插入排序
![插入排序](Pics/插入排序.gif)

基本思想：

    将元素插入一个有序数列

时间复杂度：O(n^2)

    插入排序虽然时间复杂度是n^2,但是这个是最坏的时间复杂度，实际感觉要比选择排序和冒泡排序快一点，因为每次不
    一定要和之前的所有比较，但是相应的虽然比较次数少一点，但是移动位置的次数增多，只不过计算时间复杂度的时候
    只计算了比较运算

    n-1次插入操作，第一个元素默认有序
    第一从插入 比较1个(按照最坏的计算)
    第二次插入 比较2个
    ...
    第n-1次插入 比较n-1个
空间复杂度：O(1)

    只需要一个temp记录位

#希尔排序
![希尔排序](Pics/希尔排序.gif)

基本思想：
    
    希尔排序是对直接插入排序的改进，引入了增量机制
    以一个递减的增量gap = gap // 2(递减规则不一定），初始gap = len(list) // 2(初始规则也不一定）
    每次比较x ,x + gap ,x + 2* gap ,...这几个数，比较规则也是插入排序
    直到增量递减位1时及比较每一个元素
    个人感觉：增量递减的过程有点像归并排序的感觉，将俩个俩个有序数列合并到一起，比如8个数01234567
    第一次：04 15 26 37 （增量4）
    第二次：0246 1357   （增量2）
    第三次：01234567    （增量1）
    但是希尔排序是不稳定的，比如有10个数0123456789
    第一次：05 16 27 38 49 （增量5）
    第二次：02468 13579    （增量2）
    显然这一次就重排了，浪费了之前排好的顺序，也就是奇数个的增量导致了会有排序结果浪费，所以希尔排序要比直接插入排序快，但是没有归并排序那么优秀。
    本来第一次看觉得希尔排序不太行，但是这样一顺，感觉如果修正增量的处理方法，那希尔排序也是大哥，等有时间再研究（有时间时不可能的）

时间复杂度：O(n^1.3 ~ n^2)

    不稳定，和增量有关，我就不算啦（有人算好了可以分享，我就看看）

空间复杂度：O(1)

    没有多余的空间开销，只有个记录量

## 接下来才是排序的大哥们

# 归并排序
![归并排序](Pics/归并排序.gif)

基本思想：

    归并排序的基本思想就是把原来是数列以2分法切成一棵树，然后从叶子节点再向上俩俩merge

时间复杂度： O(nlogn)

    切分后树的高度是logn ,在每一层都n个数都会经历一次排序

空间复杂度： O(n)

    需要一个list来记录merge那步的结果

#快速排序
![快速排序](Pics/快速排序.gif)

基本思想：

    快排的基本思想也是树，但是与归并不同的是，归并从下到上merge。快排从上到下切分
    首先要选取一个标准值，一般选择第一个元素（作为了根节点），然后将比它小的放到它左边，比它大的放到它右边
    然后每一个部分继续这样操作，直到最小的左边或者右边只有一个或者没有数

时间复杂度：O(nlogn)

    切分开之后就是一颗二叉树，高度为logn
    每一层都要实现找根节点分左右俩个树比较n次

空间复杂度：O(1)

    都是在原来的数组上操作，只有一个临时记录位temp

#堆排序
![堆排序](Pics/堆排序.gif)

基本思想：

    堆排序的基本思想就是利用了堆的概念（记住没有用堆的数据结构）一颗完全二叉树
    一般正序排序都是构造大顶堆，也就是保证每一个父节点都要比俩个子节点大
    写代码要知道的俩个常识：对于一颗完全二叉树。(索引从0，根节点位0)假设父节点的index是i，那左孩子就是2*i+1 右孩子就是2*i+2
    如果找一个节点的父节点可以（假设该节点的index是v) (v-1)//2
    堆排序：
    第一步：将原来的数组看成一个无序的堆
    第二步：将无序的堆调整成大顶堆
    第三步：将根节点与最后一个叶子节点交换，并将堆的大小减一
    第四步：继续将其调整位一个大顶堆
    重复第三步和第四步 知道所有都有序

时间复杂度： O(nlogn)

    很明显的树结构，每个节点都和父节点比较，最多走logn步（比较logn次)
    一共n-1个节点要往上走走比较

空间复杂度： O(1)

    不用其他的空间，直接利用完全二叉树的性质行程一棵理论上的树，只需要临时一个temp


## ！！！
    
### 所有理解均为个人理解，如果有错误欢迎指正，请礼貌交流
### 所有的图片均来自网上，不是个人原创，请勿用于商业
    