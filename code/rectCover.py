# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        r1 = 1
        r2 = 2
        if number < 3:
            return number
        else:
            for i in range(3,number+1):
                fn = r1+r2 # 横着放时，必须同时横放两个才不会出现覆盖
                r1,r2 = r2,fn
            return fn
        
