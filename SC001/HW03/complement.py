"""
File: complement.py
Name: Chance
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    Give string dna and feedback it's complement(case-insensitive)
    """
    dna = input("Please give me a DNA strand and I'll find the complement: ")
    ans = build_complement(dna)
    print(ans)


def build_complement(dna):
    """
    Give string dna and feedback it's complement(case-insensitive)
    """
    ans = ''
    skip = 0
    for i in range(len(dna)):
        if dna[i] == 'A' or dna[i] == 'a':
            ans += 'T'
        elif dna[i] == 'T' or dna[i] == 't':
            ans += 'A'
        elif dna[i] == 'C' or dna[i] == 'c':
            ans += 'G'
        elif dna[i] == 'G' or dna[i] == 'g':
            ans += 'C'
        else:
            print('Please input the right DNA', end='')
            skip = 1
            break
    if skip == 1:
        return ''
    return ans


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
