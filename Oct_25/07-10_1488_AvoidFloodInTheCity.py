#Question Link: https://leetcode.com/problems/avoid-flood-in-the-city/?envType=daily-question&envId=2025-10-08
"""
1488. Avoid Flood in The City

Problem Statement: Your country has an infinite number of lakes. Initially, all the lakes are empty, but when it rains over the nth lake, the nth lake becomes full of water. If it rains over a lake that is full of water, there will be a flood. Your goal is to avoid floods in any lake.

Given an integer array rains where:
- rains[i] > 0 means there will be rains over the rains[i] lake.
- rains[i] == 0 means there are no rains this day and you can choose one lake this day and dry it.

Return an array ans where:
- ans.length == rains.length
- ans[i] == -1 if rains[i] > 0.
- ans[i] is the lake you choose to dry in the ith day if rains[i] == 0.

If there are multiple valid answers return any of them. If it is impossible to avoid flood return an empty array.
Notice that if you chose to dry a full lake, it becomes empty, but if you chose to dry an empty lake, nothing changes.

Example 1:
Input: rains = [1,2,3,4]
Output: [-1,-1,-1,-1]
Explanation: After the first day full lakes are [1]
After the second day full lakes are [1,2]
After the third day full lakes are [1,2,3]
After the fourth day full lakes are [1,2,3,4]
There's no day to dry any lake and there is no flood in any lake.

Example 2:
Input: rains = [1,2,0,0,2,1]
Output: [-1,-1,2,1,-1,-1]
Explanation: After the first day full lakes are [1]
After the second day full lakes are [1,2]
After the third day, we dry lake 2. Full lakes are [1]
After the fourth day, we dry lake 1. There is no full lakes.
After the fifth day, full lakes are [2].
After the sixth day, full lakes are [1,2].
It is easy that this scenario is flood-free. [-1,-1,1,2,-1,-1] is another acceptable scenario.

Example 3:
Input: rains = [1,2,0,1,2]
Output: []
Explanation: After the second day, full lakes are  [1,2]. We have to dry one lake in the third day.
After that, it will rain over lakes [1,2]. It's easy to prove that no matter which lake you choose to dry in the 3rd day, the other one will flood.
 
Constraints:
* 1 <= rains.length <= 10^5
* 0 <= rains[i] <= 10^9
"""

from typing import List
import bisect  # for binary search

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        ans = [-1] * n  # final answer
        full_lakes = {}  # lake -> last day it got rain
        dry_days = []    # list of indices (days we can dry lakes)

        for i, lake in enumerate(rains):
            if lake == 0:
                # It's a dry day, add index to available dry days
                dry_days.append(i)
                ans[i] = 1  # placeholder (we can change later)
            else:
                # It rains on 'lake'
                if lake in full_lakes:
                    # Find a dry day after the lake was last filled
                    last_rain = full_lakes[lake]
                    idx = bisect.bisect_right(dry_days, last_rain)
                    if idx == len(dry_days):
                        # No available dry day → flood unavoidable
                        return []
                    
                    # Use that dry day to dry this lake
                    dry_day = dry_days[idx]
                    ans[dry_day] = lake  # we dry this specific lake
                    dry_days.pop(idx)    # remove that day from available ones

                # Update this lake's last rain day
                full_lakes[lake] = i

                # On rainy day, always -1 in answer
                ans[i] = -1

        return ans
