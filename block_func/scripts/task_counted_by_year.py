#!/usr/bin/env python


from datetime import datetime
from collections import Counter


def get_men_counted_by_year(lst):
    f_list = []
    for item in lst:
        if item['gender'] == 'male':
            val_list = list(item.values())
            date_srt = datetime.strptime(val_list[2], "%Y-%m-%d")
            year = date_srt.strftime('%Y')
            f_list.append(int(year))
    return dict(Counter(f_list))


def date_string_to_year(date_string):
    dt = datetime.strptime(date_string, '%Y-%m-%d')
    return dt.year


def get_men_counted_by_year_t(users):
    men = filter(lambda user: user['gender'] == 'male', users)
    birth_years = map(lambda man: date_string_to_year(man['birthday']), men)
    return dict(Counter(birth_years))


def main():
    user_list = [
        {'name': 'Bronn', 'gender': 'male', 'birthday': '1973-03-23'},
        {'name': 'Reigar', 'gender': 'male', 'birthday': '1973-11-03'},
        {'name': 'Sansa', 'gender': 'female', 'birthday': '2012-11-03'},
        {'name': 'Jon', 'gender': 'male', 'birthday': '1980-11-03'},
    ]
    print(get_men_counted_by_year(user_list))
    print(get_men_counted_by_year([]))


if __name__ == "__main__":
    main()
