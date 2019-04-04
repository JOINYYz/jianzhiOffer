# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        #不能忘记空链表的特殊情况
        if pHead == None:
            return None
            
        # 在原节点后复制新节点
        cur = pHead
        while (cur!=None):
            new = RandomListNode(cur.label)
            new.next = cur.next
            cur.next = new
            cur = new.next
            
        #复制新节点的random节点
        cur = pHead
        while (cur!=None):
            if cur.random!=None:
                cur.next.random = cur.random.next
            cur = cur.next.next
            
        #分离新旧链表
        cur = pHead
        head = pHead.next
        ptr = head
        while(cur!=None):
            cur.next = cur.next.next
            if (ptr.next!=None):
                ptr.next = ptr.next.next
            cur = cur.next
            ptr = ptr.next
        return head
