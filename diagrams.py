import pandas
from textwrap import wrap
from matplotlib import pyplot as plt
import dataExtractor as dE


def tonnes_diagram_by_months(dataset_df: pandas.core.frame.DataFrame):
    data_by_month = dE.turnover_by_month(dataset_df)

    values_in_tonnes = data_by_month.loc[data_by_month['Measure'] == 'Tonnes']

    plt.plot(values_in_tonnes['Date'], values_in_tonnes['Value'], 'r')
    plt.title("Amount of dollars each month")
    plt.xlabel("Years")
    plt.ylabel("$")
    plt.show()


def dollars_diagram_by_months(dataset_df: pandas.core.frame.DataFrame):
    data_by_month = dE.turnover_by_month(dataset_df)

    values_in_dollars = data_by_month.loc[data_by_month['Measure'] == '$']

    plt.plot(values_in_dollars['Date'], values_in_dollars['Value'])
    plt.title("Amount of tonnes each month")
    plt.xlabel("Years")
    plt.ylabel("Tonnes")
    plt.show()


def tonnes_bar_by_country(dataset_df: pandas.core.frame.DataFrame):
    data_by_country = dE.turnover_by_country(dataset_df)

    country = []
    tonnes = []
    for elem in data_by_country:
        country += [elem]
        tonnes += [data_by_country[elem][0]]

    country = tuple(country)
    country = ['\n'.join(wrap(l, 6)) for l in country]
    tonnes = tuple(tonnes)

    bars = plt.bar(country, tonnes, color='red', alpha=0.8, width=0.6, label="Tonnes")
    plt.bar_label(bars)

    plt.legend()

    plt.show()


def dollars_bar_by_country(dataset_df: pandas.core.frame.DataFrame):
    data_by_country = dE.turnover_by_country(dataset_df)

    country = []

    dollars = []
    for elem in data_by_country:
        country += [elem]
        dollars += [data_by_country[elem][1]]

    country = tuple(country)
    country = ['\n'.join(wrap(l, 6)) for l in country]
    dollars = tuple(dollars)

    bars = plt.bar(country, dollars, color='blue', alpha=0.8, width=0.6, label="$")
    plt.bar_label(bars)

    plt.legend()

    plt.show()


def tonnes_bar_by_day(dataset_df: pandas.core.frame.DataFrame):
    data_by_day = dE.turnover_by_day(dataset_df)

    values_in_tonnes = data_by_day.loc[data_by_day['Measure'] == 'Tonnes']
    values_in_tonnes = values_in_tonnes[['Weekday', 'Value']]

    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    value_list = []
    day = []
    for weekday in weekdays:
        value = values_in_tonnes['Value'].loc[values_in_tonnes['Weekday'] == weekday].sum()
        value_list += [value]
        day += [weekday]

    bars = plt.bar(day, value_list, color='red', width=0.6, alpha=0.8, label='Tonnes')
    plt.xlabel("Weekdays")
    plt.ylabel("Values")
    plt.title("Tonnes each Weekday")
    plt.legend()
    plt.show()


def dollars_bar_by_day(dataset_df: pandas.core.frame.DataFrame):
    data_by_day = dE.turnover_by_day(dataset_df)

    values_in_dollars = data_by_day.loc[data_by_day['Measure'] == '$']
    values_in_dollars = values_in_dollars[['Weekday', 'Value']]

    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    value_list = []
    day = []
    for weekday in weekdays:
        value = values_in_dollars['Value'].loc[values_in_dollars['Weekday'] == weekday].sum()
        value_list += [value]
        day += [weekday]

    plt.bar(day, value_list, width=0.6, alpha=0.8, label='$')
    plt.xlabel("Weekdays")
    plt.ylabel("Values")
    plt.title("Dollars each Weekday")
    plt.legend()
    plt.show()


def tonnes_bar_by_transport(dataset_df: pandas.core.frame.DataFrame):
    data_by_transport = dataset_df[['Transport_Mode', 'Value']].loc[dataset_df['Measure'] == 'Tonnes']
    transports = set(dataset_df['Transport_Mode'])

    transport_mean = []
    values = []
    for transport in transports:
        value = data_by_transport['Value'].loc[data_by_transport['Transport_Mode'] == transport].sum()
        transport_mean += [transport]
        values += [value]

    bars = plt.bar(transport_mean, values, color='red', width=0.6, alpha=0.8, label='Tonnes')
    plt.xlabel("Transport")
    plt.ylabel("Values")
    plt.title("Tonnes for each Transport mean")
    plt.bar_label(bars)
    plt.legend()
    plt.show()


def dollars_bar_by_transport(dataset_df: pandas.core.frame.DataFrame):
    data_by_transport = dataset_df[['Transport_Mode', 'Value']].loc[dataset_df['Measure'] == '$']
    transports = set(dataset_df['Transport_Mode'])

    transport_mean = []
    values = []
    for transport in transports:
        value = data_by_transport['Value'].loc[data_by_transport['Transport_Mode'] == transport].sum()
        transport_mean += [transport]
        values += [value]

    bars = plt.bar(transport_mean, values, width=0.6, alpha=0.8, label='$')
    plt.xlabel("Transport")
    plt.ylabel("Values")
    plt.title("Dollars for each Transport mean")
    plt.bar_label(bars)
    plt.legend()
    plt.show()


def tonnes_bar_by_commodity(dataset_df: pandas.core.frame.DataFrame):
    data_by_commodity = dataset_df[['Commodity', 'Value']].loc[dataset_df['Measure'] == 'Tonnes']
    commodities = set(data_by_commodity['Commodity'])

    commodity_list = []
    values = []
    for commodity in commodities:
        value = data_by_commodity['Value'].loc[data_by_commodity['Commodity'] == commodity].sum()
        commodity_list += [commodity]
        values += [value]

    commodity_list = ['\n'.join(wrap(commodity, 10)) for commodity in commodity_list]

    bars = plt.barh(commodity_list, values, color='red',  alpha=0.8, label='Tonnes')
    plt.xlabel("Commodity")
    plt.ylabel("Values")
    plt.title("Tonnes for each Commodity type")
    plt.legend()
    plt.show()


def dollars_bar_by_commodity(dataset_df: pandas.core.frame.DataFrame):
    data_by_commodity = dataset_df[['Commodity', 'Value']].loc[dataset_df['Measure'] == '$']
    commodities = set(data_by_commodity['Commodity'])

    commodity_list = []
    values = []
    for commodity in commodities:
        value = data_by_commodity['Value'].loc[data_by_commodity['Commodity'] == commodity].sum()
        commodity_list += [commodity]
        values += [value]

    commodity_list = ['\n'.join(wrap(commodity, 15)) for commodity in commodity_list]

    bars = plt.barh(commodity_list, values, alpha=0.8, label='$')
    plt.xlabel("Commodity")
    plt.ylabel("Values")
    plt.title("Dollars for each Commodity type")
    plt.bar_label(bars)
    plt.legend()
    plt.show()
