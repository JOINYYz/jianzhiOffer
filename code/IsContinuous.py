# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        
        if numbers == []:
            return False
        
        numbers = sorted(numbers)
        count0 = 0
        if self.hasKing(numbers): #有大小王
            for i in range(len(numbers)-1):
                if numbers[i] == 0: #计算王的数量
                    count0 += 1
                else:
                    gap = numbers[i+1] - numbers[i]
                    if gap == 0: # 有重复的非0数字
                        return False
                    elif  gap ==1 :
                        continue
                    elif gap-1 > count0: #王的数量不够替补
                        return False
                    else: #减掉已经替补了的王
                        count0 = count0-gap+1
            return True
        else: #没有大小王
            if numbers[-1] - numbers[0] == 4:
                return True
            else:
                return False
                        
    def hasKing(self,numbers):
        for num in numbers:
            if num == 0:
                return True
        return False
