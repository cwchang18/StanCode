"""
File: class_reviews.py
Name: Chance
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""

EXIT = -1


def main():
    """
    input SC001/SC101 and score to calculate max/min/avg
    class == EXIT -> EXIT
    """
    # Initial condition
    times_class_001 = 0
    times_class_101 = 0
    sum_score_001 = 0
    sum_score_101 = 0
    max_score_001 = 0
    max_score_101 = 0
    min_score_001 = 0
    min_score_101 = 0

    # Ask the class/score
    while True:
        class_name = input('Which class? ')
        class_name = class_name.upper()

        # EXIT
        if class_name == str(EXIT):
            break

        score = int(input('Score: '))

        # class SC001
        if class_name == 'SC001':
            if times_class_001 == 0:
                times_class_001 = 1
                sum_score_001 = score
                max_score_001 = score
                min_score_001 = score
            else:
                times_class_001 += 1
                sum_score_001 += score
                if score > max_score_001:
                    max_score_001 = score
                elif score < min_score_001:
                    min_score_001 = score

        # class SC101
        elif class_name == 'SC101':
            if times_class_101 == 0:
                times_class_101 = 1
                sum_score_101 = score
                max_score_101 = score
                min_score_101 = score
            else:
                times_class_101 += 1
                sum_score_101 += score
                if score > max_score_101:
                    max_score_101 = score
                elif score < min_score_101:
                    min_score_101 = score

    # print No scores were entered
    if times_class_001 + times_class_101 == 0:
        print('No class scores were entered')
    else:
        # print SC001 score
        print('=============SC001=============')
        if times_class_001 == 0:
            print('No score for SC001')
        else:
            print('Max (001): ' + str(max_score_001))
            print('Min (001): ' + str(min_score_001))
            print('Avg (001): ' + str(sum_score_001 / times_class_001))

        # print SC101 score
        print('=============SC101=============')
        if times_class_101 == 0:
            print('No score for SC101')
        else:
            print('Max (101): ' + str(max_score_101))
            print('Min (101): ' + str(min_score_101))
            print('Avg (101): ' + str(sum_score_101 / times_class_101))


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
