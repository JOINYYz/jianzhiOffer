class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        list_str = s.split(' ')
        new_str = '%20'.join(list_str)
        return new_str
