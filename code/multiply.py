# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        B = [1] * len(A)
        for i in range(len(B)):
            for j in range(len(A)):
                if i != j:
                    B[i] *= A[j]
                else:
                    continue
        return B
        
    #解法二
    分成A[0]*..*A[i-1]和A[i+1]*...*A[n-1]两组
            
