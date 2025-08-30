class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return True if sorted(s) == sorted(t) else False


s = "anagram"
t = "nagaram"
sol = Solution()
print(sol.isAnagram(s, t))

# n(log n) complexity because of the sorted function