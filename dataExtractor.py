import pandas
import pandas as pd


def read_data_from_url(
        url="https://www.stats.govt.nz/assets/Uploads/Effects-of-COVID-19-on-trade/Effects-of-COVID-19-on-trade-At-15"
            "-December-2021-provisional/Download-data/effects-of-covid-19-on-trade-at-15-december-2021-provisional"
            ".csv"):
    return pd.read_csv(url)


def turnover_by_month(dataset_df: pd.core.frame.DataFrame):
    temp_df = dataset_df.copy()
    temp_df['Date'] = pd.to_datetime(temp_df['Date'], format="%d/%m/%Y")

    values_monthly_df = temp_df.groupby([pd.Grouper(key='Date', freq='M'), 'Direction', 'Measure'],
                                        as_index=False).sum()

    turnover = pd.pivot_table(values_monthly_df, values='Value', index='Date', columns=['Direction', 'Measure'],
                              aggfunc='sum')

    turnover.fillna(0, inplace=True)

    dollars = turnover['Imports']['$'] + turnover['Reimports']['$'] - turnover['Exports']['$']
    tonnes = -turnover['Exports']['Tonnes']

    return dollars, tonnes


def turnover_by_country(dataset_df: pandas.core.frame.DataFrame):
    values_country_df = dataset_df.groupby(['Country', 'Direction', 'Measure'], as_index=False).sum()

    values_country_df = values_country_df[['Country', 'Direction', 'Measure', 'Value']]

    turnover = pd.pivot_table(values_country_df, values='Value', index='Country', columns=['Direction', 'Measure'],
                              aggfunc='sum')

    turnover.fillna(0, inplace=True)

    dollars = turnover['Imports']['$'] + turnover['Reimports']['$'] - turnover['Exports']['$']
    tonnes = - turnover['Exports']['Tonnes']

    return dollars, tonnes


def turnover_by_transport(dataset_df: pandas.core.frame.DataFrame) -> pandas.core.frame.DataFrame:
    values_transport_df = dataset_df.groupby(['Transport_Mode', 'Direction', 'Measure'], as_index=False).sum()

    values_transport_df = values_transport_df[['Direction', 'Transport_Mode', 'Measure', 'Value']]

    turnover = pd.pivot_table(values_transport_df, values='Value', index='Transport_Mode',
                              columns=['Direction', 'Measure'],
                              aggfunc='sum')

    turnover.fillna(0, inplace=True)

    dollars = turnover['Imports']['$'] + turnover['Reimports']['$'] - turnover['Exports']['$']
    tonnes = - turnover['Exports']['Tonnes']

    return dollars, tonnes


def turnover_by_day(dataset_df: pandas.core.frame.DataFrame) -> pandas.core.frame.DataFrame:
    values_transport_df = dataset_df.groupby(['Weekday', 'Direction', 'Measure'], as_index=False).sum()

    values_transport_df = values_transport_df[['Direction', 'Weekday', 'Measure', 'Value']]

    turnover = pd.pivot_table(values_transport_df, values='Value', index='Weekday',
                              columns=['Direction', 'Measure'],
                              aggfunc='sum')

    turnover.fillna(0, inplace=True)

    dollars = turnover['Imports']['$'] + turnover['Reimports']['$'] - turnover['Exports']['$']
    tonnes = - turnover['Exports']['Tonnes']

    return dollars, tonnes


def turnover_by_commodity(dataset_df: pandas.core.frame.DataFrame):
    values_transport_df = dataset_df.groupby(['Commodity', 'Direction', 'Measure'], as_index=False).sum()

    values_transport_df = values_transport_df[['Direction', 'Commodity', 'Measure', 'Value']]

    turnover = pd.pivot_table(values_transport_df, values='Value', index='Commodity',
                              columns=['Direction', 'Measure'],
                              aggfunc='sum')

    turnover.fillna(0, inplace=True)

    dollars = turnover['Imports']['$'] + turnover['Reimports']['$'] - turnover['Exports']['$']
    tonnes = turnover['Imports']['$'] + turnover['Reimports']['$'] - turnover['Exports']['Tonnes']

    return dollars, tonnes


def max_turnover_by_month(dataset_df: pandas.core.frame.DataFrame):
    dollars, tonnes = turnover_by_month(dataset_df)

    dollars_df = pd.DataFrame(dollars)
    tonnes_df = pd.DataFrame(tonnes)

    sort_dollars_df = dollars_df.sort_values(by=['$'], ascending=False).head(5)
    sort_tonnes_df = tonnes_df.sort_values(by=['Tonnes'], ascending=False).head(5)

    return sort_dollars_df, sort_tonnes_df


def max_turnover_by_commodity_country(dataset_df: pandas.core.frame.DataFrame):
    values_commodity_df = dataset_df.groupby(['Country', 'Commodity', 'Direction', 'Measure'], as_index=False).sum()

    values_commodity_df = values_commodity_df[['Country', 'Commodity', 'Direction', 'Measure', 'Value']]

    turnover = pd.pivot_table(values_commodity_df, values='Value', index=['Country', 'Commodity'],
                              columns=['Direction', 'Measure'], aggfunc='sum')

    turnover.fillna(0, inplace=True)

    dollars = dict()
    tonnes = dict()
    countries = []
    for (country, commodity) in turnover.index:
        dollar_value = turnover.loc[country, commodity]['Imports']['$'] + turnover.loc[country, commodity]['Reimports'][
            '$'] \
                       - turnover.loc[country, commodity]['Exports']['$']
        tonnes_value = - turnover.loc[country, commodity]['Exports']['Tonnes']

        countries.append(country)

        dollars['$'] = dollar_value
        tonnes['Tonnes'] = tonnes_value

    dollars_df = pd.DataFrame(data=dollars, index=turnover.index)
    tonnes_df = pd.DataFrame(data=tonnes, index=turnover.index)

    countries = set(countries)

    def get_top_5(group):
        return group.head(5)

    dollars_dataframe = pd.DataFrame()
    tonnes_dataframe = pd.DataFrame()
    for country in countries:
        dollars_return_df = dollars_df.loc[country].apply(lambda x: get_top_5(x))
        dollars_return_df['Country'] = country
        dollars_dataframe = pd.concat([dollars_dataframe, dollars_return_df])

        tonnes_return_df = tonnes_df.loc[country].apply(lambda x: get_top_5(x))
        tonnes_return_df['Country'] = country
        tonnes_dataframe = pd.concat([tonnes_dataframe, tonnes_return_df])

    dollars_dataframe = dollars_dataframe.groupby(by=['Country', 'Commodity']).sum()
    tonnes_dataframe = tonnes_dataframe.groupby(by=['Country', 'Commodity']).sum()

    # print(tonnes_dataframe)
    return dollars_dataframe, tonnes_dataframe


def max_turnover_by_commodity_day(dataset_df: pandas.core.frame.DataFrame):
    values_commodity_df = dataset_df.groupby(['Commodity', 'Weekday', 'Direction', 'Measure'], as_index=False).sum()
    values_commodity_df = values_commodity_df[['Commodity', 'Weekday', 'Direction', 'Measure', 'Value']]

    turnover = pd.pivot_table(values_commodity_df, values='Value', index=['Weekday', 'Commodity'],
                              columns=['Direction', 'Measure'], aggfunc='sum')
    turnover.fillna(0, inplace=True)


