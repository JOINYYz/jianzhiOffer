# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    #head指向最小的，tail指向当前最大的（不断移动Tail）
    head = None
    tail = None
    def Convert(self, pRootOfTree):
        # write code here
        if pRootOfTree == None:
            return None
        self.Convert(pRootOfTree.left) #中序遍历
        if self.head == None: #找到最小的之后就不变
            self.head = pRootOfTree
            self.tail = pRootOfTree
        else:
        # 移动tail指针
            self.tail.right = pRootOfTree
            pRootOfTree.left = self.tail
            self.tail = self.tail.right
        self.Convert(pRootOfTree.right) #中序遍历
        return self.head
