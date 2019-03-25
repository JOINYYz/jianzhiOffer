# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        Node = pHead
        ppre = None
        pnext = None  # 设置了三个指针
        re = None
        while (Node!= None):
            if Node.next == None:
                re = Node
            pnext = Node.next #四步实现将Node的下一个指向前一个元素
            Node.next = ppre
            ppre = Node
            Node = pnext
        return re

       
