import dispersion_aggregation

continent_data_directory = 'source/continent/'
cleaned_data_file_location = 'output/cleaned_data.csv'

normalize.normalize_date(cleaned_data_file_location)

dispersion_aggregation.get_continent_aggregation(cleaned_data_file_location, continent_data_directory)
