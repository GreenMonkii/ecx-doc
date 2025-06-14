from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Use a defaultdict to group anagrams so new keys automatically get an empty list.
        anagram_map = defaultdict(list)

        for word in strs:
            # Anagrams will have identical sorted signatures.
            sorted_word = "".join(sorted(word))

            # Append the original word to the list associated with its sorted signature.
            anagram_map[sorted_word].append(word)

        # The values of the map are the lists of grouped anagrams.
        return list(anagram_map.values())
