class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        prod = 1
        i = 0
        j = 0
        n = len(nums)
        while j < n:
            prod = prod * nums[j]
            while prod >= k and i <= j:
                prod = prod // nums[i]
                i += 1
            count += j - i + 1
            j += 1
        return count