#Question Link: https://leetcode.com/problems/trapping-rain-water-ii/?envType=daily-question&envId=2025-10-04
"""
407. Trapping Rain Water II

Problem Statement: Given an m x n integer matrix heightMap representing the height of each unit cell in a 2D elevation map, return the volume of water it can trap after raining.

Example 1:
Input: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
Output: 4
Explanation: After the rain, water is trapped between the blocks.
We have two small ponds 1 and 3 units trapped.
The total volume of water trapped is 4.

Example 2:
Input: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
Output: 10
 
Constraints:
* m == heightMap.length
* n == heightMap[i].length
* 1 <= m, n <= 200
* 0 <= heightMap[i][j] <= 2 * 10^4
"""

import heapq
from typing import List

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        # Edge case: if matrix is too small, no water can be trapped
        if not heightMap or not heightMap[0]:
            return 0

        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        heap = []  # min-heap for boundary cells

        # Step 1: Push all boundary cells into heap
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = True

        trapped_water = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 4 neighbors

        # Step 2: BFS with heap
        while heap:
            height, x, y = heapq.heappop(heap)

            # Explore neighbors
            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                # Check boundaries and if visited
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True

                    # If neighbor is lower, water is trapped
                    trapped_water += max(0, height - heightMap[nx][ny])

                    # Push the "effective height" into heap
                    heapq.heappush(heap, (max(height, heightMap[nx][ny]), nx, ny))

        return trapped_water
