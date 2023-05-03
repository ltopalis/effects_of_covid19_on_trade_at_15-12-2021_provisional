import customtkinter
from dataExtractor import *
from textwrap import wrap
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


def turnover_by_commodity():
    value_data_group_by_commodity = data.groupby(['Commodity', 'Measure'], as_index=False)['Value']

    return value_data_group_by_commodity.sum()


def tonnes_diagram_by_months():
    ax.clear()
    data_by_month = turnover_by_month(data)

    values_in_tonnes = data_by_month.loc[data_by_month['Measure'] == 'Tonnes']
    ax.plot(values_in_tonnes['Date'], values_in_tonnes['Value'], 'r', label="Tonnes")
    plt.title("Amount of dollars each month")
    plt.xlabel("Years")
    plt.ylabel("$")
    plt.legend()
    canvas.draw()


def dollars_diagram_by_months():
    ax.clear()
    data_by_month = turnover_by_month(data)

    values_in_dollars = data_by_month.loc[data_by_month['Measure'] == '$']

    ax.plot(values_in_dollars['Date'], values_in_dollars['Value'], label="$")
    plt.title("Amount of tonnes each month")
    plt.xlabel("Years")
    plt.ylabel("Tonnes")
    plt.legend()
    canvas.draw()


def tonnes_bar_by_country():
    ax.clear()
    data_by_country = turnover_by_country(data)

    country = []
    tonnes = []
    for elem in data_by_country:
        country += [elem]
        tonnes += [data_by_country[elem][0]]

    country = tuple(country)
    country = ['\n'.join(wrap(l, 6)) for l in country]
    tonnes = tuple(tonnes)

    ax.bar(country, tonnes, color='red', alpha=0.8, width=0.6, label="Tonnes")

    plt.legend()
    canvas.draw()


def dollars_bar_by_country():
    ax.clear()
    data_by_country = turnover_by_country(data)

    country = []

    dollars = []
    for elem in data_by_country:
        country += [elem]
        dollars += [data_by_country[elem][1]]

    country = tuple(country)
    country = ['\n'.join(wrap(l, 6)) for l in country]
    dollars = tuple(dollars)

    ax.bar(country, dollars, color='blue', alpha=0.8, width=0.6, label="$")

    plt.legend()
    canvas.draw()


def tonnes_bar_by_day():
    ax.clear()
    data_by_day = turnover_by_day(data)

    values_in_tonnes = data_by_day.loc[data_by_day['Measure'] == 'Tonnes']
    values_in_tonnes = values_in_tonnes[['Weekday', 'Value']]

    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    value_list = []
    day = []
    for weekday in weekdays:
        value = values_in_tonnes['Value'].loc[values_in_tonnes['Weekday'] == weekday].sum()
        value_list += [value]
        day += [weekday]

    ax.bar(day, value_list, color='red', width=0.6, alpha=0.8, label='Tonnes')
    plt.xlabel("Weekdays")
    plt.ylabel("Values")
    plt.title("Tonnes each Weekday")
    plt.legend()

    canvas.draw()


def dollars_bar_by_day():
    ax.clear()
    data_by_day = turnover_by_day(data)

    values_in_dollars = data_by_day.loc[data_by_day['Measure'] == '$']
    values_in_dollars = values_in_dollars[['Weekday', 'Value']]

    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    value_list = []
    day = []
    for weekday in weekdays:
        value = values_in_dollars['Value'].loc[values_in_dollars['Weekday'] == weekday].sum()
        value_list += [value]
        day += [weekday]

    ax.bar(day, value_list, width=0.6, alpha=0.8, label='$')
    plt.xlabel("Weekdays")
    plt.ylabel("Values")
    plt.title("Dollars each Weekday")
    plt.legend()
    canvas.draw()


def tonnes_bar_by_transport():
    ax.clear()
    data_by_transport = data[['Transport_Mode', 'Value']].loc[data['Measure'] == 'Tonnes']
    transports = set(data['Transport_Mode'])

    transport_mean = []
    values = []
    for transport in transports:
        value = data_by_transport['Value'].loc[data_by_transport['Transport_Mode'] == transport].sum()
        transport_mean += [transport]
        values += [value]

    bars = ax.bar(transport_mean, values, color='red', width=0.6, alpha=0.8, label='Tonnes')
    plt.xlabel("Transport")
    plt.ylabel("Values")
    plt.title("Tonnes for each Transport mean")
    plt.bar_label(bars)
    plt.legend()
    canvas.draw()


def dollars_bar_by_transport():
    ax.clear()
    data_by_transport = data[['Transport_Mode', 'Value']].loc[data['Measure'] == '$']
    transports = set(data['Transport_Mode'])

    transport_mean = []
    values = []
    for transport in transports:
        value = data_by_transport['Value'].loc[data_by_transport['Transport_Mode'] == transport].sum()
        transport_mean += [transport]
        values += [value]

    bars = ax.bar(transport_mean, values, width=0.6, alpha=0.8, label='$')
    plt.xlabel("Transport")
    plt.ylabel("Values")
    plt.title("Dollars for each Transport mean")
    plt.bar_label(bars)
    plt.legend()
    canvas.draw()


def tonnes_bar_by_commodity():
    ax.clear()
    data_by_commodity = data[['Commodity', 'Value']].loc[data['Measure'] == 'Tonnes']
    commodities = set(data_by_commodity['Commodity'])

    commodity_list = []
    values = []
    for commodity in commodities:
        value = data_by_commodity['Value'].loc[data_by_commodity['Commodity'] == commodity].sum()
        commodity_list += [commodity]
        values += [value]

    commodity_list = ['\n'.join(wrap(commodity, 10)) for commodity in commodity_list]

    ax.barh(commodity_list, values, color='red', alpha=0.8, label='Tonnes')
    plt.xlabel("Commodity")
    plt.ylabel("Values")
    plt.title("Tonnes for each Commodity type")
    plt.legend()
    canvas.draw()


