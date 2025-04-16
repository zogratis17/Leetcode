class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            key = [0] * 26
            for c in s:
                key[ord(c) - ord('a')] += 1
            anagrams[tuple(key)].append(s)
        
        return list(anagrams.values())

# Time Complexity (TC):
# Let:
# n = number of strings in the input list strs
# k = average length of each string

# Steps:
# Loop over each string → O(n)

# For each string:

# Creating and filling the frequency array → O(k)

# Converting it to a tuple → O(26) = constant time

# So total = O(n * k)

# ✅ Time Complexity = O(n * k)