# -*- coding:utf-8 -*-
class Solution:
    def bisearch(self,data,k):
        low = 0
        high = len(data)-1        
        while low<=high:
            mid = int((low+high)/2)
            if data[mid]==k:
                return mid                
            elif data[mid]<k:
                low = mid+1
            else:
                high = mid-1                
        return None
                    
    def GetNumberOfK(self, data, k):
        # write code here
        mid = self.bisearch(data,k)
        if mid is not None:
            ptr = mid-1
            count = 1
            while ptr!=-1:
                if data[ptr] == k:
                    count+=1
                    ptr-=1
                else:
                    break
            ptr = mid+1
            while ptr!=len(data):
                if data[ptr] == k:
                    count+=1
                    ptr+=1
                else:
                    break
            return count
        else:
            return 0
