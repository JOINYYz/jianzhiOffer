# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        stack = []
        for item in pushV:
            stack.append(item)
            while len(stack)!=0 and stack[-1]==popV[0]:
                stack.pop()
                popV.pop(0)
        if len(stack)==0:  #等于 if not stack
            return True
        else:
            return False
