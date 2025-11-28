class Anagram:
    def __init__(self, word: str):
    
        self.word = word

    @staticmethod
    def are_anagrams(str1: str, str2: str) -> bool:

        str1_cleaned = str1.replace(" ", "").lower()
        str2_cleaned = str2.replace(" ", "").lower()

    
        return sorted(str1_cleaned) == sorted(str2_cleaned)

    def match(self, word_list):
        """Find all anagrams of the stored word in the given list."""
        return [word for word in word_list if self.are_anagrams(self.word, word)]