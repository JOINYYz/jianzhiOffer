# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        tmp = s[:n]
        s = s[n:]
        s = s+tmp
        return s
