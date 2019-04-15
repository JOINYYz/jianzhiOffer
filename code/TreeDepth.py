# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if pRoot == None:
            return 0
        else:
            cur = pRoot
            depth = 0
            dep_list = []
            stack = []
            while cur or stack:
                while cur != None:
                    stack.append(cur)
                    cur = cur.left
                    depth += 1
                elem = stack.pop()
                dep_list.append(depth)
                depth -= 1
                if elem.right != None:
                    cur = elem.right
                    depth += 1
            return max(dep_list)
