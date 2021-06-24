#importing all the essential librarys for thr program
#helps loading .json files
import json
#this lib is what makes this dict smart
import difflib
#this func returns a floating value by comparing the 2 strings 1=same and similarly decending accordingly
from difflib import SequenceMatcher
#this compares one string to multiple strings to give out the closest strings in list format
from difflib import get_close_matches

#opens data.json file and store it in data variable
data = json.load(open("data.json"))
conti = "y"
def matcher(word):
    #converts the word in lower case as whole dict has lowercase keys
    word = word.lower()
    #this func compares the word to all the keys avaialble and returns the closest string
    #and store it in cm, n=1 gives out only 1 element in list cutoff gives closest possile value
    cm = get_close_matches(word, data.keys(), n = 1, cutoff = 0.8)
    # if a word directly matches with the key
    if word in data.keys():
        #*splits a list and sep seprates the list with "\n" between each gap
        print(*(data[word]), sep = "\n\n")
        #as single words could have multiple meanings it splits list open and prints it seprately
    #if word didnt matched directly with key and has a value stored in list
    elif len(cm) > 0:
        #prints out the 0th element of list that is first and the only element in the list present
        print("\ndid you mean %s instead? \n" %cm[0])
        check = input("'y' for yes or 'n' for no? \n")
        if  check == "y":
            #if user had the typo it replaces wron string with the right one and prints its value
            print(*(data[cm[0]]), sep ="\n\n")
        elif check == "n":
            print("\nenter word again\n")
        else:
            print("I said 'y' or 'n' 😑")
    #if word didnt directly, wrongly matched anything then this prints
    else:
        print("\nword doesn't exists")

#program starts from here conti is y so it runs, until y is not replaced with anthing else
while conti == "y":
    word = input("Enter a word: ")
    matcher(word)
    conti = input("\nDo you want to search for more words? y or n :")
