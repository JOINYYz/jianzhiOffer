# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if len(s)==0:
            return -1
        else:
            s_dict={}
            for char in s: #str可直接遍历
                if char not in s_dict:
                    s_dict[char] = 1
                else:
                    s_dict[char] += 1
            for char in s: 
                if s_dict[char]==1:
                    return s.find(char) #返回char开始的索引值
            return 0
