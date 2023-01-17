def most_common_alphabet(word):
    word = word.lower()
    alphabet_count = {}
    for alphabet in word:
        if alphabet.isalpha():
            if alphabet in alphabet_count:
                alphabet_count[alphabet] += 1
            else:
                alphabet_count[alphabet] = 1
   
    most_common = '?'
    max_count = 0
    for alphabet, count in alphabet_count.items():
        if count > max_count:
            most_common = alphabet
            max_count = count
        elif count == max_count:
            most_common = '?'
    return most_common.upper() 


a = input()
print(most_common_alphabet(a)) 