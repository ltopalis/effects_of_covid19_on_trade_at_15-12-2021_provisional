import pandas
from textwrap import wrap
from matplotlib import pyplot as plt
import dataExtractor as dE
import numpy as np


def tonnes_diagram_by_months(dataset_df: pandas.core.frame.DataFrame):
    data_by_month = dE.turnover_by_month(dataset_df)

    values_in_tonnes = data_by_month.loc[data_by_month['Measure'] == 'Tonnes']

    plt.plot(values_in_tonnes['Date'], values_in_tonnes['Value'])
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

    bars = plt.bar(country, tonnes, color='blue', alpha=0.8, width=0.6, label="Tonnes")
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

    bars = plt.bar(country, dollars, color='red', alpha=0.8, width=0.6, label="Tonnes")
    plt.bar_label(bars)

    plt.legend()

    plt.show()
