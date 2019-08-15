# AnagramDict
AnagramDict is a python class that constructs a dictionary to find anagrams given any list of words.

## Approach
I used an approach based off of [this article](https://scipython.com/blog/using-prime-numbers-to-determine-if-two-words-are-anagrams/):

We construct a dictionary to get a unique signature from each word using a hash that maps prime numbers to letters. Then, we store the product of each hashed letter as a key in our dictionary saving the word as a value in a list.

We can throw any set of letters into the hash and look it up in the dictionary to see if there are any anagrams.


Space: O(size of dictionary) we store the dictionary in memory   
Run time for lookup: O(length of letters)+O(1) We hash the letters and then look it up

## Usage
This will run our anagrams finder program with user input
```bash
python3 anagrams.py
```

If you'd like to use the anagrams dict itself you can
```python
import anagrams
import requests

url = 'https://raw.githubusercontent.com/lad/words/master/words'
stuff = requests.get(url)
texts = stuff.text.split('\n')
anagrams = anagramDict(texts)

anagrams.getAnagram('a') # will return -> ['a','A']
```

## Running it with the bash file
Make sure python3 is in your path!