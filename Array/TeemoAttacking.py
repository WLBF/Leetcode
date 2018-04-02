class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if timeSeries == []:
            return 0

        ans = timeSeries[-1] - timeSeries[0] + duration

        for idx in range(1, len(timeSeries)):
            blank = timeSeries[idx] - timeSeries[idx - 1] - duration
            if blank > 0:
                ans -= blank

        return ans
