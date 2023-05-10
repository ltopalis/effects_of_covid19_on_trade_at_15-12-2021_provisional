from GUIs import *
from dataExtractor import DataExtractor

de = None


def main():
    de = DataExtractor()
    main_gui(de)


if __name__ == '__main__':
    # data = read_data_from_url("effects-of-covid-19-on-trade-at-15-december-2021-provisional.csv")
    # # #
    # # # # print(data.columns)
    # max_turnover_by_commodity_day(data)

    # print(data)
    # print(type(x))
    # print(x)
    # print('-------------------------------------------------------------------')
    # print(y)

    main()
