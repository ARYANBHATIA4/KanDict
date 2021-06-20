import json
data = json.load(open("data.json"))
conti = "y"

def check(conti):
    while conti == "y":
        word = input("Enter a word: ")
        print("\n", data[word], "\n")
        conti = input("Do you want to continue(y or n): ")
        if conti == "n":
            break
        print("\n")

try:
    check(conti)
except:
    print("\n", "invalid Try a different word", "\n")
