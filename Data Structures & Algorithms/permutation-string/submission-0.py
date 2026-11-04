class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sub_len = len(s1)
        for index in range(0, len(s2)-sub_len+1,1):
            sub = s2[index:index+sub_len]
            count_s1 = [0]*26
            count_s2 = [0]*26
            for i in range(sub_len):
                count_s1[ord(s1[i])-ord('a')] +=1
                count_s2[ord(sub[i])-ord('a')] +=1
            if count_s1 == count_s2:
                return True
        return False

            