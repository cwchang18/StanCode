"""
File: anagram.py
Name: Chance
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    TODO:
    """

    # initial variable
    num = 0
    super_set = set()
    search_times = 0
    output_time_wi_dict = 0
    input_word_lst = []
    output_time_lst = []

    # choose dict type
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit')
    print('______________________________________________________________________')
    print('(1) Basic Dict - Dict build fast, but search slow')
    print('(2) Better Dict - Dict build slow, but search slightly fast')
    print('(3) Super Dict - Dict build slow slow slow slow, but best search time')
    select_dict = int(input('Dict Choose(1/2/3): '))

    # better dict: need to choose num of word to check whether go recursion
    if select_dict == 2:
        num = int(input('Better Dict choose how many words to judge(Suggest 4 or 5) : '))
        if num == EXIT:
            return

    # search dict and cal. the dict time
    start_build_dict_time = time.time()
    set_f = read_dictionary()

    # basic dict
    if select_dict == 1:
        pass

    # better dict
    elif select_dict == 2:
        for line in set_f:
            if line[0:num] not in super_set:
                super_set.add(line[0:num])

    # super dice
    elif select_dict == 3:
        for line in set_f:
            for num in range(len(line)):
                if line[0:num + 1] not in super_set:
                    super_set.add(line[0:num + 1])
        super_set.add('')

    # no select dict
    else:
        print("Don't joke me, goodbye")
        return
    end_build_dict_time = time.time()

    # output the dict time
    print(f'Build time: {end_build_dict_time - start_build_dict_time} seconds.')

    # search word
    while True:

        # print all check result
        for i in range(search_times):
            if i == 0:
                print(f'search word wi dict: {input_word_lst[i]}; use time: {output_time_wi_dict} ')
            print(f'search word: {input_word_lst[i]}; use time: {output_time_lst[i]} ')
        print('----------------------------------')

        # input data and cal. the times
        input_word = input('Find anagrams for: ')
        if input_word == str(EXIT):
            break
        start_select_word_time = time.time()
        print('Searching...')

        # permutations set
        per_set = find_anagrams_basic(input_word, select_dict, num, super_set)

        # intersection set
        ans_set = per_set & set_f
        ans_lst = list(ans_set)

        # print result
        for i in range(len(ans_set)):
            print(f'Found:   {ans_lst[i]}')
            print('Searching...')

        print(f' {len(ans_set)} anagrams: {ans_set}')

        # end time
        end_select_word_time = time.time()

        # for next print
        input_word_lst.append(input_word)
        output_time_lst.append(end_select_word_time - start_select_word_time)
        if search_times == 0:
            output_time_wi_dict = end_select_word_time - start_select_word_time + \
                                  end_build_dict_time - start_build_dict_time
        search_times += 1
        print('----------------------------------')


def read_dictionary():
    with open(FILE, 'r') as f:
        lst_f = f.read().split('\n')
        set_f = set(lst_f)
    return set_f


def find_anagrams_basic(s, select_dict, num, check_set):
    """
    :param s: (str) the word need to do anagram
    :param select_dict: (int) dict type
    :param num: (int) better dict choose how many word
    :param check_set: (set) if not in set, don't recursion
    :return:
    """
    ans_len = len(s)
    data_dict = {}
    per_lst = []

    for i in range(len(s)):
        data_dict[i] = s[i]

    # basic dict
    if select_dict == 1:
        find_anagrams_helper_basic(ans_len, data_dict, {}, per_lst)

    # better dict
    elif select_dict == 2:
        find_anagrams_helper_better(ans_len, data_dict, {}, per_lst, check_set, num)

    # super dict
    else:
        find_anagrams_helper_super(ans_len, data_dict, {}, per_lst, check_set)

    per_set = set(per_lst)

    return per_set


def find_anagrams_helper_basic(ans_len, data_dict, current_dict, per_lst):
    if len(current_dict) == ans_len:
        per_lst.append(''.join(current_dict.values()))
    else:
        for s in data_dict:
            if s not in current_dict:
                # choose
                current_dict[s] = data_dict[s]
                # explore
                find_anagrams_helper_basic(ans_len, data_dict, current_dict, per_lst)
                # un-choose
                current_dict.popitem()


def find_anagrams_helper_better(ans_len, data_dict, current_dict, per_lst, check_set, num):
    if len(current_dict) == ans_len:
        per_lst.append(''.join(current_dict.values()))
    else:
        for s in data_dict:
            if s not in current_dict:
                if len(current_dict) == num:
                    if ''.join(current_dict.values()) in check_set:
                        # choose
                        current_dict[s] = data_dict[s]
                        # explore
                        find_anagrams_helper_better(ans_len, data_dict, current_dict, per_lst, check_set, num)
                        # un-choose
                        current_dict.popitem()
                else:
                    # choose
                    current_dict[s] = data_dict[s]
                    # explore
                    find_anagrams_helper_better(ans_len, data_dict, current_dict, per_lst, check_set, num)
                    # un-choose
                    current_dict.popitem()


def find_anagrams_helper_super(ans_len, data_dict, current_dict, per_lst, check_set):
    if len(current_dict) == ans_len:
        per_lst.append(''.join(current_dict.values()))
    else:
        for s in data_dict:
            if s not in current_dict:
                if ''.join(current_dict.values()) in check_set:
                    # choose
                    current_dict[s] = data_dict[s]
                    # explore
                    find_anagrams_helper_super(ans_len, data_dict, current_dict, per_lst, check_set)
                    # un-choose
                    current_dict.popitem()


def has_prefix(sub_s):
    """
    :param sub_s:
    :return:
    """
    pass


if __name__ == '__main__':
    main()
