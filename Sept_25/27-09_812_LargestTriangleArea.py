#Question Link: https://leetcode.com/problems/largest-triangle-area/description/?envType=daily-question&envId=2025-09-27
"""
812. Largest Triangle Area

Problem Statement: Given an array of points on the X-Y plane points where points[i] = [x_i, y_i], return the area of the largest triangle that can be formed by any three different points.
Answers within 10^(-5) of the actual answer will be accepted.

Example 1:
Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2.00000

Example 2:
Input: points = [[1,0],[0,0],[0,1]]
Output: 0.50000
 
Constraints:
* 3 <= points.length <= 50
* -50 <= x_i, y_i <= 50
* All the given points are unique.
"""

from typing import List

class Solution:
  def largestTriangleArea(self, points: List[List[int]]) -> float:
    n = len(points)
    max_area = 0.0
    
    #Step 1: Try all combinations of 3 points
    for i in range(n):
      for j in range(i+1, n):
        for k in range(j+1, n):
          x1, y1 = points[i]
          x2, y2 = points[j]
          x3, y3 = points[k]
          
          #Step 2: Apply the area formula
          area = abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2
          
          #Step 3: Track max area
          max_area = max(max_area, area)

    return max_area
