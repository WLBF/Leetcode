class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        acc = [0] * length
        bcc = [0] * length
        acc[0] = nums[0]
        bcc[-1] = nums[-1]
        for idx in range(1, length - 1):
            acc[idx] = acc[idx - 1] * nums[idx]
            bcc[-1 - idx] = bcc[-idx] * nums[-1 - idx]
            
        ans = [0] * length
        ans[0] = bcc[1]
        ans[-1] = acc[-2]
        for idx in range(1, length - 1):
            ans[idx] = acc[idx - 1] * bcc[idx + 1]
            
        return ans
