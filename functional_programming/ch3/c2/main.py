def sort_dates(date_list):
    sorted_dates = sorted(date_list, key=format_date)
    return sorted_dates


def format_date(date):
    month, day, year = map(int, date.split("-"))
    return (year, month, day)
