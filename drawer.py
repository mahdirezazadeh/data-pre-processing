import pandas as pd
# from matplotlip import pyplot as plt


def draw_line_chart(src, dest):
    data = pd.read_csv(src)
    # ts = pd.Series(
    #     data['total_deaths_per_population'], index=data['date'])
    # ts.cumsum()
    # ts.plot()

    data.set_index('date', inplace=True)
    data.plot.line(figsize=(20, 10))
    # plt.show()
    # plt.pyplot.show()

    # data.plot(x=data['people_fully_vaccinated_per_population'], y=data['date'], kind='line')
    # plt.show()

    # data.plot(x=data['total_cases_per_population'], y=data['date'], kind='line')
    # plt.show()

    # data.plot(x=data['total_deaths'], y=data['date'], kind='line')
    # plt.show()

    # data.plot(x=data['people_fully_vaccinated'], y=data['date'], kind='line')
    # plt.show()

    # data.plot(x=data['total_cases'], y=data['date'], kind='line')
    # plt.show()

    # data.plot(x=data['total_vaccinations'], y=data['date'], kind='line')
    # plt.show()

    # data.plot(x=data['people_vaccinated'], y=data['date'], kind='line')
    # plt.show()

    # data.plot(x=data['people_fully_vaccinated'], y=data['date'], kind='line')
    # plt.show()

    # data.plot(x=data['total_vaccinations'], y=data['continent'], kind='line')
    # plt.show()

    # data.plot(x=data['people_vaccinated'], y=data['continent'], kind='line')
    # plt.show()

    # data.plot(x=data['total_deaths'], y=data['continent'], kind='line')
    # plt.show()

    # data.plot(x=data['people_fully_vaccinated'], y=data['continent'], kind='line')
    # plt.show()

    # data.plot(x=data['total_cases'], y=data['continent'], kind='line')
    # plt.show()
