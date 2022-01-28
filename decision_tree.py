import os
from pathlib import Path

import numpy as np
import pandas as pd
from matplotlib import pyplot
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error


def rrse(actual, predicted):
    return np.sqrt(np.sum(np.square(actual.to_numpy() - predicted.to_numpy())) / np.sum(
        np.square(actual.to_numpy() - np.mean(actual.to_numpy()))))


def rae(actual, predicted):
    numerator = np.sum(np.abs(predicted - actual))
    denominator = np.sum(np.abs(np.mean(actual) - actual))
    return numerator / denominator


def regress(data, target, date_point, model, model_name, plots_output_directory, location):
    plot_dir = '{}/{}/{}/{}'.format(plots_output_directory, model_name, location.split('.')[0], target)
    if not os.path.exists(plot_dir):
        os.makedirs(plot_dir)
    # Path(plot_dir).mkdir(parents=True, exist_ok=True)
    train_data = data.loc[data['date'] <= date_point]

    x_train = train_data['date']
    y_train = train_data[target]
    x_train = x_train[:, None]
    y_train = y_train[:, None]

    predict_data = data.loc[data['date'] > date_point]

    # x_predict = predict_data['date']
    # y_predict = predict_data[target]
    # model = DecisionTreeRegressor()
    # x_train = np.array(x_train)
    try:
        model.fit(x_train, y_train)
    except:
        print(f'exception occurred on training {plot_dir}')
        return

    feature_date_start = 20211100
    feature_dates = [7, 14, 21, 28, 30]

    for feature_date in feature_dates:
        fp_date = feature_date_start + feature_date

        x_predict = predict_data.loc[predict_data['date'] < fp_date]['date']
        y_predict = predict_data.loc[predict_data['date'] < fp_date][target]

        x_predict = x_predict[:, None]
        y_predict = y_predict[:, None]

        model_predict_data = model.predict(x_predict)

        mean_abs_err = mean_absolute_error(y_predict, model_predict_data)
        mean_sq_err = mean_squared_error(y_predict, model_predict_data)
        r2 = r2_score(y_predict, model_predict_data)
        rms = mean_squared_error(y_predict, model_predict_data, squared=False)
        ea_err = rae(y_predict, model_predict_data)
        # rrs_err = rrse(y_predict, model_predict_data)
        # print(f'mean_abs_err: {mean_abs_err}\nmean_sq_err:{mean_sq_err}\nr2:{r2}\nrms:{rms}
        # \neae:{ea_err}\nrrse:{rrs_err}')
        print(f'mean_abs_err: {mean_abs_err}\nmean_sq_err:{mean_sq_err}\nr2:{r2}\nrms:{rms}\neae:{ea_err}')

        pyplot.plot(x_predict, y_predict, label='Expected')
        pyplot.plot(x_predict, model_predict_data, label='Predicted')
        # pyplot.plot(x_train, y_train, label='trained')
        pyplot.plot()
        pyplot.title(f'{feature_date} first days')
        pyplot.savefig(
            '{}/{}days.png'.format(
                plot_dir, feature_date))
        pyplot.legend()
        pyplot.show()


def regressor_directory(continent_data_directory, plots_output_directory):
    list_data = os.listdir(continent_data_directory)

    targets = ['total_cases', 'total_deaths', 'total_vaccinations', 'people_vaccinated', 'people_fully_vaccinated',
               'new_cases', 'new_deaths', ]

    for data_file in list_data:
        data = pd.read_csv(f'{continent_data_directory}{data_file}')
        for target in targets:
            # regress(data, target, 20211031, DecisionTreeRegressor(), 'DecisionTree', plots_output_directory, data_file)
            # regress(data, target, 20211031, RandomForestRegressor(), 'RandomForest', plots_output_directory, data_file)
            regress(data, target, 20211031, MultinomialNB(), 'Multinomial', plots_output_directory, data_file)


# def regressor_country(normalized_date_file_location, plots_output_directory):
#     countries = []

