"""
File: webcrawler.py
Name: Chance
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10890537
Female Number: 7939153
---------------------------
2000s
Male Number: 12975692
Female Number: 9207577
---------------------------
1990s
Male Number: 14145431
Female Number: 10644002
"""

import requests
from bs4 import BeautifulSoup

MAX_RANK = 200


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, features="html.parser")

        # ----- Write your code below this line ----- #

        # Initial Value
        men_total = 0
        women_total = 0

        # Find tags
        tags = soup.find_all('table', {'class': 't-stripe'})

        # Split the Specified Position
        lst = tags[0].tbody.text.split()

        # Sum
        for i in range(MAX_RANK):
            men_total += int(lst[i * 5 + 2].replace(',', ''))
            women_total += int(lst[i * 5 + 4].replace(',', ''))

        # Print
        print('Male Number:' + str(men_total))
        print('Female Number:' + str(women_total))


if __name__ == '__main__':
    main()
