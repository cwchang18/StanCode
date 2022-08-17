"""
File: caesar.py
Name: Chance
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    Give me a shift number and translate the secret.
    """
    secret_number = int(input('Secret number: '))
    secret_word = input("What's the ciphered string?")

    # define new_alphabet and replace secret_word to ans
    new_alphabet = ALPHABET[26-secret_number:]+ALPHABET[:26-secret_number]
    ans = ''
    for i in range(len(secret_word)):
        # skip means secret_word not alphabet
        # .isalpha() need to check more time than skip
        skip = 1
        for j in range(26):
            if secret_word[i] == new_alphabet[j] or secret_word[i] == new_alphabet[j].lower():
                ans += ALPHABET[j]
                skip = 0
                break
        if skip == 1:
            ans += secret_word[i]
    print('The deciphered string is: ' + ans)


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
