# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        l = s.split(' ')
        left = 0
        right = len(l)-1
        while(left<right):
            l[left],l[right] = l[right],l[left] #从头尾开始用指针对换
            left+=1
            right-=1
        return ' '.join(l)


#最简单这种
    def ReverseSentence(self, s):
        # write code here
        l = s.split(' ')
        return ' '.join(l[::-1])
