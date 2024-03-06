class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
          print("false")
        else:
          return sorted(s) == sorted(t)
          