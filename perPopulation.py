import pandas as pd


def add_new_columns(source_file_location, dest_file_location):
    data = pd.read_csv(source_file_location)
    data['total_cases_per_population'] = (data['total_cases'] * 100) / data['population']
    data['total_deaths_per_population'] = (data['total_deaths'] * 100) / data['population']
    data['people_fully_vaccinated_per_population'] = (data['people_fully_vaccinated'] * 100) / data['population']
    data.to_csv(dest_file_location)
