from time import time
import sys
import json

word_dictionary = []
# load the dictionary file into the word_dictionary
for word in open('words.txt', 'r'):
    word_dictionary.append(word.lower().strip())


def anagram_finder(anagram):
    current_time = time()
    words = []

    is_anagram_found = False
    current_time = time()
    for word in word_dictionary:
        if (len(word) == len(anagram)) \
           and (sorted(anagram) == sorted(word)) \
           and not (word == anagram):
            is_anagram_found = True
            words.append(word)

    if not is_anagram_found:
        words.append("No anagrams found")

    print(words)
    
    return (
        words,
        "{}s".format(str(time() - current_time))
    )


def anagram_handler(event, context):
    print(event)
    print(type(event))
    print(json.loads(event["body"])["word"])
    
    
    return {
        "response": anagram_finder(json.loads(event["body"])["word"]),
        "StatusCode": 200
    }

# only run the program if started directly, rather than from a module
if __name__ == "__main__":
    print(anagram_finder(sys.argv[1]))

