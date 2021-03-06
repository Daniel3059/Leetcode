#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
       
        # build has map : character and how often it appears
        count = collections.Counter(s)
        # find the index 
        for idx , str1 in enumerate(s):
            if count[str1] == 1:
                return idx 

        return -1
# TC: O(N) we go through the string of length N two times
# SC: O(1) English alphabet contains 26 letters 

        
# @lc code=end

