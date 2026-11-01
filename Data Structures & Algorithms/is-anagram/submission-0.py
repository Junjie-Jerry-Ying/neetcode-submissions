class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_seen = {}
        for l in s:
            if l not in s_seen:
                s_seen[l] = 1
            else:
                s_seen[l] +=1
        l_seen = {}
        for l in t:
            if l not in l_seen:
                l_seen[l] = 1
            else:
                l_seen[l] +=1
        if s_seen == l_seen:
            return True
        else:
            return False