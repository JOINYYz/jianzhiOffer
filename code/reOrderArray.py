# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        odd = []
        even = []
        for num in array:
            if num&(2-1) == 1: #用位与计算代替求余，判断奇
                odd.append(num)
            if num&(2-1) == 0: #用位与计算代替求余，判断偶
                even.append(num)
        return odd+even
        
