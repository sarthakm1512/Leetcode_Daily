#Question Link: https://leetcode.com/problems/minimum-score-triangulation-of-polygon/?envType=daily-question&envId=2025-09-29
"""
1039. Minimum Score Triangulation of Polygon

Problem Statement: You have a convex n-sided polygon where each vertex has an integer value. You are given an integer array values where values[i] is the value of the ith vertex in clockwise order.
Polygon triangulation is a process where you divide a polygon into a set of triangles and the vertices of each triangle must also be vertices of the original polygon. Note that no other shapes other than triangles are allowed in the division. This process will result in n - 2 triangles.
You will triangulate the polygon. For each triangle, the weight of that triangle is the product of the values at its vertices. The total score of the triangulation is the sum of these weights over all n - 2 triangles.
Return the minimum possible score that you can achieve with some triangulation of the polygon.

Example 1:
Input: values = [1,2,3]
Output: 6
Explanation: The polygon is already triangulated, and the score of the only triangle is 6.

Example 2:
Input: values = [3,7,4,5]
Output: 144
Explanation: There are two triangulations, with possible scores: 3*7*5 + 4*5*7 = 245, or 3*4*5 + 3*4*7 = 144.
The minimum score is 144.

Example 3:
Input: values = [1,3,1,4,1,5]
Output: 13
Explanation: The minimum score triangulation is 1*1*3 + 1*1*4 + 1*1*5 + 1*1*1 = 13.

Constraints:
* n == values.length
* 3 <= n <= 50
* 1 <= values[i] <= 100
"""

from typing import List

class Solution:
  def minScoreTriangulation(self, values: List[int]) -> int:
    n = len(values)
    
    #dp[i][j] will store the minimum triangulation score for polygon from i to j
    dp = [[0] * n for _ in range(n)]

    #We fill the dp table for increasing interval lengths
    for length in range(3, n+1): #length must be at least 3 to form triangle
      for i in range(n - length + 1):
        j = i + length - 1
        dp[i][j] = float('inf') #start with infinity
        #Try choosing every point k in between i & j as third vertex
        for k in range(i+1, j):
          cost = values[i] * values[k] * values[j] + dp[i][k] + dp[k][j]
          dp[i][j] = min(dp[i][j], cost)
          
    return dp[0][n-1] #minimum score for whole polygon
