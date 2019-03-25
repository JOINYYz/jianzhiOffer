# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        head = ListNode(-1)  #创建一个新的链表头结点来存储合并后的链表
        head.next = None
        ptr = head
        while (pHead1 != None and pHead2 != None): #先比较一样长度的部分
            if pHead1.val <= pHead2.val:
                ptr.next = pHead1
                ptr = pHead1
                pHead1 = pHead1.next
            else:
                ptr.next = pHead2
                ptr = pHead2
                pHead2 = pHead2.next
        if pHead1 == None: # pHead1链表遍历完，剩下的都是pHead2的，这里同时判断了一开始pHead1为None的特殊用例
            ptr.next = pHead2
        if pHead2 == None:
            ptr.next = pHead1
        return head.next
                
            
            
