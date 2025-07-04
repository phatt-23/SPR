import sys
import string
from typing import DefaultDict, List
from copy import copy

def load_num():
    return int(sys.stdin.readline().rstrip())

def load_line():
    return sys.stdin.readline().rstrip()

def is_valid_choice(subs, e, w):
    if len(e) != len(w):
        return False
    for a,b in zip(e,w):
        if subs[a] != None and subs[a] != b:
            return False
    return True

def add_word(subs, e, w):
    new_subs = copy(subs)
    for a,b in zip(e,w):
        if new_subs[a] == b:
            continue

        if new_subs[a] != None:
            raise
        if b in new_subs.values():
            raise
        new_subs[a] = b
    return new_subs


def decrypt(enc, words, subs=None, d=0):
    if subs is None:
        subs = {i:None for i in string.ascii_lowercase}

    for word in words[len(enc[0])]:
        if not is_valid_choice(subs, enc[0], word):
            continue

        try:
            new_subs = add_word(subs, enc[0], word)
        except:
            continue

        # print('  '*d, word)

        if len(enc) == 1:
            return [word]

        result = decrypt(enc[1:], words, new_subs, d+1)
        if result:
            return [word] + result
    
    return None


if __name__ == "__main__":
    words = DefaultDict(List)

    n_words = load_num()

    for _ in range(n_words):
        word = load_line()
        if len(word) not in words:
            words[len(word)] = []
        words[len(word)].append(word)

    for enc_line in sys.stdin:
        enc = enc_line.split() 

        # print('-----------------')
        # print(enc)
        result = decrypt(enc, words)
        # print(result)
        if result:
            print(' '.join(result))
        else:
            print(' '.join('*'*len(e) for e in enc))