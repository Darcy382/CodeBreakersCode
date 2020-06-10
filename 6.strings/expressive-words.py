def expressiveWords(S: str, words) -> int:
    main_key, main_counts = make_key_counts(S)
    expressive_words = 0
    L = len(main_key)
    for word in words:
        temp_key, temp_counts = make_key_counts(word)
        print(temp_key)
        if L != len(temp_key):
            continue
        expressive = True
        for i in range(L):
            # Letter mismatch
            # count mismatch, temp > main or main < 3
            fails_expressive = (
                    temp_key[i] != main_key[i]
                    or temp_counts[i] > main_counts[i]
                    or temp_counts[i] < main_counts[i] and main_counts[i] < 3
            )
            print(fails_expressive)
            if fails_expressive:
                expressive = False
                break
        if expressive:
            expressive_words += 1
    return expressive_words

def make_key_counts(string):
    key = []
    letter_counts = []
    i = 0
    while i < len(string):
        key.append(string[i])
        letter_counts.append(1)
        while i < len(string) - 1 and string[i] == string[i + 1]:
            letter_counts[-1] += 1
            i += 1
        i += 1
    return ("".join(key), tuple(letter_counts))

S = "heeellooo"
words = ["hello", "hi", "helo"]

print(expressiveWords(S, words))