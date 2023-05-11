import pandas
import pandas as pd
import threading


def _read_data_from_url(
        url="https://www.stats.govt.nz/assets/Uploads/Effects-of-COVID-19-on-trade/Effects-of-COVID-19-on-trade-At-15"
            "-December-2021-provisional/Download-data/effects-of-covid-19-on-trade-at-15-december-2021-provisional"
            ".csv"):
    return pd.read_csv(url)


def _turnover_by_month(dataset_df: pd.core.frame.DataFrame):
    temp_df = dataset_df.copy()
    temp_df['Date'] = pd.to_datetime(temp_df['Date'], format="%d/%m/%Y")

    values_monthly_df = temp_df.groupby([pd.Grouper(key='Date', freq='M'), 'Direction', 'Measure'],
                                        as_index=False).sum()

    turnover = pd.pivot_table(values_monthly_df, values='Value', index='Date', columns=['Direction', 'Measure'],
                              aggfunc='sum')

    turnover.fillna(0, inplace=True)

    dollars = turnover['Imports']['$'] + turnover['Reimports']['$'] - turnover['Exports']['$']
    tonnes = -turnover['Exports']['Tonnes']

    dollars = dollars.replace(-0, 0)
    tonnes = tonnes.replace(-0, 0)

    return dollars, tonnes


def _turnover_by_country(dataset_df: pandas.core.frame.DataFrame):
    values_country_df = dataset_df.groupby(['Country', 'Direction', 'Measure'], as_index=False).sum()

    values_country_df = values_country_df[['Country', 'Direction', 'Measure', 'Value']]

    turnover = pd.pivot_table(values_country_df, values='Value', index='Country', columns=['Direction', 'Measure'],
                              aggfunc='sum')

    turnover.fillna(0, inplace=True)

    dollars = turnover['Imports']['$'] + turnover['Reimports']['$'] - turnover['Exports']['$']
    tonnes = - turnover['Exports']['Tonnes']

    dollars = dollars.replace(-0, 0)
    tonnes = tonnes.replace(-0, 0)

    return dollars, tonnes


def _turnover_by_transport(dataset_df: pandas.core.frame.DataFrame) -> pandas.core.frame.DataFrame:
    values_transport_df = dataset_df.groupby(['Transport_Mode', 'Direction', 'Measure'], as_index=False).sum()

    values_transport_df = values_transport_df[['Direction', 'Transport_Mode', 'Measure', 'Value']]

    turnover = pd.pivot_table(values_transport_df, values='Value', index='Transport_Mode',
                              columns=['Direction', 'Measure'],
                              aggfunc='sum')

    turnover.fillna(0, inplace=True)

    dollars = turnover['Imports']['$'] + turnover['Reimports']['$'] - turnover['Exports']['$']
    tonnes = - turnover['Exports']['Tonnes']

    dollars = dollars.replace(-0, 0)
    tonnes = tonnes.replace(-0, 0)

    return dollars, tonnes


def _turnover_by_day(dataset_df: pandas.core.frame.DataFrame) -> pandas.core.frame.DataFrame:
    values_transport_df = dataset_df.groupby(['Weekday', 'Direction', 'Measure'], as_index=False).sum()

    values_transport_df = values_transport_df[['Direction', 'Weekday', 'Measure', 'Value']]

    turnover = pd.pivot_table(values_transport_df, values='Value', index='Weekday',
                              columns=['Direction', 'Measure'],
                              aggfunc='sum')

    turnover.fillna(0, inplace=True)

    dollars = turnover['Imports']['$'] + turnover['Reimports']['$'] - turnover['Exports']['$']
    tonnes = - turnover['Exports']['Tonnes']

    dollars = dollars.replace(-0, 0)
    tonnes = tonnes.replace(-0, 0)

    return dollars, tonnes


def _turnover_by_commodity(dataset_df: pandas.core.frame.DataFrame):
    values_transport_df = dataset_df.groupby(['Commodity', 'Direction', 'Measure'], as_index=False).sum()

    values_transport_df = values_transport_df[['Direction', 'Commodity', 'Measure', 'Value']]

    turnover = pd.pivot_table(values_transport_df, values='Value', index='Commodity',
                              columns=['Direction', 'Measure'],
                              aggfunc='sum')

    turnover.fillna(0, inplace=True)

    dollars = turnover['Imports']['$'] + turnover['Reimports']['$'] - turnover['Exports']['$']
    tonnes = turnover['Imports']['$'] + turnover['Reimports']['$'] - turnover['Exports']['Tonnes']
    tonnes.name = 'Tonnes'

    dollars = dollars.replace(-0, 0)
    tonnes = tonnes.replace(-0, 0)

    return dollars, tonnes


def _max_turnover_by_month(dataset_df: pandas.core.frame.DataFrame):
    dollars, tonnes = _turnover_by_month(dataset_df)

    dollars_df = pd.DataFrame(dollars)
    tonnes_df = pd.DataFrame(tonnes)

    sort_dollars_df = dollars_df.sort_values(by=['$'], ascending=False).head(5)
    sort_tonnes_df = tonnes_df.sort_values(by=['Tonnes'], ascending=False).head(5)

    return sort_dollars_df, sort_tonnes_df