def dollars_bar_by_commodity():
    ax.clear()
    data_by_commodity = data[['Commodity', 'Value']].loc[data['Measure'] == '$']
    commodities = set(data_by_commodity['Commodity'])

    commodity_list = []
    values = []
    for commodity in commodities:
        value = data_by_commodity['Value'].loc[data_by_commodity['Commodity'] == commodity].sum()
        commodity_list += [commodity]
        values += [value]

    commodity_list = ['\n'.join(wrap(commodity, 15)) for commodity in commodity_list]

    ax.barh(commodity_list, values, alpha=0.8, label='$')
    plt.xlabel("Commodity")
    plt.ylabel("Values")
    plt.title("Dollars for each Commodity type")
    plt.legend()
    canvas.draw()

if __name__ == '__main__':
    # read data from file or from web
    data = read_data_from_url("effects-of-covid-19-on-trade-at-15-december-2021-provisional.csv")

    fig, ax = plt.subplots()
    fig.set_figwidth(9)
    fig.set_figheight(9)


    # creating the GUI
    customtkinter.set_appearance_mode("system")
    customtkinter.set_default_color_theme("dark-blue")

    # main window's size is 1556x1000
    root = customtkinter.CTk()
    root.geometry("1556x1000")
    root.resizable(True, True)

    # right side of the GUI - GRAPHICS
    right = customtkinter.CTkFrame(root, 1078, 1000)
    right.pack(side=customtkinter.RIGHT, fill=customtkinter.X, expand=customtkinter.YES)

    canvas = FigureCanvasTkAgg(fig, master=right)
    canvas.get_tk_widget().pack(padx=10, fill=customtkinter.X, expand=customtkinter.YES)
    toolbar = NavigationToolbar2Tk(canvas, right, pack_toolbar=False)
    toolbar.update()
    toolbar.pack(anchor="w", fill=customtkinter.BOTH, expand=True)

    # left side of the GUI - CONTROLS
    left = customtkinter.CTkFrame(root, 478, 1000)

    dollars_months_button = customtkinter.CTkButton(master=left, width=468, height=50,
                                                    text="Συνολική παρουσίαση του τζίρου ανά μήνα ($)",
                                                    command=dollars_diagram_by_months)
    tonnes_months_button = customtkinter.CTkButton(master=left, width=468, height=50,
                                                   text="Συνολική παρουσίαση του τζίρου\nανά μήνα (Tonnes)",
                                                   command=tonnes_diagram_by_months)
    dollars_country_button = customtkinter.CTkButton(master=left, width=468, height=50,
                                                     text="Συνολική παρουσίαση του τζίρου\nγια κάθε χώρα ($)",
                                                     command=dollars_bar_by_country)
    tonnes_country_button = customtkinter.CTkButton(master=left, width=468, height=50,
                                                    text="Συνολική παρουσίαση του τζίρου\nγια κάθε χώρα (Tonnes)",
                                                    command=tonnes_bar_by_country)
    dollars_transport_button = customtkinter.CTkButton(master=left, width=468, height=50,
                                                       text="Συνολική παρουσίαση του τζίρου για\n"
                                                            "κάθε μέσο μεταφοράς ($)",
                                                       command=dollars_bar_by_transport)
    tonnes_transport_button = customtkinter.CTkButton(master=left, width=468, height=50,
                                                      text="Συνολική παρουσίαση του τζίρου για\n"
                                                           "κάθε μέσο μεταφοράς (Tonnes)",
                                                      command=tonnes_bar_by_transport)
    dollars_day_button = customtkinter.CTkButton(master=left, width=468, height=50,
                                                 text="Συνολική παρουσίαση του τζίρου για\n"
                                                      "κάθε μέρα της εβδομάδας ($)",
                                                 command=dollars_bar_by_day)
    tonnes_day_button = customtkinter.CTkButton(master=left, width=468, height=50,
                                                text="Συνολική παρουσίαση του τζίρου για\n"
                                                     "κάθε μέρα της εβδομάδας (Tonnes)",
                                                command=tonnes_bar_by_day)
    dollars_commodity_button = customtkinter.CTkButton(master=left, width=468, height=50,
                                                       text="Συνολική παρουσίαση του τζίρου για\n"
                                                            "κάθε κατηγορία εμπορεύματος ($)",
                                                       command=dollars_bar_by_commodity)
    tonnes_commodity_button = customtkinter.CTkButton(master=left, width=468, height=50,
                                                      text="Συνολική παρουσίαση του τζίρου για\n"
                                                           "κάθε κατηγορία εμπορεύματος (Tonnes)",
                                                      command=tonnes_bar_by_commodity)

    dollars_months_button.pack(pady=5, padx=5)
    tonnes_months_button.pack(pady=5, padx=5)
    dollars_country_button.pack(pady=5, padx=5)
    tonnes_country_button.pack(pady=5, padx=5)
    dollars_transport_button.pack(pady=5, padx=5)
    tonnes_transport_button.pack(pady=5, padx=5)
    dollars_day_button.pack(pady=5, padx=5)
    tonnes_day_button.pack(padx=5, pady=5)
    dollars_commodity_button.pack(pady=5, padx=5)
    tonnes_commodity_button.pack(pady=5, padx=5)

    left.pack(side=customtkinter.LEFT)

    root.mainloop()
