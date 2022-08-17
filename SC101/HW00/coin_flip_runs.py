"""
File: coin_flip_runs.py
Name: Chance
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random as r


def main():
	"""
	(1) end_runs is end condition
	(2) random string and meet our end condition
	(3) print random string
	"""
	print("Let;s flip a coin!")
	end_runs = int(input('Number of runs: '))

	# Initial Condition
	runs = 0
	on_check = 0
	pre_coin = 2
	ans = ''

	while True:
		# random coin 0/1
		coin = r.randrange(0, 2)

		# ans
		if coin:
			ans += 'H'
		else:
			ans += 'T'

		# runs
		if coin == pre_coin:
			if not on_check:
				runs += 1
				on_check = 1
		else:
			on_check = 0
		pre_coin = coin

		# EXIT
		if runs == end_runs:
			break
	print(ans)


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()
