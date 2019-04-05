# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        result = []
        self.place(ss,result,'')
        return sorted(list(set(result)))
        
    def place(self,ss,result,path):
        if not ss: #ss经过切分后变成''长度为0的字符串，而不是None
            result.append(path)
        else:
            for i in range(len(ss)):
                self.place(ss[:i]+ss[i+1:],result,path+ss[i])
                '''
                ss[:i]+ss[i+1:]是本次的递归，把除了第i个元素以外的元素，全部都给下一层递归
                path + ss[i]是在字符串中，选择了第i个元素加入path
                比如，全部元素是abc，第i个元素是b，那么b加入了path，ac就传到下一个递归  
                '''
                
