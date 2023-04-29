import pandas as pd
import pandas.core.frame


def read_data_from_url(
        url="https://www.stats.govt.nz/assets/Uploads/Effects-of-COVID-19-on-trade/Effects-of-COVID-19-on-trade-At-15"
            "-December-2021-provisional/Download-data/effects-of-covid-19-on-trade-at-15-december-2021-provisional"
            ".csv"):
    return pd.read_csv(url)


def turnover_by_month(dataset_df: pandas.core.frame.DataFrame):
    dataset_df['Date'] = pd.to_datetime(dataset_df['Date'], format="%d/%m/%Y")

    values_monthly_df = dataset_df.groupby([pd.Grouper(key='Date', freq='M'), 'Measure'], as_index=False)['Value'].sum()

    return values_monthly_df


def turnover_by_country(dataset_df: pandas.core.frame.DataFrame):
    value_data_group_by_country = dataset_df.groupby(['Country', 'Measure'], as_index=False)['Value']

    return value_data_group_by_country.sum()


def turnover_by_transport(dataset_df: pandas.core.frame.DataFrame):
    value_data_group_by_transport = dataset_df.groupby(['Transport_Mode', 'Measure'], as_index=False)['Value']

    return value_data_group_by_transport.sum()


def turnover_by_day(dataset_df: pandas.core.frame.DataFrame):
    value_data_group_by_weekday = dataset_df.groupby(['Weekday', 'Measure'], as_index=False)['Value']

    return value_data_group_by_weekday.sum()


def turnover_by_commodity(dataset_df: pandas.core.frame.DataFrame):
    value_data_group_by_commodity = dataset_df.groupby(['Commodity', 'Measure'], as_index=False)['Value']

    return value_data_group_by_commodity.sum()
