# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        f1 = 1
        f2 = 2
        sum = f1 + f2
        if number < 3:
            return number
        else:
            for i in range(3,number+1):
                fn = sum + 1 #第一次选择跳m阶后，剩下的是求跳n-m阶的跳法，再加上可以一次跳n阶的次数1
                sum = sum + fn
            return fn
