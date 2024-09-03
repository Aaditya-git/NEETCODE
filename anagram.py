'''
https://neetcode.io/problems/is-anagram
Solution : 
'''


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        string1 = list(s)
        string2 = list(t)
        res1 = ''.join(sorted(string1))
        res2 = ''.join(sorted(string2))
        if res1 == res2:
            return True
        else:
            return False
