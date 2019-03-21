class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        root = TreeNode(pre[0])
        root_index = tin.index(pre[0])  # 用前序和中序的根节点来确定左右子树范围
        right_num = len(tin)- root_index -1 #记录根节点右边的节点数
        if root_index > 0: # 根节点左边不为空
            root.left = self.reConstructBinaryTree(pre[1:root_index+1],tin[:root_index]) #这里注意self,否则无法递归
        if right_num > 0:  # 根节点右边不为空
            root.right = self.reConstructBinaryTree(pre[root_index+1:],tin[root_index+1:])
        return root
