import os

import numpy as np
import pandas as pd
from matplotlib import pyplot
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeRegressor

feature_dates_pre = pd.DataFrame(columns=['date'])


def errors(y_predict, model_predict_data, plot_dir, feature_date):
    df = pd.DataFrame(columns=['feature_date', 'mean_abs_err', 'mean_sq_err', 'r2', 'rms', 'ea_err', 'rrs_err'])
    file = f'{plot_dir}/errors.csv'

    if os.path.exists(file):
        df = pd.read_csv(file)

    feature_date = feature_date
    ea_err = rae(y_predict, model_predict_data)
    r2 = r2_score(y_predict, model_predict_data)
    rrs_err = rrse(y_predict, model_predict_data)
    mean_sq_err = mean_squared_error(y_predict, model_predict_data)
    mean_abs_err = mean_absolute_error(y_predict, model_predict_data)
    rms = mean_squared_error(y_predict, model_predict_data, squared=False)

    df.loc[len(df.index)] = [feature_date, ea_err, r2, rrs_err, mean_sq_err, mean_abs_err, rms]

    df.to_csv(file, index=False)
    if feature_date == 30:
        plot_errors(df, plot_dir)


def plot_errors(df, plot_dir):
    errs = ['mean_abs_err', 'mean_sq_err', 'r2', 'rms', 'ea_err', 'rrs_err']

    for err in errs:
        # ptr = 10
        # pyplot.plot(df['feature_date'][ptr:], df[err][ptr:])
        # pyplot.plot(df['feature_date'][0:ptr], df[err][0:ptr])
        pyplot.plot(df['feature_date'], df[err])
        pyplot.xlabel('date')
        pyplot.ylabel(err)
        pyplot.title(err)
        pyplot.savefig(
            '{}/{}.png'.format(
                plot_dir, err))
        pyplot.legend()
        pyplot.show()


def plot(x_predict, y_predict, model_predict_data, plot_dir, feature_date):
    pyplot.plot(x_predict, y_predict, label='Expected')
    pyplot.plot(x_predict, model_predict_data, label='Predicted')
    pyplot.plot()
    pyplot.title(f'{feature_date} first days')
    pyplot.savefig(
        '{}/{}days.png'.format(
            plot_dir, feature_date))
    pyplot.legend()
    pyplot.show()


def rrse(actual, predicted):
    return np.sqrt(np.sum(np.square(actual - predicted)) /
                   np.sum(np.square(actual - np.mean(actual))))


def rae(actual, predicted):
    numerator = np.sum(np.abs(predicted - actual))
    denominator = np.sum(np.abs(np.mean(actual) - actual))
    return numerator / denominator


def regress(data, target, date_point, model, model_name, plots_output_directory, location):
    plot_dir = '{}/{}/{}/{}'.format(plots_output_directory, model_name, location.split('.')[0], target)
    if not os.path.exists(plot_dir):
        os.makedirs(plot_dir)

    train_data = data.loc[data['date'] <= date_point]

    x_train = train_data['date'][:, None]
    y_train = train_data[target][:, None]

    predict_data = data.loc[data['date'] > date_point]

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

        errors(y_predict, model_predict_data, plot_dir, feature_date)

        plot(x_predict, y_predict, model_predict_data, plot_dir, feature_date)


def regressor_directory(continent_data_directory, plots_output_directory):
    list_data = os.listdir(continent_data_directory)

    targets = ['total_cases', 'total_deaths', 'total_vaccinations', 'people_vaccinated', 'people_fully_vaccinated',
               'new_cases', 'new_deaths', ]

    for data_file in list_data:
        data = pd.read_csv(f'{continent_data_directory}{data_file}')
        for target in targets:
            regress(data, target, 20211031, DecisionTreeRegressor(), 'DecisionTree', plots_output_directory, data_file)
            regress(data, target, 20211031, RandomForestRegressor(), 'RandomForest', plots_output_directory, data_file)
            regress(data, target, 20211031, MultinomialNB(), 'Multinomial', plots_output_directory, data_file)
            regress(data, target, 20211031, GaussianNB(), 'GaussianNB', plots_output_directory, data_file)


