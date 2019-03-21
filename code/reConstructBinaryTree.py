class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        root = TreeNode(pre[0])
        root_index = tin.index(pre[0])
        right_num = len(tin)- root_index -1
        if root_index > 0:
            root.left = self.reConstructBinaryTree(pre[1:root_index+1],tin[:root_index])
        if right_num > 0:
            root.right = self.reConstructBinaryTree(pre[root_index+1:],tin[root_index+1:])
        return root
