# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        if s == '':
            return 0 
        else:
            s = s.strip() # 去掉空格
            tmp,num,flag = 0,0,1 # flag是符号标记，正为1，负为-1
            # 先处理符号
            if s[0] == '-':
                flag = -1
                s = s[1:]
            elif s[0] == '+':
                s = s[1:]
            # 开始遍历，遇到非数字的都为0
            for c in s:
                if c >= '0' and c <= '9':
                    tmp = ord(c)-ord('0') # ord将字符转成ascii码
                    num = num*10 + tmp # num*10左移
                else:
                    return 0
            return flag*num # 最后要带上符号，正负数
                       
