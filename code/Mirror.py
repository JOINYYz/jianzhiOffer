# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
    '''
    和先根遍历相似，将打印根值部分替换成“交换左右节点”
    '''
        # write code here
        cur = root
        stack = []
        while stack or cur:
            while cur != None:               
                if cur.left or cur.right :
                    cur.left,cur.right = cur.right,cur.left
                stack.append(cur)
                cur = cur.left
            elm = stack.pop()
            if elm.right != None:
                cur = elm.right
        return root
        
            
    
