# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        self.flag = True
        if pRoot == None:
            return self.flag
        self.TreeDepth(pRoot)
        return self.flag
        
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot or self.flag==False:
            return 0
        left = self.TreeDepth(pRoot.left)
        right = self.TreeDepth(pRoot.right)
        if abs(left-right)>1:
            self.flag = False
        return max(left, right) + 1
