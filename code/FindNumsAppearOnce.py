# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        if array == None:
            return
            
        #array中每个数字异或
        tmp = 0
        for i in array:
            tmp ^= i
        
        #获取tmp中最低位1的位置
        pos = 0
        while(tmp&1)==0:
            tmp>>=1
            pos+=1
            
        #按pos位置是否为1分组进行异或
        a=b=0       
        for i in array:
            if i>>(pos)&1 :
                a = a^i
            else:
                b = b^i
        return [a,b]
        
            
