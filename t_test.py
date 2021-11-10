from math import sqrt
import pandas as pd
from scipy.stats import ttest_ind


def save_t_test(source_file_location, dest_file_location):
    print('<---------T-Test--------->')
    print('')
    data = pd.read_csv(source_file_location)

    people_fully_vaccinated_per_population = list(data['people_fully_vaccinated_per_population'])
    total_cases_per_population = list(data['total_cases_per_population'])
    total_deaths_per_population = list(data['total_deaths_per_population'])
    people_fully_vaccinated = list(data['people_fully_vaccinated'])
    total_cases = list(data['total_cases'])
    total_deaths = list(data['total_deaths'])

    df = pd.DataFrame(columns=['T_test_people_fully_vaccinated_per_population_AND_total_cases_per_population',
                               'T_test_people_fully_vaccinated_per_population_AND_total_deaths_per_population',
                               'T_test_people_fully_vaccinated_AND_total_cases',
                               'T_test_people_fully_vaccinated_AND_total_deaths'])

    df.assign()

    df['T_test_people_fully_vaccinated_per_population_AND_total_cases_per_population'] = [
        t_test(people_fully_vaccinated_per_population, total_cases_per_population)]

    print('T_test_people_fully_vaccinated_per_population_AND_total_cases_per_population: ')
    print(
        ttest_ind(people_fully_vaccinated_per_population, total_cases_per_population, equal_var=True))

    df['T_test_people_fully_vaccinated_per_population_AND_total_deaths_per_population'] = [
        t_test(people_fully_vaccinated_per_population, total_deaths_per_population)]

    print('T_test_people_fully_vaccinated_per_population_AND_total_deaths_per_population: ')
    print(
        ttest_ind(people_fully_vaccinated_per_population, total_deaths_per_population, equal_var=True))

    df['T_test_people_fully_vaccinated_AND_total_cases'] = [
        t_test(people_fully_vaccinated, total_cases)]

    print('T_test_people_fully_vaccinated_AND_total_cases: ')
    print(
        ttest_ind(people_fully_vaccinated, total_cases, equal_var=True))

    df['T_test_people_fully_vaccinated_AND_total_deaths'] = [
        t_test(people_fully_vaccinated, total_deaths)]

    print('T_test_people_fully_vaccinated_AND_total_deaths: ')
    print(
        ttest_ind(people_fully_vaccinated, total_deaths, equal_var=True))

    df.to_csv(dest_file_location)
    print('')
    print('')
    print('<------------t-test done!------------>')


def t_test(arr1, arr2):
    df = pd.DataFrame()
    df['first'] = arr1
    df['second'] = arr2
    stds = df.std()
    means = [df['first'].mean(), df['second'].mean()]
    res = (means[0] - means[1]) / (sqrt((stds['first'] ** 2 / len(arr1)) * (stds['second'] ** 2 / len(arr2))))
    # print(res)
    return res
