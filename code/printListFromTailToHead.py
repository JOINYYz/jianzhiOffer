# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        val = []
        
        while(listNode != None):
            val.append(listNode.val)
            listNode = listNode.next
        n = len(val)
        re_val=[]
        for i in range(n):
            re_val.append(val[n-i-1]) #头尾下标的关系
        return re_val
