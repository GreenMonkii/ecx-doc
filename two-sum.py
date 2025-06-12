from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Create a dictionary to store numbers and their indices
        num_map = {}

        for index, num in enumerate(nums):
            complement = target - num

            # Check if the complement exists in the map
            if complement in num_map:
                # num_map[complement] gives the index of the complement
                return [num_map[complement], index]

            # Store the index of the current number for future lookups
            num_map[num] = index

        # Return an empty list if no solution is found
        return []
