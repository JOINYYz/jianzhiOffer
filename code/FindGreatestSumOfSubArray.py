# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        sum = 0
        max = None
        for i in array:
            if sum <0:
                sum = i 
            else:
                sum = sum+i
            #要留下最大的和
            if sum > max:
                max = sum
        return max