def regressor_location(normalized_date_file_location, plots_output_directory):
    data = pd.read_csv(normalized_date_file_location)
    # countries = (data['location'].unique())
    countries = ['Malaysia', 'Argentina', 'Austria', 'Canada', 'United States']

    targets = ['total_cases', 'total_deaths', 'total_vaccinations', 'people_vaccinated', 'people_fully_vaccinated',
               'new_cases', 'new_deaths', ]

    for location in countries:
        for target in targets:
            regress(data.loc[data['location'] == location], target, 20211031, DecisionTreeRegressor(), 'DecisionTree',
                    plots_output_directory, location)
            regress(data.loc[data['location'] == location], target, 20211031, RandomForestRegressor(), 'RandomForest',
                    plots_output_directory, location)
            regress(data.loc[data['location'] == location], target, 20211031, MultinomialNB(), 'Multinomial',
                    plots_output_directory, location)
            regress(data.loc[data['location'] == location], target, 20211031, GaussianNB(), 'GaussianNB',
                    plots_output_directory, location)


def regressor_location_predict(normalized_date_file_location, plots_output_directory):
    feature_date_start = 20211200
    date_list = []

    for i in range(1, 31):
        # feature_dates_pre['date'][len(feature_dates_pre.index)] = [feature_date_start + i]
        date_list.extend([feature_date_start + i])

    feature_dates_pre['date'] = date_list

    data = pd.read_csv(normalized_date_file_location)
    # countries = (data['location'].unique())
    countries = ['Malaysia', 'Argentina', 'Austria', 'Canada', 'United States']

    targets = ['total_cases', 'total_deaths', 'total_vaccinations', 'people_vaccinated', 'people_fully_vaccinated',
               'new_cases', 'new_deaths', ]

    for location in countries:
        for target in targets:
            regress_pre(data.loc[data['location'] == location], target, DecisionTreeRegressor(), 'DecisionTree',
                        plots_output_directory, location)
            regress_pre(data.loc[data['location'] == location], target, RandomForestRegressor(), 'RandomForest',
                        plots_output_directory, location)
            regress_pre(data.loc[data['location'] == location], target, MultinomialNB(), 'Multinomial',
                        plots_output_directory, location)
            regress_pre(data.loc[data['location'] == location], target, GaussianNB(), 'GaussianNB',
                        plots_output_directory, location)


def regressor_directory_pre(continent_data_directory, plots_output_directory):
    list_data = os.listdir(continent_data_directory)

    targets = ['total_cases', 'total_deaths', 'total_vaccinations', 'people_vaccinated', 'people_fully_vaccinated',
               'new_cases', 'new_deaths', ]

    for data_file in list_data:
        data = pd.read_csv(f'{continent_data_directory}{data_file}')
        for target in targets:
            regress_pre(data, target, DecisionTreeRegressor(), 'DecisionTree', plots_output_directory, data_file)
            regress_pre(data, target, RandomForestRegressor(), 'RandomForest', plots_output_directory, data_file)
            regress_pre(data, target, MultinomialNB(), 'Multinomial', plots_output_directory, data_file)
            regress_pre(data, target, GaussianNB(), 'GaussianNB', plots_output_directory, data_file)


def regress_pre(data, target, model, model_name, plots_output_directory, location):
    plot_dir = '{}/{}/{}/{}'.format(plots_output_directory, model_name, location.split('.')[0], target)
    if not os.path.exists(plot_dir):
        os.makedirs(plot_dir)

    train_data = data

    x_train = train_data['date'][:, None]
    y_train = train_data[target][:, None]

    try:
        model.fit(x_train, y_train)
    except:
        print(f'exception occurred on training {plot_dir}')
        return

    feature_date_start = max(x_train)[0]
    feature_dates = [7, 14, 21, 28, 30]

    for feature_date in feature_dates:
        fp_date = feature_date_start + feature_date

        x_predict = feature_dates_pre.loc[feature_dates_pre['date'] < fp_date]['date']

        x_predict = x_predict[:, None]

        try:
            model_predict_data = model.predict(x_predict)
            plot_pre(x_predict, model_predict_data, plot_dir, feature_date)
        except:
            print(f'exception occurred on training {plot_dir}')
            return


def plot_pre(x_predict, model_predict_data, plot_dir, feature_date):
    pyplot.plot(x_predict, model_predict_data, label='Predicted')
    pyplot.plot()
    pyplot.title(f'{feature_date} first days')
    pyplot.savefig(
        '{}/pre_{}days.png'.format(
            plot_dir, feature_date))
    pyplot.legend()
    pyplot.show()
