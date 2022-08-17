"""
File: weather_master.py
Name: Chance
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""


LOW_BOUND_TEMP = 16
EXIT = -100


def main():
	"""
	Give the next temperature and reply the highest/Lowest/Average temperature
	ane code day(<16)
	Exit if input -100
	"""

	print('stanCode "Weather Master 4.0"')
	temp = int(input('Next Temperature: (or '+str(EXIT)+' to quit)? '))
	times_temp = 0
	sum_temp = 0
	lowest_temp = temp
	highest_temp = temp
	times_low_temp = 0
	while True:
		if temp == EXIT:
			break
		times_temp += 1
		sum_temp += temp
		if temp < lowest_temp:
			lowest_temp = temp
		if temp > highest_temp:
			highest_temp = temp
		if temp < LOW_BOUND_TEMP:
			times_low_temp += 1
		temp = int(input('Next Temperature: (or '+str(EXIT)+' to quit)? '))
	if times_temp == 0:
		print('No temperatures were entered')
	else:
		print('Highest temperature = ' + str(highest_temp))
		print('Lowest temperature = ' + str(lowest_temp))
		print('Average = ' + str(sum_temp/times_temp))
		print(str(times_low_temp) + ' cold day(s)')

# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == "__main__":
	main()
