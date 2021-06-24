import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("data.json"))

def matcher(word):
    word = word.lower()
    if word in data.keys():
        return data[word]
    elif len(get_close_matches(word, data.keys(), n = 1, cutoff = 0.8)) > 0:
        print("did you mean %s instead? " % get_close_matches(word, data.keys(), n = 1, cutoff = 0.8)[0])
        check = input("y or n? ")
        if  check != "y":
            return("enter word again")
        else:
            return data[get_close_matches(word, data.keys(), n = 1, cutoff = 0.8)[0]]
    else:
        return "word doesn't exists"

word = input("Enter a word: ")
print(matcher(word))
