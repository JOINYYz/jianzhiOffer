# -*- coding:utf-8 -*-
class Solution:
    #求和公式
    def Sum_Solution(self, n):
        # write code here
        sum = 0.5 * n *(1+n)
        return sum
        
    #逻辑与的短路特性实现递归
    def Sum_Solution(self, n):
        # write code here
        result = n
        tmp = n>0 and Sum_Solution(n-1)
        result = n+tmp #True为1，False为0
        return result
