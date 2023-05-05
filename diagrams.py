from dataExtractor import *
from textwrap import wrap


def tonnes_diagram_by_months(data, ax, plt, canvas):
    ax.clear()
    data_by_month = turnover_by_month(data)

    values_in_tonnes = data_by_month.loc[data_by_month['Measure'] == 'Tonnes']
    ax.plot(values_in_tonnes['Date'], values_in_tonnes['Value'], 'r', label="Τόνοι")
    plt.title("Τζίρος ανα Μήνα")
    plt.xlabel("Έτη")
    plt.ylabel("$")
    plt.legend()
    plt.grid()
    canvas.draw()


def dollars_diagram_by_months(data, ax, plt, canvas):
    ax.clear()
    data_by_month = turnover_by_month(data)

    values_in_dollars = data_by_month.loc[data_by_month['Measure'] == '$']

    ax.plot(values_in_dollars['Date'], values_in_dollars['Value'], label="$")
    plt.title("Τζίρος ανα Μήνα")
    plt.xlabel("Έτη")
    plt.ylabel("Τόνοι")
    plt.legend()
    plt.grid()
    canvas.draw()


def tonnes_bar_by_country(data, ax, plt, canvas):
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

    ax.bar(country, tonnes, color='red', alpha=0.8, width=0.6, label="Τόνοι")
    plt.title("Τζίρος ανα Χώρα")
    plt.xlabel("Χώρα")
    plt.ylabel("Τόνοι")

    plt.legend()
    canvas.draw()


def dollars_bar_by_country(data, ax, plt, canvas):
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
    plt.title("Τζίρος ανα Χώρα")
    plt.xlabel("Χώρα")
    plt.ylabel("$")

    plt.legend()
    canvas.draw()


def tonnes_bar_by_day(data, ax, plt, canvas):
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

    ax.bar(day, value_list, color='red', width=0.6, alpha=0.8, label='Τόνοι')
    plt.xlabel("Ημέρα")
    plt.ylabel("Τόνοι")
    plt.title("Τζίρος ανα Ημέρα")
    plt.legend()

    canvas.draw()


def dollars_bar_by_day(data, ax, plt, canvas):
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
    plt.xlabel("Ημέρα")
    plt.ylabel("$")
    plt.title("Τζίρος ανα Ημέρα")
    plt.legend()
    canvas.draw()


def tonnes_bar_by_transport(data, ax, plt, canvas):
    ax.clear()
    data_by_transport = data[['Transport_Mode', 'Value']].loc[data['Measure'] == 'Tonnes']
    transports = set(data['Transport_Mode'])

    transport_mean = []
    values = []
    for transport in transports:
        value = data_by_transport['Value'].loc[data_by_transport['Transport_Mode'] == transport].sum()
        transport_mean += [transport]
        values += [value]

    bars = ax.bar(transport_mean, values, color='red', width=0.6, alpha=0.8, label='Τόνοι')
    plt.xlabel("Μεταφορικό Μέσο")
    plt.ylabel("Τόνοι")
    plt.title("Τζίρος ανα Μεταφορικό Μέσο")
    plt.bar_label(bars)
    plt.legend()
    canvas.draw()


def dollars_bar_by_transport(data, ax, plt, canvas):
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
    plt.xlabel("Μεταφορικό Μέσο")
    plt.ylabel("$")
    plt.title("Τζίρος ανα Μεταφορικό Μέσο")
    plt.bar_label(bars)
    plt.legend()
    canvas.draw()


def tonnes_bar_by_commodity(data, ax, plt, canvas):
    ax.clear()
    data_by_commodity = data[['Commodity', 'Value']].loc[data['Measure'] == 'Tonnes']
    commodities = set(data_by_commodity['Commodity'])

    commodity_list = []
    values = []
    for commodity in commodities:
        value = data_by_commodity['Value'].loc[data_by_commodity['Commodity'] == commodity].sum()
        commodity_list += [commodity]
        values += [value]

    commodity_list = [
        '\n'.join(wrap(commodity, len(commodity[0:len(commodity) // 2]))) if len(commodity) >= 15 else commodity
        for commodity in commodity_list]

    ax.barh(commodity_list, values, color='red', alpha=0.8, label='Τόνοι')
    plt.xlabel("Τόνοι")
    plt.ylabel("Κατηγορία Εμπορεύματος")
    plt.title("Τζίρος ανα Κατηγορία Εμπορεύματος")
    plt.legend()
    canvas.draw()


def dollars_bar_by_commodity(data, ax, plt, canvas):
    ax.clear()
    data_by_commodity = data[['Commodity', 'Value']].loc[data['Measure'] == '$']
    commodities = set(data_by_commodity['Commodity'])

    commodity_list = []
    values = []
    for commodity in commodities:
        value = data_by_commodity['Value'].loc[data_by_commodity['Commodity'] == commodity].sum()
        commodity_list += [commodity]
        values += [value]

    commodity_list = [
        '\n'.join(wrap(commodity, len(commodity[0:len(commodity) // 2]))) if len(commodity) >= 15 else commodity
        for commodity in commodity_list]

    ax.barh(commodity_list, values, alpha=0.8, label='$')
    plt.xlabel("$")
    plt.ylabel("Κατηγορία Εμπορεύματος")
    plt.title("Τζίρος ανα Κατηγορία Εμπορεύματος")
    plt.legend()
    canvas.draw()


def max_dollars_by_month(data, ax, plt, canvas):
    ax.clear()
    data_by_month, _ = max_turnout_by_month(data)

    date_list = []
    for datetime in data_by_month['Date']:
        date = datetime.date()
        date_list.append(date.strftime("%B %Y"))

    values = list(data_by_month['Value'])

    bars = ax.bar(date_list, values, width=0.6, alpha=0.8, label='$')
    plt.bar_label(bars)
    plt.title("5 μήνες με το μεγαλύτερο τζίρο")
    plt.xlabel("Μήνες")
    plt.ylabel("$")
    plt.legend()
    canvas.draw()


def max_tonnes_by_month(data, ax, plt, canvas):
    ax.clear()
    _, data_by_month = max_turnout_by_month(data)

    date_list = []
    for datetime in data_by_month['Date']:
        date = datetime.date()
        date_list.append(date.strftime("%B %Y"))

    values = list(data_by_month['Value'])

    bars = ax.bar(date_list, values, color="red", width=0.6, alpha=0.8, label='Τόνοι')
    plt.bar_label(bars)
    plt.title("5 μήνες με το μεγαλύτερο τζίρο")
    plt.xlabel("Μήνες")
    plt.ylabel("Tonnes")
    plt.legend()
    canvas.draw()


def clc(ax, canvas):
    ax.clear()
    canvas.draw()
