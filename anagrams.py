import requests
import string
import collections
from typing import List


class anagramDict:

    def __init__(self, words: List[str]):
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
                  43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        self.lowercaseToPrimes = dict(zip(string.ascii_lowercase, primes))
        self.asciiSumToWords = collections.defaultdict(list)
        for word in words:
            lowered = word.lower()
            asciiValue = self.hashLetters(lowered)
            self.asciiSumToWords[asciiValue].append(word)

    def hashLetters(self, word: str) -> int:
        product = 1
        for letter in word:
            if letter in self.lowercaseToPrimes:
                product *= self.lowercaseToPrimes[letter]
        return product

    def getAnagram(self, letters: str) -> List[str]:
        asciiValue = self.hashLetters(letters.lower())
        if asciiValue not in self.asciiSumToWords:
            return []
        return self.asciiSumToWords[asciiValue]


def main():
    url = 'https://raw.githubusercontent.com/lad/words/master/words'
    stuff = requests.get(url)
    texts = stuff.text.split('\n')
    anagrams = anagramDict(texts)
    print("Welcome to an Anagram finder!")
    while True:
        while True:
            characters = input("Please enter a word or set of characters: ")
            if not characters.isalpha():
                print("Please give a set of alphabetical characters: ")
            else:
                break
        print(anagrams.getAnagram(characters))
        quit = input("If you'd like to quit, please enter '1': ")
        if quit == '1':
            break


if __name__ == "__main__":
    main()
