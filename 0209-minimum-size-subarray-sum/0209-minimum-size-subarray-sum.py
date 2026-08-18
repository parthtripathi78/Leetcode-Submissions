class Solution(object):
    def minSubArrayLen(self, target, nums):

        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        res = float('inf')
        total = 0
        left = 0

        for right in range(n):
            total = total + nums[right]

            while total >= target:
                res = min(res, right - left + 1)
                total = total - nums[left]
                left = left + 1

        if res == float('inf'):
            return 0

        return res