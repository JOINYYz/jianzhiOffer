# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if k>len(tinput) or k ==0: #要注意k的特殊情况
            return []
        k_num = tinput[:k]
        for item in tinput[k:]:
            k_max = max(k_num)
            if item < k_max:
                i = k_num.index(k_max)
                k_num[i]=item
        return sorted(k_num)
