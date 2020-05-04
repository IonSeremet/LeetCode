from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(0, len(nums)):
        for j in range(0, len(nums)):
            if j == i: continue
            if nums[i] + nums[j] == target:
                return [i, j]


twoSum([2, 7, 11, 15], 13)
print(twoSum([2, 7, 11, 15], 13))
a={"valera":"destept",
   "ionut":"tare destept"}
print(a["valera"])