# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        count ={}
        for num in numbers: #在则+1，不在则创建并=1
            if num in count:
                count[num]+=1
            else:
                count[num]=1
        for key,value in count.items():
            if value > len(numbers)/2:
                return key
        return 0
