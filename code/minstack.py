# -*- coding:utf-8 -*-
class Solution:
    min_stack = []
    data = []
    
    def push(self, node):
        # write code here
        self.data.append(node)
        if len(self.min_stack)==0 or node < self.min_stack[-1]: #倒数第一个元素
            self.min_stack.append(node)
        else:
            self.min_stack.append(self.min_stack[-1])
            
    def pop(self):
        # write code here
         if len(self.data) > 0:
            self.data.pop()
            self.min_stack.pop()
            
    def top(self):
        # write code here
        return self.data[-1]
        
    def min(self):
        # write code here
        return self.min_stack[-1]
