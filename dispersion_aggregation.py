import numpy as np
import pandas as pd


def get_continent_aggregation(source_file_location, continent_data_directory):
    data = pd.read_csv(source_file_location)
    continents = (data['continent'].unique())
    for continent in continents:
        continent_data = data.loc[data['continent'] == continent]

        agg_cont_data = agg_continent_data(continent_data)
        np_array = np.array(agg_cont_data)

        agg_cont_data = pd.DataFrame(np_array.transpose(),
                                     columns=['date', 'total_cases', 'total_deaths', 'total_vaccinations',
                                              'people_vaccinated', 'people_fully_vaccinated', 'population',
                                              ])
        print(f'{continent_data_directory}{continent}.csv')
        agg_cont_data.sort_values(by=['date'], inplace=True)
        agg_cont_data.to_csv(f'{continent_data_directory}{continent}.csv', index=False)


def agg_continent_data(data):
    date = []
    total_cases = []
    total_deaths = []
    total_vaccinations = []
    people_vaccinated = []
    people_fully_vaccinated = []
    population = []

    data.drop('location', axis=1, inplace=True)
    dates = (data['date'].unique())
    for date_ in dates:
        data_per_date = data.loc[data['date'] == date_]
        cases = 0
        deaths = 0
        vaccinations = 0
        vaccinated = 0
        fully_vaccinated = 0
        population_ = 0

        for i in range(len(data_per_date)):
            cases += list(data_per_date['total_cases'])[i]
            deaths += list(data_per_date['total_deaths'])[i]
            vaccinations += list(data_per_date['total_vaccinations'])[i]
            vaccinated += list(data_per_date['people_vaccinated'])[i]
            fully_vaccinated += list(data_per_date['people_fully_vaccinated'])[i]
            population_ += list(data_per_date['population'])[i]

        data.drop(data[data['date'] == date_].index, inplace=True)

        date.append(date_)
        total_cases.append(cases)
        total_deaths.append(deaths)
        total_vaccinations.append(vaccinations)
        people_vaccinated.append(vaccinated)
        people_fully_vaccinated.append(fully_vaccinated)
        population.append(population_)

    new_data = [date, total_cases, total_deaths, total_vaccinations, people_vaccinated,
                people_fully_vaccinated, population, ]

    return new_data
