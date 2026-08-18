class Solution(object): 
    def lengthOfLongestSubstring(self, s): 
        """ 
        :type s: str 
        :rtype: int 
        """ 
 
        last_index = {} 
        res = 0 
        left = 0 

        for right in range(len(s)): 
            if s[right] in last_index: 
                left = max(left, last_index[s[right]] + 1) 
            last_index[s[right]] = right 
            res = max(res, right - left + 1) 

        return res