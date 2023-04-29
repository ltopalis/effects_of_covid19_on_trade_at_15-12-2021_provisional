from dataExtractor import *
from diagrams import *

if __name__ == '__main__':
    data = read_data_from_url("effects-of-covid-19-on-trade-at-15-december-2021-provisional.csv")

    tonnes_diagram_by_months(data)
    dollars_diagram_by_months(data)

    tonnes_bar_by_country(data)
    dollars_bar_by_country(data)

    # result = turnover_by_day(data)
    # print(result, end="\n\n")
    #
    # result = turnover_by_commodity(data)
    # print(result, end="\n\n")

    # result = turnover_by_transport(data)
    # print(result)



