from dataExtractor import *

if __name__ == '__main__':
    data = read_data_from_url()

    result = turnover_by_country(data)
    print(result)

    result = turnover_by_day(data)
    print(result)

    result = turnover_by_commodity(data)
    print(result)

    result = turnover_by_month(data)
    print(result)

    result = turnover_by_transport(data)
    print(result)
