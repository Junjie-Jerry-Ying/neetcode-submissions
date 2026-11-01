class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        while (i<j):
            if (not 
                (
                (s[i]>='A' and s[i]<='Z') 
                or 
                (s[i]>='a' and s[i]<='z')
                or 
                (s[i]>='0' and s[i]<='9')
                )):
                i+=1
                continue
            if (not 
                (
                (s[j]>='A' and s[j]<='Z') 
                or 
                (s[j]>='a' and s[j]<='z')
                or 
                (s[j]>='0' and s[j]<='9')
                )):
                j-=1
                continue
            if (s[i].lower()!=s[j].lower()):
                return False
            i+=1
            j-=1
        return True