class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        n = len(timeSeries)
        if n <= 0 or duration <=0:
            return 0

        time = 0
        for i in range(n-1):
            if timeSeries[i] + duration <= timeSeries[i+1]:
                time += duration
            else:
                time += timeSeries[i+1] - timeSeries[i]
        # 加上最后一个区间
        return time + duration
