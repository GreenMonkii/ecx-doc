class NumArray:
    def __init__(self, nums: list[int]):
        # Initialize the input list of numbers for sum range queries.
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        # Calculates the sum of elements from 'left' to 'right' (inclusive).
        # The slice [left : right + 1] ensures 'right' index is included.
        return sum(self.nums[left : right + 1])
