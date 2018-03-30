class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        nums.sort()
        idx = 1
        while idx < len(nums):
            if nums[idx] == nums[idx - 1]:
                ans.append(nums[idx])
                idx += 2
            else:
                idx += 1

        return ans
