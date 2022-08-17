"""
File: boggle.py
Name: Chance
----------------------------------------
(1) Boggle with word 4x4
(2) String adjacent words together
(3) Search the dictionary
(4) Output the search result
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	(1) Boggle with word 4x4
	(2) String adjacent words together
	(3) Search the dictionary
	(4) Output the search result
	"""
	# row_1
	row_1_lst = question(1)
	if len(row_1_lst) == 0:
		print('Illegal input')
		return

	# row_2
	row_2_lst = question(2)
	if len(row_2_lst) == 0:
		print('Illegal input')
		return

	# row_3
	row_3_lst = question(3)
	if len(row_3_lst) == 0:
		print('Illegal input')
		return

	# row_4
	row_4_lst = question(4)
	if len(row_4_lst) == 0:
		print('Illegal input')
		return

	# data_lst
	data_lst = [row_1_lst, row_2_lst, row_3_lst, row_4_lst]

	ans_lst = []

	start = time.time()

	# dict word
	dict_set = read_dictionary()[0]
	# dict search prefix word
	dict_search_set = read_dictionary()[1]

	for x in range(4):
		for y in range(4):
			# do a boggle
			boggle(x, y, data_lst[y][x], data_lst, ans_lst, [[x,y]], dict_set, dict_search_set)

	# output the result
	for i in range(len(ans_lst)):
		print(f'Found "{ans_lst[i]}"')
	print(f'There are {len(ans_lst)} words in total.')
	####################
	#                  #
	#       TODO:      #
	#                  #
	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def question(n):
	"""
	:param n: (int) Give 'n' times question
	"""
	row_lst = input(str(n) + ' row of letters: ').split()
	if len(row_lst) != 4:
		return []
	for i in range(len(row_lst)):
		if len(row_lst[i]) != 1:
			return []
		else:
			row_lst[i] = row_lst[i].lower()
	return row_lst


def boggle(x, y, cur_str, data_lst, ans_lst, path_lst, dict_set, dict_search_set):
	"""
	:param x: (int) The origin position x
	:param y: (int) The origin position y
	:param cur_str: (str) current string
	:param data_lst: (lst(lst)) 4x4 words
	:param ans_lst: (lst) search result
	:param path_lst: (lst) current search path
	:param dict_set: (set) dictionary word
	:param dict_search_set: (set) dictionary prefix word
	"""
	for i in range(-1, 2):
		if x+i < 0 or x+i > 3:
			continue
		for j in range(-1, 2):
			if y+j < 0 or y+j > 3:
				continue
			if [x+i, y+j] not in path_lst:
				if cur_str + data_lst[y+j][x+i] in dict_search_set:
					# choose
					path_lst.append([x+i, y+j])
					cur_str += data_lst[y+j][x+i]
					if len(cur_str) >= 4:
						if cur_str in dict_set:
							if cur_str not in ans_lst:
								ans_lst.append(cur_str)
					# explore
					boggle(x+i, y+j, cur_str, data_lst, ans_lst, path_lst, dict_set, dict_search_set)
					# un-choose
					path_lst.pop()
					cur_str = cur_str[:-1]


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, 'r') as f:
		lst_f = f.read().split('\n')
		set_f = set(lst_f)
		super_set = {s[0:x+1] for s in set_f for x in range(len(s))}
	return [set_f, super_set]


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	pass


if __name__ == '__main__':
	main()
