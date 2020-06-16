from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        N = len(candidates)
        ans = []

        def backtrack(cur_target, current_idx, current):
            if cur_target < 0:
                return
            elif cur_target == 0:
                ans.append(current)
                return

            for i in range(current_idx, N):
                backtrack(cur_target - candidates[i], i, current + [candidates[i]])

        backtrack(target, 0, [])
        return ans