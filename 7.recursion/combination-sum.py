def combinationSum(self, candidates, target: int):
    solution_set = set()
    self._combinationSum([], candidates, target, solution_set)
    return solution_set


def _combinationSum(self, current_nums, candidates, target, solution_set):
    for num in candidates:
        if target - num > 0:
            new_nums = current_nums[:]
            new_nums.append(num)
            self._combinationSum(new_nums, candidates, target - num, solution_set)
        elif target - num == 0:
            new_nums = current_nums[:]
            new_nums.append(num)
            new_nums.sort()
            solution_set.add(tuple(new_nums))