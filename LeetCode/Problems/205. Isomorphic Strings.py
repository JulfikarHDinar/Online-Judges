class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict1 = {}
        for i in range(len(s)):
            if s[i] not in dict1.keys() and t[i] not in dict1.values():
                dict1.update({s[i]:t[i]})
            elif s[i] in dict1.keys() and dict1[s[i]] == t[i]:
                continue
            else:
                return False
        return True