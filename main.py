class Solution:
    def lengthOfLongestSubstring(self, s):
        list_s = list(s)
        check = []
        seek_max = []
        i = 0

        if bool(s) == True: # 判別是否為空字串
            for i in range(len(list_s)):
                result = []
                for alph in list_s[i:]:
                    result.append(alph)
                # print(result)

                if len(result )!= len(set(result)):
                    for alph2 in result:
                        if alph2 not in check:
                            check.append(alph2)
                        else:
                            del result[result.index(alph2):]
                            seek_max.append(len(check))
                            check =[]
                else:
                    seek_max.append(len(result))
                # print(seek_max)
            max_result = max(seek_max)
            
        else:
            max_result = 0

        print(max_result)
        return max_result


solution = Solution()
solution.lengthOfLongestSubstring("abcabcbb")

# Input: s = "abcabcbb"
# Output: 3

# Input: s = "bbbbb"
# Output: 1

# Input: s = "pwwkew"
# Output: 3