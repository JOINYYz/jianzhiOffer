# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        small = 0
        big = len(array)-1
        while small<big :
            sum = array[small]+array[big]
            if sum == tsum:
            # 把两个数字想成矩形的两条边，当两条边越接近，面积越大（乘积越大）。
            # 从两头向中间进行查找,找到的第一个组合一定是边差距最大的，所以乘积最小。
                return [array[small],array[big]]
            elif sum < tsum:
                small+=1
            else:
                big-=1
        return []
                
            
