class Solution:
    def longestCommonPrefix(self, strs):
        min_len = min(len(word) for word in strs)
        prefix = ""

        for i in range(min_len):
            ch = strs[0][i]

            for word in strs:
                if word[i] != ch:
                    return prefix

            prefix += ch

        return prefix