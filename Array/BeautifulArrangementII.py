class Solution:
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        ans = list(range(1, n - k))
        
        m = 0
        while m < k / 2:
            ans.append(n - k + m)
            ans.append(n - m) 
            m += 1
            
        if n - k + m == n - m:
            ans.append(n - k + m)
            
        return ans
