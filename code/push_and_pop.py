# -*- coding:utf-8 -*-
class Solution:
    stack1=[]
    stack2=[]
    def push(self, node):
        # write code here
        self.stack1.append(node)
    def pop(self):
        # return xx
        while(len(self.stack1) > 1):
            self.stack2.append(self.stack1.pop())
        aim = self.stack1.pop()
        while(len(self.stack2) > 0):
            self.stack1.append(self.stack2.pop())       
        return aim
