# your code goes here!

class Anagram:

    def __init__(self, word):
        self.word_letter = sorted([letter for letter in word])

    def match(self, word_list):
        match_word_list = []

        for word in word_list:
            if sorted([letter for letter in word]) == self.word_letter:
                match_word_list.append(word)

        return match_word_list