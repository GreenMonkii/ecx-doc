import re


class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Use regex to cleanup non-alphanumeric characters
        cleaned = re.sub(r"[^A-Za-z0-9]", "", s).lower()

        # Check that the cleaned string is equal to its reverse
        return cleaned == cleaned[::-1]
