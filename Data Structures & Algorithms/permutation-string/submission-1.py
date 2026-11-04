class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sub_len = len(s1)

        if sub_len > len(s2):
            return False

        count_s1 = [0] * 26
        count_s2 = [0] * 26

        # Count s1 and the first complete window in s2.
        for i in range(sub_len):
            count_s1[ord(s1[i]) - ord('a')] += 1
            count_s2[ord(s2[i]) - ord('a')] += 1

        if count_s1 == count_s2:
            return True

        # Slide the window one character at a time.
        for right in range(sub_len, len(s2)):
            incoming = s2[right]
            outgoing = s2[right - sub_len]

            count_s2[ord(incoming) - ord('a')] += 1
            count_s2[ord(outgoing) - ord('a')] -= 1

            if count_s1 == count_s2:
                return True

        return False