# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head == None or k <= 0 : #增加代码鲁棒性
            return None
        else:
            ptr1 = head
            ptr2 = head # 用两个指针
            for i in range(k-1): #第一个指针走到K-1时，第二个指针开始移动
                if ptr1.next == None:
                    return None
                else:
                    ptr1 = ptr1.next
            while (ptr1.next!= None):
                ptr2 = ptr2.next
                ptr1 = ptr1.next
            return ptr2