def _max_turnover_by_commodity_country(dataset_df: pandas.core.frame.DataFrame):
    values_commodity_df = dataset_df.groupby(['Country', 'Commodity', 'Direction', 'Measure'], as_index=False).sum()

    values_commodity_df = values_commodity_df[['Country', 'Commodity', 'Direction', 'Measure', 'Value']]

    turnover = pd.pivot_table(values_commodity_df, values='Value', index=['Country', 'Commodity'],
                              columns=['Direction', 'Measure'], aggfunc='sum')

    turnover.fillna(0, inplace=True)

    dollars_dict = {'Country': [], 'Commodity': [], 'Value': []}
    tonnes_dict = {'Country': [], 'Commodity': [], 'Value': []}
    countries = set()
    for (country, commodity) in turnover.index:
        dollars = turnover.loc[country, commodity]['Imports']['$'] + \
                  turnover.loc[country, commodity]['Reimports']['$'] - \
                  turnover.loc[country, commodity]['Exports']['$']

        dollars_dict['Country'] += [country]
        dollars_dict['Commodity'] += [commodity]
        dollars_dict['Value'] += [dollars]

        tonnes = - turnover.loc[country, commodity]['Exports']['Tonnes']

        tonnes_dict['Country'] += [country]
        tonnes_dict['Commodity'] += [commodity]
        tonnes_dict['Value'] += [tonnes]

        countries.add(country)

    dollars_df = pd.DataFrame(dollars_dict)
    tonnes_df = pd.DataFrame(tonnes_dict)

    dollars_dataframe = pd.DataFrame()
    tonnes_dataframe = pd.DataFrame()
    for country in countries:
        temp_dollars_df = dollars_df.loc[dollars_df['Country'] == country]. \
            sort_values(by=['Value'], ascending=False).head(5)
        dollars_dataframe = pd.concat([dollars_dataframe, temp_dollars_df])

        temp_tonnes_df = tonnes_df.loc[tonnes_df['Country'] == country]. \
            sort_values(by=['Value'], ascending=False).head(5)
        tonnes_dataframe = pd.concat([tonnes_dataframe, temp_tonnes_df])

    dollars_dataframe = dollars_dataframe.reset_index()
    tonnes_dataframe = tonnes_dataframe.reset_index()

    dollars_dataframe = dollars_dataframe.drop('index', axis=1)
    tonnes_dataframe = tonnes_dataframe.drop('index', axis=1)

    return dollars_dataframe, tonnes_dataframe


# def _max_turnover_by_commodity_day(dataset_df: pandas.core.frame.DataFrame):
#     values_commodity_df = dataset_df.groupby(['Commodity', 'Weekday', 'Direction', 'Measure'], as_index=False).sum()
#     values_commodity_df = values_commodity_df[['Commodity', 'Weekday', 'Direction', 'Measure', 'Value']]
#
#     turnover = pd.pivot_table(values_commodity_df, values='Value', index=['Weekday', 'Commodity'],
#                               columns=['Direction', 'Measure'], aggfunc='sum')
#     turnover.fillna(0, inplace=True)


class DataExtractor:

    def _thread_function_1(self):
        self.dollars_by_month, self.tonnes_by_month = _turnover_by_month(self.data)
        self.dollars_by_country, self.tonnes_by_country = _turnover_by_country(self.data)
        self.dollars_by_transport, self.tonnes_by_transport = _turnover_by_transport(self.data)
        print("END 1")

    def _thread_function_2(self):
        self.max_dollars_by_month, self.max_tonnes_by_month = _max_turnover_by_month(self.data)
        self.dollars_by_commodity, self.tonnes_by_commodity = _turnover_by_commodity(self.data)
        self.max_dollars_by_month, self.max_tonnes_by_month = _max_turnover_by_month(self.data)
        print("END 2")

    def _thread_function_3(self):
        self.max_dollars_by_commodity_in_country, self.max_tonnes_by_commodity_in_country = \
            _max_turnover_by_commodity_country(self.data)
        self.day_max_dollars_by_commodity, self.day_max_tonnes_by_commodity = \
            _max_turnover_by_commodity_country(self.data)
        print("END 3")

    def _thread_function_4(self):
        self.dollars_by_day, self.tonnes_by_day = _turnover_by_day(self.data)
        self.dollars_by_commodity, self.tonnes_by_commodity = _turnover_by_commodity(self.data)
        print("END 4")

    def __init__(self, csv_file=None):
        if csv_file is None:
            self.data = _read_data_from_url()
        else:
            self.data = _read_data_from_url(csv_file)

        x1 = threading.Thread(target=self._thread_function_1)
        x1.start()

        x2 = threading.Thread(target=self._thread_function_2)
        x2.start()

        x3 = threading.Thread(target=self._thread_function_3)
        x3.start()

        x4 = threading.Thread(target=self._thread_function_4)
        x4.start()

        x1.join()
        x2.join()
        x3.join()
        x4.join()
