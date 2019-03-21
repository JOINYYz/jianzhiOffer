# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
    '''
    原有数组已升序排序，翻转时选取前几个数据翻转，因此翻转后最小的数一定在中间，
    在中间找到第i个数比第i+1个数大的位置，则第i+1个数就是最小的数
    '''
        # write code here
        if len(rotateArray) == 0:
            return 0
        else:
            for i in range(len(rotateArray)-1): # 注意数组下标，不要溢出
                if rotateArray[i] > rotateArray[i+1]:
                    return rotateArray[i+1]
