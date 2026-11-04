class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        sub = {}
        max_len = 0
        max_char_count = 0
        l_index = 0
        r_index = 0
        while r_index < len(s):
            # Add the new character
            r_char = s[r_index]
            sub[r_char] = sub.get(r_char, 0)+1
            # Update which character is the max
            max_char_count = max(sub.values())
            #Check if violate k replacement
            while (r_index - l_index - max_char_count >= k):
                l_char = s[l_index]
                sub[l_char]-=1
                max_char_count = max(sub.values())
                l_index+=1
            max_len = max(max_len, r_index - l_index + 1)
            r_index+=1
        return max_len