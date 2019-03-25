# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        if exponent == 0:
            return 1
        else:
            result = base
            for i in range(abs(exponent)-1): #注意要-1
                result = result*base
            if exponent < 0 :
                result = 1.0/result
            return result
#第二种解法
