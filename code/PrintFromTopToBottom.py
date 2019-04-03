# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        
        queue = [root]
        result = []
        while queue:
            elem = queue.pop(0)
            if elem != None: #注意空树的情况
                if elem.left!=None: #注意子节点为空的情况
                    queue.append(elem.left)
                if elem.right!=None:
                    queue.append(elem.right)
                result.append(elem.val)
            else:
                return queue
        return result
        
