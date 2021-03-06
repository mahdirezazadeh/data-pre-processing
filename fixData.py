import pandas as pd


def fix_column(column):
    if pd.isnull(column[0]):
        column[0] = 0

    col_len = len(column)
    for index in range(1, col_len):
        if pd.isnull(column[index]):
            column[index] = column[index - 1]

    # print(column)
    return column


def fix_column2(column):
    col_len = len(column)
    for index in range(0, col_len):
        if pd.isnull(column[index]):
            column[index] = 0

    return column


def fix_columns(data_per_location):
    total_vaccinations = fix_column(list(data_per_location['total_vaccinations']))
    people_vaccinated = fix_column(list(data_per_location['people_vaccinated']))
    people_fully_vaccinated = fix_column(list(data_per_location['people_fully_vaccinated']))
    total_deaths = fix_column(list(data_per_location['total_deaths']))
    total_cases = fix_column(list(data_per_location['total_cases']))

    new_cases = fix_column2(list(data_per_location['new_cases']))
    new_deaths = fix_column2(list(data_per_location['new_deaths']))

    return total_vaccinations, people_vaccinated, people_fully_vaccinated \
        , total_deaths, total_cases, new_cases, new_deaths


def fix(source_file_location, cleaned_data_file_location):
    data = pd.read_csv(source_file_location)

    # remove two location datasets from dataframe
    data.drop(data[data['location'] == 'International'].index, inplace=True)
    data.drop(data[data['location'] == 'Northern Cyprus'].index, inplace=True)

    # get all locations
    locations = (data['location'].unique())
    new_data = [[], [], [], [], [], [], []]
    for location in locations:
        total_vaccinations, people_vaccinated, people_fully_vaccinated, total_deaths \
            , total_cases, new_cases, new_deaths = fix_columns(data.loc[data['location'] == location])
        new_data[0].extend(total_vaccinations)
        new_data[1].extend(people_vaccinated)
        new_data[2].extend(people_fully_vaccinated)
        new_data[3].extend(total_deaths)
        new_data[4].extend(total_cases)
        new_data[5].extend(new_cases)
        new_data[6].extend(new_deaths)

    # replace new data with old data
    data.drop('total_cases', axis=1, inplace=True)
    data.insert(4, 'total_cases', new_data[4], True)

    data.drop('total_deaths', axis=1, inplace=True)
    data.insert(5, 'total_deaths', new_data[3], True)

    data.drop('total_vaccinations', axis=1, inplace=True)
    data.insert(6, 'total_vaccinations', new_data[0], True)

    data.drop('people_vaccinated', axis=1, inplace=True)
    data.insert(7, 'people_vaccinated', new_data[1], True)

    data.drop('people_fully_vaccinated', axis=1, inplace=True)
    data.insert(8, 'people_fully_vaccinated', new_data[2], True)

    data.drop('new_cases', axis=1, inplace=True)
    data.insert(9, 'new_cases', new_data[5], True)

    data.drop('new_deaths', axis=1, inplace=True)
    data.insert(10, 'new_deaths', new_data[6], True)

    # write to file
    data.to_csv(cleaned_data_file_location, index=False)
