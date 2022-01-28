import drawer
import fixData
import perPopulation
import t_test

main_source_file_location = "source/SARS-CoV-2 Dataset Updated.csv"
cleaned_data_file_location = "output/cleaned_data.csv"
per_population_data_file_location = "output/per_population_data.csv"
t_test_file_location = "output/t_test.csv"
plots_output_directory = 'plots'

fixData.fix(main_source_file_location, cleaned_data_file_location)

perPopulation.add_new_columns(cleaned_data_file_location, per_population_data_file_location)

t_test.save_t_test(per_population_data_file_location, t_test_file_location)

drawer.draw_charts(per_population_data_file_location, plots_output_directory)
