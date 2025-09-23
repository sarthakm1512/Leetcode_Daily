#Question Link: https://leetcode.com/problems/compare-version-numbers/description/?envType=daily-question&envId=2025-09-23
"""
165. Compare Version Numbers

Problem Statement: Given two version strings, version1 and version2, compare them. A version string consists of revisions separated by dots '.'. The value of the revision is its integer conversion ignoring leading zeros.
To compare version strings, compare their revision values in left-to-right order. If one of the version strings has fewer revisions, treat the missing revision values as 0.

Return the following:
- If version1 < version2, return -1.
- If version1 > version2, return 1.
- Otherwise, return 0.
 
Example 1:
Input: version1 = "1.2", version2 = "1.10"
Output: -1
Explanation:
version1's second revision is "2" and version2's second revision is "10": 2 < 10, so version1 < version2.

Example 2:
Input: version1 = "1.01", version2 = "1.001"
Output: 0
Explanation:
Ignoring leading zeroes, both "01" and "001" represent the same integer "1".

Example 3:
Input: version1 = "1.0", version2 = "1.0.0.0"
Output: 0
Explanation:
version1 has less revisions, which means every missing revision are treated as "0".

Constraints:
* 1 <= version1.length, version2.length <= 500
* version1 and version2 only contain digits and '.'.
* version1 and version2 are valid version numbers.
* All the given revisions in version1 and version2 can be stored in a 32-bit integer.
"""

from typing import List

class Solution:
  def compareVersion(self, version1: str, version2: str) -> int:
    #Step 1: Split both versions into parts
    v1 = version1.split(".")
    v2 = version2.split(".")
    
    #Step 2: Convert each part into integers (removes leading 0's automatically)
    v1 = [int(x) for x in v1]
    v2 = [int(x) for x in v2]
    
    #Step 3: Pad the shorter list with zeros so they are the same length
    n = max(len(v1), len(v2))
    while len(v1) < n:
      v1.append(0)
    while len(v2) < n:
      v2.append(0)
    
    #Step 4: Compare element by element
    for i in range(n):
      if v1[i] < v2[i]:
        return -1
      elif v1[i] > v2[i]:
        return 1
    
    #Step 5: if all are equal
    return 0
