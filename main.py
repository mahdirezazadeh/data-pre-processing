import drawer
import fixData
import perPopulation
import t_test

main_source_file_location = "SARS-CoV-2_Dataset.csv"
cleaned_data_file_location = "cleaned_data.csv"
per_population_data_file_location = "per_population_data.csv"
t_test_file_location = "t_test.csv"

# fixData.fix(main_source_file_location, cleaned_data_file_location)

# perPopulation.add_new_columns(cleaned_data_file_location, per_population_data_file_location)

# t_test.save_t_test(per_population_data_file_location, t_test_file_location)

drawer.draw_line_chart(per_population_data_file_location, "/")

# x = np.array(data)

# print(data.dtypes)


# names = [
#     'continent', 'location', 'date', 'total_cases', 'total_deaths',
#     'total_vaccinations', 'people_vaccinated', 'people_fully_vaccinated',
#     'population'
# ]
# for cell in data[]:
#     print(cell)

# print(data.loc[1, names[5]])
# print(pd.isnull(data.loc[1, names[5]]))

# print(len(data['location'].unique()))

# print(data.iloc[:, 0:2])
#
# print(data.iloc[:, 5])
# n_data = data.loc[data[names[1]] == 'Chile']
#
# total_v = list(n_data['total_vaccinations'])
# print(total_v)
#
# print(pd.isnull(total_v[0]))

#
# print(ndata.iloc[:, 8])
# print(ndata.iloc[:, 0:5].dtypes)
#
# x = 1
# for name in names:
#     print(x)
#     x+=1
# print(data[][0])

# print(data.shape)
# print(data)
