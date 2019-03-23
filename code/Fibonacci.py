# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        f1 = 0
        f2 = 1 #自定义第0项和第1项
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            for i in range(2,n+1):
                fn = f1+f2
                f1,f2 = f2,fn                
            return fn
              
