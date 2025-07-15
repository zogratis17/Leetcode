class Solution:
    def isValid(self, word: str) -> bool:
        return re.search(r"(?i)(?=^.*[b-df-hj-np-tv-z])(?=.*[aieou])^[a-z0-9]{3,}$", word) is not None