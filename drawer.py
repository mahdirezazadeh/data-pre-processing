import pandas as pd
import matplotlib.pylab as plt
from pathlib import Path


def draw_charts(src, output_folder_location):
    data = pd.read_csv(src)
    locations = ['Iran', 'Comoros', 'Brazil']

    Path('/{}'.format(output_folder_location)).mkdir(parents=True, exist_ok=True)

    for location in locations:
        Path('/{}/{}'.format(output_folder_location, location)).mkdir(parents=True, exist_ok=True)
        draw_line_charts_full_per_page(data.loc[data['location'] == location], location, output_folder_location)

    for location in locations:
        draw_scatter_plot_full_per_page(data.loc[data['location'] == location], location, output_folder_location)


def draw_line_charts_full_per_page(dataframe, country_name, output_folder_location):
    dataframe.plot(
        y=['total_deaths_per_population', 'people_fully_vaccinated_per_population', 'total_cases_per_population'],
        x='date', kind='line')

    plt.title(country_name)
    plt.savefig(
        '{}/{}/Total_deaths_per_population_People_fully_vaccinated_per_population_Total_cases_per_population.png'.format(
            output_folder_location, country_name))
    plt.show()

    dataframe.plot(
        y=['total_deaths', 'people_fully_vaccinated', 'total_cases'],
        x='date', kind='line')

    plt.title(country_name)
    plt.savefig(
        '{}/{}/total_deaths_people_fully_vaccinated_total_cases.png'.format(output_folder_location, country_name))
    plt.show()

    dataframe.plot(
        y=['total_vaccinations', 'people_vaccinated', 'people_fully_vaccinated'],
        x='date', kind='line')

    plt.title(country_name)
    plt.savefig('{}/{}/total_vaccinations_people_vaccinated_people_fully_vaccinated.png'.format(output_folder_location,
                                                                                                country_name))
    plt.show()


def draw_scatter_plot_full_per_page(dataframe, country_name, output_folder_location):
    dataframe.plot.scatter(
        y='people_fully_vaccinated',
        x='total_cases', s=1)

    plt.title(country_name)
    plt.savefig('{}/{}/people_fully_vaccinated_total_cases.png'.format(output_folder_location, country_name))
    plt.show()

    dataframe.plot.scatter(
        y='people_fully_vaccinated',
        x='total_deaths', s=1)

    plt.title(country_name)
    plt.savefig('{}/{}/people_fully_vaccinated_total_deaths.png'.format(output_folder_location, country_name))
    plt.show()

    dataframe.plot.scatter(
        y='total_vaccinations',
        x='total_cases', s=1)

    plt.title(country_name)
    plt.savefig('{}/{}/total_vaccinations_total_cases.png'.format(output_folder_location, country_name))
    plt.show()

    dataframe.plot.scatter(
        y='total_vaccinations',
        x='total_deaths', s=1)

    plt.title(country_name)
    plt.savefig('{}/{}/total_vaccinations_total_deaths.png'.format(output_folder_location, country_name))
    plt.show()

    dataframe.plot.scatter(
        y='total_vaccinations',
        x='people_fully_vaccinated', s=1)

    plt.title(country_name)
    plt.savefig('{}/{}/total_vaccinations_people_fully_vaccinated.png'.format(output_folder_location, country_name))
    plt.show()

    dataframe.plot.scatter(
        y='total_deaths',
        x='total_cases', s=1)

    plt.title(country_name)
    plt.savefig('{}/{}/total_deaths_total_cases.png'.format(output_folder_location, country_name))
    plt.show()
