from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count element frequencies
        counts = Counter(nums)

        # Sort items by frequency in descending order and take the top k
        sorted_items = sorted(counts.items(), key=lambda item: item[1], reverse=True)

        # Extract the numbers from the top k items
        result = [item[0] for item in sorted_items[:k]]

        return result
