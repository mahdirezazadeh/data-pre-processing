import os

import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
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


def regress(data, target, date_point, model):
    train_data = data.loc[data['date'] <= date_point]

    x_train = train_data['date']
    y_train = train_data[target]
    x_train = x_train[:, None]
    y_train = y_train[:, None]

    predict_data = data.loc[data['date'] > date_point]

    x_predict = predict_data['date']
    y_predict = predict_data[target]
    # model = DecisionTreeRegressor()
    # x_train = np.array(x_train)
    x_predict = x_predict[:, None]
    y_predict = y_predict[:, None]
    model.fit(x_train, y_train)

    model_predict_data = model.predict(x_predict)
    mean_abs_err = mean_absolute_error(y_predict, model_predict_data)
    mean_sq_err = mean_squared_error(y_predict, model_predict_data)
    r2 = r2_score(y_predict, model_predict_data)
    rms = mean_squared_error(y_predict, model_predict_data, squared=False)
    ea_err = rae(y_predict, model_predict_data)
    # rrs_err = rrse(y_predict, model_predict_data)
    # print(f'mean_abs_err: {mean_abs_err}\nmean_sq_err:{mean_sq_err}\nr2:{r2}\nrms:{rms}\neae:{ea_err}\nrrse:{rrs_err}')
    print(f'mean_abs_err: {mean_abs_err}\nmean_sq_err:{mean_sq_err}\nr2:{r2}\nrms:{rms}\neae:{ea_err}')


def regressor_directory(continent_data_directory):
    list_data = os.listdir(continent_data_directory)

    targets = ['total_cases', 'total_deaths', 'total_vaccinations', 'people_vaccinated', 'people_fully_vaccinated',
               'new_cases', 'new_deaths', ]

    for data_file in list_data:
        data = pd.read_csv(f'{continent_data_directory}{data_file}')
        for target in targets:
            regress(data, target, 20211031, DecisionTreeRegressor())
