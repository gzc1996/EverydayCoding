'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''


class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        findindex = {}
        longsub = []
        
        
        for i,item in enumerate(s):
            # findindex[item] = i
            if item in longsub:
                if(len(longsub)>res):
                    res = len(longsub)
                for j,val in enumerate(longsub):
                    findindex[val] = j
                longsub = longsub[findindex[item]+1:]
                # print(longsub)
                longsub.append(item)
                findindex[item] = i
            else:
                longsub.append(item)
                findindex[item] = i
        # print(longsub)
        # print(res)
        return max(len(longsub),res)
        
        
class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result=0
        temp=[]
        for item in s:
            if item in temp:
                if len(temp)>result:
                    result=len(temp)
                temp=temp[temp.index(item)+1:]
                temp.append(item)
            else:
                temp.append(item)
        return max(len(temp),result)
