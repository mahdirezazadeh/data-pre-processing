import pandas as pd


def get_continent_aggregation(source_file_location, continent_data_directory):
    data = pd.read_csv(source_file_location)
    continents = (data['continent'].unique())
    for continent in continents:
        continent_data = data.loc[data['continent'] == continent]
        agg_cont_data = agg_continent_data(continent_data)
        agg_cont_data = pd.DataFrame(agg_cont_data,
                                     columns=['date', 'total_cases', 'total_deaths', 'total_vaccinations',
                                              'people_vaccinated', 'people_fully_vaccinated', 'population',
                                              ])
        agg_cont_data.to_csv(continent_data_directory + '/' + continent + '.csv', index=False)


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
        for details in data_per_date:
            cases += details['total_cases']
            deaths += details['total_deaths']
            vaccinations += details['total_vaccinations']
            vaccinated += details['people_vaccinated']
            fully_vaccinated += details['people_fully_vaccinated']
            population_ += details['population']

        data.drop(data[data['date'] == date_].index, inplace=True)

        date.append(date_)
        total_cases.append(cases)
        total_deaths.append(deaths)
        total_vaccinations.append(vaccinations)
        people_vaccinated.append(vaccinated)
        people_fully_vaccinated.append(fully_vaccinated)
        population.append(population_)

    new_data = [[date], [total_cases], [total_deaths], [total_vaccinations], [people_vaccinated],
                [people_fully_vaccinated], [population], ]

    return new_data
