class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 1

        arr = [(s[0], -1)]
        if s[0] == s[1]:
            arr.append((s[0:2], -1))
        arr.append((s[1], 0))

        for i in range(2, len(s)):
            n = len(arr) - 1
            if s[i] == arr[n][0]:
                arr.append((arr[n][0] + s[i], arr[n][1]))
            if s[i] == s[arr[n][1]]:
                arr.append((s[arr[n][1]] + arr[n][0] + s[i], arr[n][1] - 1))
            n -= 1
            while len(arr[n][0]) > 1:
                if arr[n][1] != -1:
                    if s[i] == s[arr[n][1]]:
                        arr.append((s[arr[n][1]] + arr[n][0] + s[i], arr[n][1] - 1))
                n -= 1
            arr.append((s[i], i - 1))

        return len(arr)
