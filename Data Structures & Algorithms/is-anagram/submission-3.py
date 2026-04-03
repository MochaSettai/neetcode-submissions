'''
242. Valid Anagram

Time Complexity: O(n)
Space Complexity: O(n)
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return Counter(s) == Counter(t)  # does the same thing as the code below but is more concise
    
        if len(s) != len(t):
            return False
        mapS, mapT = {}, {}

        # inserting words to maps
        for i in range(len(s)):
            mapS[s[i]] = 1 + mapS.get(s[i], 0)
            mapT[t[i]] = 1 + mapT.get(t[i], 0)
        # comparing the maps
        for c in mapS:
            if mapS[c] != mapT.get(c, 0):
                return False

        return True