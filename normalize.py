import pandas as pd


def normalize_date(source_file_location, dest_file_location):
    data = pd.read_csv(source_file_location)
    data.dropna(subset=['continent'], axis=0, inplace=True)
    new_dates = fix_column(list(data['date']))
    data.drop('date', axis=1, inplace=True)
    data.insert(3, 'date', new_dates, True)
    data.to_csv(dest_file_location, index=False)


def fix_column(column):
    col_len = len(column)
    for index in range(0, col_len):
        column[index] = fix_date(column[index])

    # print(column)
    return column


def fix_date(date):
    month, days, year = date.split('/')
    if len(month) < 2:
        month = '0' + month
    if len(days) < 2:
        days = '0' + days

    return f'{year}{month}{days}'
