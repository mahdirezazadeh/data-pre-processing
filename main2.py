import decision_tree
import dispersion_aggregation
import normalize

continent_data_directory = 'output/continent/'
cleaned_data_file_location = 'output/cleaned_data.csv'
normalized_date_file_location = 'output/normalized_date.csv'

# normalize.normalize_date(cleaned_data_file_location, normalized_date_file_location)

# dispersion_aggregation.get_continent_aggregation(normalized_date_file_location, continent_data_directory)

decision_tree.regressor_directory(continent_data_directory)

# decision_tree.regressor_country(normalized_date_file_location)
