class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""; # result is a string
        for i in range(len(strs)):
            res += str(len(strs[i])) + "#" + strs[i]
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j=i # Use j to find the index of the "#"
            while s[j] != "#":
                j+=1
            str_length = int(s[i:j])
            res.append(s[j+1:j+1+str_length])
            i = j+1+str_length
        return res
        
