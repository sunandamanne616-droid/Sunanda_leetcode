class Solution(object):
    def firstUniqChar(self, s):
        seen={}
        for ch in s:
            seen[ch]=seen.get(ch,0)+1
        for ch in range(len(s)):
            if seen[s[ch]]==1:
                return ch
        return -1

        