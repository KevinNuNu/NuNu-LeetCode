class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        ret = []

        start = 0
        end = 0
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                if end - start >= 2:
                    ret.append([start, end])
                start = i
            end = i
            
        if end - start >= 2:
            ret.append([start, end])
        
        return ret