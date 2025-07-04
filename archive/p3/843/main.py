from collections import defaultdict
import sys

def print_map(map):
    for k,v in map.items():
        print(k, '->', v)

def decrypts(mapping, words_to_decrypt):
    for w in words_to_decrypt:
        decrypted_word = ''.join([mapping[a] if a in mapping else '*' for a in w])

        for vocab_word in [v for v in vocabulary if len(v) == len(decrypted_word)]:
            valid = True
            for i in range(len(vocab_word)):
                if decrypted_word[i] != '*' and decrypted_word[i] != vocab_word[i]:
                    valid = False
                    break
            if valid:
                return True

    return False

def mapping_is_valid(mapping, words, vocabulary):
    for word in words:
        decrypted = ''.join(mapping[a] if a in mapping else '*' for a in word)
        if decrypted not in vocabulary:
            return False

    return True

def decrypt1(words, vocabulary):
    '''
    brute force generates all possible mappings, memory expensive
    '''

    words = sorted(list(set(words)), key=lambda w: len(w))
    vocabulary = sorted(vocabulary, key=lambda w: len(w))

    vocab_by_length = defaultdict(list)
    for i, word in enumerate(vocabulary):
        vocab_by_length[len(word)].append((i, word))

    def build_mapping(n, used):
        if n == 0:
            return []

        curr_word = words[n - 1]
        vocab_words = [(index, v) for index, v in vocab_by_length[len(curr_word)] if index not in used]
        mappings = []

        for vocab_index,vocab_word in vocab_words:
            mapping = {}

            wrong_vocab_choice = False
            for i in range(len(vocab_word)):
                if (curr_word[i] in mapping and mapping[curr_word[i]] != vocab_word[i] or 
                    curr_word[i] not in mapping and vocab_word[i] in mapping.values()):
                    wrong_vocab_choice = True
                    break 

                mapping[curr_word[i]] = vocab_word[i]
           
            if wrong_vocab_choice:
                continue

            sub_mappings = build_mapping(n - 1, [vocab_index] + used)

            for sub_mapping in sub_mappings:
                mapping_cpy = mapping.copy()

                wrong_used_configuration = False
                for (k,v) in sub_mapping.items():

                    if (k in mapping_cpy and mapping_cpy[k] != v or 
                        k not in mapping_cpy and v in mapping_cpy.values()):
                        wrong_used_configuration = True
                        break

                    mapping_cpy[k] = v

                if wrong_used_configuration:
                    continue

                if decrypts(mapping_cpy, words):
                    mappings.append(mapping_cpy)
                

            mappings.append(mapping)

        return mappings

    decrypt_mappings = build_mapping(len(words), [])

    valid_mappings = [m for m in decrypt_mappings if mapping_is_valid(m, words, vocabulary)]
    return valid_mappings[0] if len(valid_mappings) != 0 else None


def decrypt2(words, vocabulary):
    '''
    backtracking with less memory usage
    '''

    words = sorted(list(set(words)), key=lambda w: len(w))
    vocabulary = sorted(vocabulary, key=lambda w: len(w))

    vocab_by_length = {}
    for i, word in enumerate(vocabulary):
        vocab_by_length.setdefault(len(word), []).append((i, word))

    all_mappings = []

    def backtrack(index, used_indices, mapping):
        if index == len(words):
            # Make a copy so it's not mutated later
            all_mappings.append(mapping.copy())
            return

        curr_word = words[index]
        candidates = vocab_by_length.get(len(curr_word), [])

        for vocab_index, vocab_word in candidates:
            if vocab_index in used_indices:
                continue

            local_mapping = {}
            conflict = False

            for c, v in zip(curr_word, vocab_word):
                if c in mapping:
                    if mapping[c] != v:
                        conflict = True
                        break
                elif v in mapping.values():
                    conflict = True
                    break
                else:
                    local_mapping[c] = v

            if conflict:
                continue

            # Apply local changes
            for k, v in local_mapping.items():
                mapping[k] = v
            used_indices.add(vocab_index)

            # Recurse
            backtrack(index + 1, used_indices, mapping)

            # Undo changes
            for k in local_mapping:
                del mapping[k]
            used_indices.remove(vocab_index)

    backtrack(0, set(), {})

    # After generating all candidate mappings, filter them
    for m in all_mappings:
        if decrypts(m, words) and mapping_is_valid(m, words, vocabulary):
            return m

    return None


if __name__ == "__main__":
    lines = [ line.strip() for line in sys.stdin.readlines() ]

    n = int(lines[0])

    vocabulary = []
    output = []

    for line in lines[1:1+n]:
        vocabulary.append( line )

    for line in lines[1+n:]:
        words = line.split()

        # mapping = decrypt1(words, vocabulary)
        mapping = decrypt2(words, vocabulary)

        if mapping is None:
            output.append( ' '.join(['*' * len(word) for word in words]) )
        else:    
            output.append( ' '.join([''.join(mapping[a] for a in word) for word in words]) )

    print('\n'.join(output))
