class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        row_N = len(array)       
        col = len(array[0]) - 1
        if (row_N > 0 and col > 1):           # 至少要有一行和一列，才能进行循环
            row = 0
            while (row < row_N and col >= 0): # 遍历完所有行和列的时候终止循环
                if array[row][col] > target:
                    col -= 1
                elif array[row][col] < target:
                    row += 1
                else:
                    return True
            return False
        else:
            return False
