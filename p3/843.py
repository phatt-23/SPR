import sys
from collections import defaultdict
import string
from copy import copy

# substitutions : map[from enc char -> dict char]

def load_num():
    return int(sys.stdin.readline().rstrip())

def load_line():
    return sys.stdin.readline().rstrip()

def is_valid_sub_choice(word: str, enc: str, substitutions: dict) -> bool:
    if len(word) != len(enc):
        return False
    for e,w in zip(enc, word):
        if substitutions[e] != None and substitutions[e] != w:
            return False
    return True
    
def add_sub_for(enc: str, word: str, substitutions: dict):
    new_subs = copy(substitutions)
    for e,w in zip(enc, word):
        if new_subs[e] is None:
            # but check if w is already mapped by some other char
            if w in new_subs.values():
                return None
        elif new_subs[e] != w:  
            # if the sub is already filled and it doesn't 
            # match with the current enc and word we try 
            # to add to the subs, then it is not valid
            return None
        # if the sub is not there yet add it in
        new_subs[e] = w
    return new_subs

def foo(enc, words, subs):
    for word in words[len(enc[0])]:
        # print(enc[0], '->', word)
        if not is_valid_sub_choice(word, enc[0], subs):
            continue
        new_subs = add_sub_for(enc[0], word, subs)
        if new_subs is None:
            continue

        if len(enc) == 1:
            return [word]

        result = foo(enc[1:], words, new_subs)
        if result is not None:
            return [word] + result

    return None

if __name__ == "__main__":
    dict_size = load_num()
    # put the words into dict by size
    dictionary = defaultdict(list)   # len(word): [word1, word2, word3]

    for _ in range(dict_size):
        word = load_line()
        if len(word) not in dictionary:
            dictionary[len(word)] = []
        dictionary[len(word)].append(word)

    # pprint(dictionary)

    for enc_line in sys.stdin:
        enc = enc_line.split()
        subs = {a: None for a in string.ascii_lowercase}
        result = foo(enc, dictionary, subs)
        if result is None:
            print(" ".join('*' * len(e) for e in enc))
        else:
            print(" ".join(result))

    

