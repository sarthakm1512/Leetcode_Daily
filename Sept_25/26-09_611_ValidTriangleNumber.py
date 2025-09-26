#Question Link: https://leetcode.com/problems/valid-triangle-number/description/?envType=daily-question&envId=2025-09-26
"""
611. Valid Triangle Number

Problem Statement: Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

Example 1:
Input: nums = [2,2,3,4]
Output: 3
Explanation: Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3

Example 2:
Input: nums = [4,2,3,4]
Output: 4
 
Constraints:
* 1 <= nums.length <= 1000
* 0 <= nums[i] <= 1000
"""

from typing import List

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort() #Step 1: Sort Array
        n = len(nums)
        count = 0

        #Step 2: Fix the largest side nums[k]
        for k in range(n - 1, 1, -1): #from last index down to 2
            i, j = 0, k - 1
            #Step 3: Two-pointer search
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    #Valis triangle found, all pairs (i...j-1, j) works
                    count += (j - i)
                    j -= 1
                else:
                    i += 1
        return count
