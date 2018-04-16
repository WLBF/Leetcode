class Solution:
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxLen = 0
        for i in range(len(nums)):
            length = 0
            idx = i
            nextNum = nums[idx]
            while nextNum >= 0:
                length += 1
                nums[idx] = -1
                idx = nextNum
                nextNum = nums[idx]

            maxLen = max(length, maxLen)
        return maxLen
