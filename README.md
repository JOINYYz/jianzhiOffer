# 剑指Offer

| # | Title | python | Attention | Date | 运行时间 | 占用内存 |
|---| ----- | -------- | ---------- | ---------- | -------- | -------- |
|4|二维数组中的查找|[python3](./code/find.py)|判断条件、下标溢出|2019/3/17
|5|替换空格|[python3](./code/replaceSpace.py)|split、join|2019/3/17
|6|从尾到头打印链表|[python3](./code/printListFromTailToHead.py)|头尾下标的关系、栈|2019/3/17
|7|重建二叉树|[python3](./code/reConstructBinaryTree.py)|利用前序&中序找到左右子树、递归|2019/3/21
|8|用两个栈实现队列|[python3](./code/push_and_pop.py)|栈、self用法|2019/3/21
|9|旋转数组的最小数字|[python3](./code/minNumberInRotateArray.py)|趣味解法|2019/3/21
|10|斐波那契数列|[python3](./code/Fibonacci.py)|时间复杂度、动态规划代替递归|2019/3/23
|11|跳台阶|[python3](./code/.py)|同斐波那契数列|2019/3/23
|12|变态跳台阶|[python3](./code/jumpFloorII.py)|动态规划|2019/3/23
|13|矩形覆盖|[python3](./code/rectCover.py)|动态规划|2019/3/23
|14|二进制中1的个数|[python3](./code/.py)||2019/3/2？
|15|数值的整数次方|[python3](./code/Power.py)|考虑指数正负、递归O(logn)|2019/3/25
|16|调整数组顺序使奇数在偶数前面|[python3](./code/reOrderArray.py)|用位与计算代替求余|2019/3/25
|17|链表中倒数第K个结点|[python3](./code/FindKthToTail.py)|两个指针实现遍历一次、代码鲁棒性|2019/3/25
|18|反转链表|[python3](./code/ReverseList.py)|三个指针实现链表元素反转|2019/3/25
|19|合并两个排序的列表|[python3](./code/Merge.py)|（非递归）用新链存储合并后的、递归|2019/3/25
|20|树的子结构|[python3](./code/.py)||2019/3/2？
|21|二叉树的镜像|[python3](./code/Mirror.py)|活用先根遍历|2019/3/30
|21|二叉树的镜像|[python3](./code/Mirror2.py)|递归|2019/4/17|24ms|5740k
|22|顺时针打印矩阵|[python3](./code/.py)||2019/3/2？
|23|包含min函数的栈|[python3](./code/minstack.py)|用辅助栈记录每次的最小值|2019/4/3
|24|栈的压入、弹出序列|[python3](./code/IsPopOrder.py)|辅助栈记录压入值|2019/4/3
|25|从上往下打印二叉树|[python3](./code/PrintFromTopToBottom.py)|队列实现层次遍历、注意空树和空子节点情况|2019/4/3
|26|二叉搜索树的后序遍历序列|[python3](./code/VerifySquenceOfBST.py)|二叉搜索左树比根小/右树比根大|2019/4/4
|27|二叉树中和为某一值的路径|[python3](./code/.py)||2019/4/?
|28|复杂链表的复制|[python3](./code/Clone.py)|分解复杂问题、链表指针设计|2019/4/4
|29|二叉搜索树与双向链表|[python3](./code/Convert.py)|递归中序遍历、链表指针设计|2019/4/5
|30|字符串的排列|[python3](./code/Permutation.py)|将字符串分成两部分，未固定部分递归|2019/4/5
|31|数组中出现次数超过一半的数字|[python3](./code/MoreThanHalfNum_Solution.py)|字典计数、遍历key/values|2019/4/5
|32|最小的K个数|[python3](./code/GetLeastNumbers_Solution.py)|、特殊情况|2019/4/5
|33|连续子数组的最大和|[python3](./code/FindGreatestSumOfSubArray.py)|动态规划|2019/4/6
|34|从1~n整数中1出现的次数|[python3](./code/.py)||2019/4/
|35|把数组排成最小的数|[python3](./code/.py)||2019/4/
|36|丑数|[python3](./code/.py)||2019/4/
|37|第一个只出现一次的字符位置|[python3](./code/FirstNotRepeatingChar.py)|hash计数、find函数|2019/4/6
|38|数组中的逆序对|[python3](./code/.py)||2019/4/
|39|两个链表的第一个公共结点|[python3](./code/.py)||2019/4/
|40|数字在排序数组中出现的次数|[python3](./code/GetNumberOfK.py)|二分+指针|2019/4/15|24ms|5732k
|40|数字在排序数组中出现的次数|[python3](./code/GetNumberOfK2.py)|二分|2019/4/15|21ms|5624k
|41|二叉树的深度|[python3](./code/TreeDepth.py)|活用遍历|2019/4/15|22ms|5724k
|41|二叉树的深度|[python3](./code/TreeDepth2.py)|递归|2019/4/17|25ms|5736k
|42|平衡二叉树|[python3](./code/IsBalanced_Solution.py)|活用二叉树深度、flag|2019/4/18
|43|数组中只出现一次的数字|[python3](./code/FindNumsAppearOnce.py)|位异或、找二进制数低位1位置|2019/4/18
|44|和为S的连续正数序列|[python3](./code/FindContinuousSequence.py)|活用指针|2019/4/20
|45|和为S的两个数字|[python3](./code/FindNumbersWithSum.py)|活用指针|2019/4/19
|46|左旋转字符串|[python3](./code/LeftRotateString.py)|翻转|2019/4/22
|47|翻转单词顺序列|[python3](./code/ReverseSentence.py)|头尾指针、list[::-1]切片|2019/4/22
|48|扑克牌顺子|[python3](./code/.py)||2019/4/
|49|圆圈中最后剩下的数|[python3](./code/.py)||2019/4/
|5||[python3](./code/.py)||2019/4/
