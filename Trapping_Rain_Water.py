'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        res = 0
        mid = height.index(max(height))
        
        for left in range(0,mid):
            if height[left] > height[left+1]:
                res += height[left] - height[left+1]
                height[left+1] = height[left]
                
        for right in range(len(height)-1, mid, -1):
            if height[right] > height[right-1]:
                res += height[right] - height[right-1]
                height[right-1] = height[right]
                
        return res
