"""
File: similarity.py (extension)
Name: Chance
----------------------------
This program is an extension of assignment3!
It will compare short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    Search the maximum similar string in dna
    """
    # Initial define
    dna_word = input('Please give me a DNA sequence to search: ')
    match_word = input('What DNA sequence would you like to match? ')
    num_dna_word = len(dna_word)
    num_match_word = len(match_word)
    max_num_similar = 0
    max_similar_word = ''
    for i in range(num_dna_word-num_match_word+1):
        num_similar = 0
        similar_word = ''
        for j in range(num_match_word):
            if dna_word[i+j].upper() == match_word[j].upper():
                num_similar += 1
            similar_word += dna_word[i+j].upper()
        if num_similar > max_num_similar:
            max_num_similar = num_similar
            max_similar_word = similar_word
    print('The best match is ' + max_similar_word)


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
