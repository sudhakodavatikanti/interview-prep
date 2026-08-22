class Solution:
    def count_vowels(self, s: str) -> int:
        vowels = set("aeiouAEIOU")
        count = 0
        for char in s:
            if char in vowels:
                count += 1

        return count