

def main():
    word_dictionary = {
    "hi" : "a word for greeting",
    "earth": "the third planet in the solar system",
    "milk" : "a substance gotten from animals udder"
    }

    while True:
        word = input("Enter a word : ")
        if word == "":
            break
        if word in word_dictionary:
            print(word, ":", word_dictionary(word))
print(main())

#still under review not yet complete
