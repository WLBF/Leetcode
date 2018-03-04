class Solution:
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        len1 = len(s1)
        len2 = len(s2)
        dp = [[0 for j in range(len2 + 1)] for i in range(len1 + 1)]
        for i in reversed(range(len1)):
            dp[i][len2] = dp[i + 1][len2] + ord(s1[i])
        for j in reversed(range(len2)):
            dp[len1][j] = dp[len1][j + 1] + ord(s2[j])
        for i in reversed(range(len1)):
            for j in reversed(range(len2)):
                if s1[i] != s2[j]:
                    dp[i][j] = min(
                        dp[i][j + 1] + ord(s2[j]),
                        dp[i + 1][j] + ord(s1[i]),
                        dp[i + 1][j + 1] + ord(s1[i]) + ord(s2[j]))
                else:
                    dp[i][j] = dp[i + 1][j + 1]
        return dp[0][0]
