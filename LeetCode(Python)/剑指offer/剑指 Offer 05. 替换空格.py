class Solution:
    def replaceSpace(self, s: str) -> str:
        if not s:
            return ""
        
        return "%20".join(s.split(" "))

