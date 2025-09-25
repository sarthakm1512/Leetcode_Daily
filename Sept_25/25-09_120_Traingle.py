#Question Link: https://leetcode.com/problems/triangle/description/?envType=daily-question&envId=2025-09-25
"""
120. Triangle

Problem Statement: Given a triangle array, return the minimum path sum from top to bottom.
For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

Example 1:
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11.

Example 2:
Input: triangle = [[-10]]
Output: -10

Constraints:
* 1 <= triangle.length <= 200
* triangle[0].length == 1
* triangle[i].length == triangle[i - 1].length + 1
* -10^4 <= triangle[i][j] <= 10^4
"""

from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        #start from second last row and go upward
        for row in range(len(triangle) -2, -1, -1):
            for col in range(len(triangle[row])):
                #Update each cell with its value + min of two possible children
                triangle[row][col] += min(triangle[row + 1][col], triangle[row + 1][col + 1])

        #The top element now contains the minimum path sum
        return triangle[0][0]
