import pandas as pd
from datetime import datetime


def read_data_from_url(
        url="https://www.stats.govt.nz/assets/Uploads/Effects-of-COVID-19-on-trade/Effects-of-COVID-19-on-trade-At-15"
            "-December-2021-provisional/Download-data/effects-of-covid-19-on-trade-at-15-december-2021-provisional"
            ".csv"):
    return pd.read_csv(url)


def turnover_by_country(dataset):
    countries = list(set(dataset['Country']))

    results = dict()
    for country in countries:
        data_in_tones = dataset.loc[dataset['Country'] == country].loc[dataset['Measure'] == 'Tonnes']
        data_in_dollars = dataset.loc[dataset['Country'] == country].loc[dataset['Measure'] == '$']

        sum_in_tones = data_in_tones['Value'].sum()
        sum_in_dollars = data_in_dollars['Value'].sum()

        value = (sum_in_tones, sum_in_dollars)
        results[country] = value

    return results


data = read_data_from_url("effects-of-covid-19-on-trade-at-15-december-2021-provisional.csv")
result = turnover_by_country(data)
print(result)
