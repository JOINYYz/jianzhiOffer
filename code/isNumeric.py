# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        isAllowDot = True # ‘.’标记
        isAllowE = True # ‘Ee’标记
        for i in range(len(s)):
        # 列出了所有不符合的条件，则成功遍历完为True
            if s[i] in "+-" and (i==0 or s[i-1] in "eE") and i < len(s)-1: # 判断‘+-’符号位置
                continue
            elif isAllowDot and s[i] == ".": # 判断‘.’是否允许出现
                isAllowDot = False
                if i >= len(s)-1 or s[i+1] not in "0123456789":
                    return False
            elif isAllowE and s[i] in "Ee": # 判断‘Ee’是否允许出现,且在‘Ee’出现过后不允许出现‘.’
                isAllowDot = False
                isAllowE = False
                if i >= len(s)-1 or s[i+1] not in "0123456789+-":
                    return False
            elif s[i] not in "0123456789": # 判断字符是否为非数字，去掉ab..等
                return False
        return True

--------------------------------------------------------------------------------
作者：goddaniel、自己添加了注释
来源：CSDN 
原文：https://blog.csdn.net/u010005281/article/details/80232379 

