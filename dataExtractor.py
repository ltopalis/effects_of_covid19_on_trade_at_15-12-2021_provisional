import pandas as pd
from datetime import datetime

import pandas.core.frame


def read_data_from_url(
        url="https://www.stats.govt.nz/assets/Uploads/Effects-of-COVID-19-on-trade/Effects-of-COVID-19-on-trade-At-15"
            "-December-2021-provisional/Download-data/effects-of-covid-19-on-trade-at-15-december-2021-provisional"
            ".csv"):
    return pd.read_csv(url)


def turnover_by_month(dataset: pandas.core.frame.DataFrame):
    # ['tonnes', '$']
    results = dict()
    for month in range(1, 13):
        results[str(month)] = [0, 0]
    for i in range(len(dataset['Date'])):
        date = datetime.strptime(dataset['Date'][i], "%d/%m/%Y").date()
        month = date.month
        if dataset['Measure'][i] == 'Tonnes':
            results[str(month)][0] += dataset['Value'][i]
        else:
            results[str(month)][1] += dataset['Value'][i]

    for month in range(1, 12):
        results[str(month)] = tuple(results[str(month)])

    return results


def turnover_by_country(dataset: pandas.core.frame.DataFrame):
    # ('Tonnes', '$')
    countries = list(set(dataset['Country']))

    results = dict()
    for country in countries:
        data_in_tones = dataset.loc[(dataset['Country'] == country) & (dataset['Measure'] == 'Tonnes')]
        data_in_dollars = dataset.loc[(dataset['Country'] == country) & (dataset['Measure'] == '$')]

        sum_in_tones = data_in_tones['Value'].sum()
        sum_in_dollars = data_in_dollars['Value'].sum()

        value = (sum_in_tones, sum_in_dollars)
        results[country] = value

    return results


def turnover_by_transport(dataset: pandas.core.frame.DataFrame):
    # ('tonnes', '$')
    transports = set(dataset['Transport_Mode'])

    results = dict()

    for transport in transports:
        value_in_tonnes = dataset.loc[(dataset['Transport_Mode'] == transport) & (dataset['Measure'] == 'Tonnes')]
        value_in_dollars = dataset.loc[(dataset['Transport_Mode'] == transport) & (dataset['Measure'] == '$')]

        sum_in_tonnes = value_in_tonnes['Value'].sum()
        sum_in_dollars = value_in_dollars['Value'].sum()

        results[transport] = (sum_in_tonnes, sum_in_dollars)

    return results


def turnover_by_day(dataset: pandas.core.frame.DataFrame):
    # (Tonnes, $)
    days = set(dataset['Weekday'])

    results = dict()
    for day in days:
        value_in_tonnes = dataset.loc[(dataset['Weekday'] == day) & (dataset['Measure'] == 'Tonnes')]
        value_in_dollars = dataset.loc[(dataset['Weekday'] == day) & (dataset['Measure'] == '$')]

        sum_in_tonnes = value_in_tonnes['Value'].sum()
        sum_in_dollars = value_in_dollars['Value'].sum()

        results[day] = (sum_in_tonnes, sum_in_dollars)

    return results


def turnover_by_commodity(dataset: pandas.core.frame.DataFrame):
    commodities = set(dataset['Commodity'])

    results = dict()
    for commodity in commodities:
        value_by_tonnes = dataset.loc[(dataset['Commodity'] == commodity) & (dataset['Measure'] == 'Tonnes')]
        value_by_dollars = dataset.loc[(dataset['Commodity'] == commodity) & (dataset['Measure'] == '$')]

        sum_in_tonnes = value_by_tonnes['Value'].sum()
        sum_in_dollars = value_by_dollars['Value'].sum()

        value = (sum_in_tonnes, sum_in_dollars)
        results[commodity] = value

    return results
