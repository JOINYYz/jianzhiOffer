# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        small = 1
        big = 2
        len = (tsum+1)/2
        tmp = [1,2]
        res = []
        while(small<len and small<big):
            if sum(tmp) == tsum:
                res.append(tmp[:])
                big+=1
                tmp.append(big)
            elif sum(tmp) < tsum:
                big+=1
                tmp.append(big)
            else:
                tmp.pop(0)
                small+=1
        return res
        
