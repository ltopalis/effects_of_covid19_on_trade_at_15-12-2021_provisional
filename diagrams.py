import matplotlib.pyplot as plt

from dataExtractor import *
from textwrap import wrap


def tonnes_diagram_by_months(data):
    _, data_in_tonnes = turnover_by_month(data)

    plt.plot(data_in_tonnes, label='Tonnes', color='red')
    plt.title("Τζίρος ανα Μήνα")
    plt.xlabel("Έτη")
    plt.ylabel("$")
    plt.legend()
    plt.grid()
    plt.show()


def dollars_diagram_by_months(data):
    data_in_dollars, _ = turnover_by_month(data)

    plt.plot(data_in_dollars, label="$")
    plt.title("Τζίρος ανα Μήνα")
    plt.xlabel("Έτη")
    plt.ylabel("$")
    plt.legend()
    plt.grid()
    plt.show()


def tonnes_bar_by_country(data):
    _, data_in_tonnes = turnover_by_country(data)

    country = tuple(data_in_tonnes.index)
    country = ['\n'.join(wrap(l, 9)) for l in country]

    bars = plt.bar(country, data_in_tonnes, color='red', alpha=0.8, width=0.6, label="Τόνοι")
    plt.title("Τζίρος ανα Χώρα")
    plt.xlabel("Χώρα")
    plt.ylabel("Τόνοι")
    plt.bar_label(bars)

    plt.legend()
    plt.show()


def dollars_bar_by_country(data):
    data_in_dollars, _ = turnover_by_country(data)

    country = tuple(data_in_dollars.index)
    country = ['\n'.join(wrap(l, 9)) for l in country]

    bars = plt.bar(country, data_in_dollars, color='blue', alpha=0.8, width=0.6, label="Τόνοι")
    plt.title("Τζίρος ανα Χώρα")
    plt.xlabel("Χώρα")
    plt.ylabel("Τόνοι")
    plt.bar_label(bars)

    plt.legend()
    plt.show()


def tonnes_bar_by_transport(data):
    _, data_in_tonnes = turnover_by_transport(data)

    bars = plt.bar(data_in_tonnes.index, data_in_tonnes, color='blue', alpha=0.8, width=0.6, label="Τόνοι")
    plt.title("Τζίρος ανα Χώρα")
    plt.xlabel("Χώρα")
    plt.ylabel("Τόνοι")
    plt.bar_label(bars)

    plt.legend()
    plt.show()


def dollars_bar_by_transport(data):
    data_in_dollars, _ = turnover_by_transport(data)

    bars = plt.bar(data_in_dollars.index, data_in_dollars, color='blue', alpha=0.8, width=0.6, label="Τόνοι")
    plt.title("Τζίρος ανα Είδος Μεταφορικού Μέσου")
    plt.xlabel("Είδος Μεταφορικού Μέσου")
    plt.ylabel("$")
    plt.bar_label(bars)

    plt.legend()
    plt.show()


def tonnes_bar_by_day(data):
    _, data_in_tonnes = turnover_by_day(data)

    bars = plt.bar(data_in_tonnes.index, data_in_tonnes, color='blue', alpha=0.8, width=0.6, label="Τόνοι")
    plt.title("Τζίρος ανα ημέρα")
    plt.xlabel("Ημέρα")
    plt.ylabel("Τόνοι")
    plt.bar_label(bars)

    plt.legend()
    plt.show()


def dollars_bar_by_day(data):
    data_in_dollars, _ = turnover_by_day(data)

    bars = plt.bar(data_in_dollars.index, data_in_dollars, color='red', alpha=0.8, width=0.6, label="$")
    plt.title("Τζίρος ανα Ημέρα")
    plt.xlabel("Ημέρα")
    plt.ylabel("$")
    plt.bar_label(bars)

    plt.legend()
    plt.show()


def tonnes_bar_by_commodity(data):
    data_in_dollars, _ = turnover_by_commodity(data)

    commodities = list(data_in_dollars.index)

    commodity_list = [
        '\n'.join(wrap(commodity, len(commodity[0:len(commodity) // 2]))) if len(commodity) >= 15 else commodity
        for commodity in commodities]

    plt.barh(commodity_list, data_in_dollars, color='red', alpha=0.8, label='Τόνοι')
    plt.xlabel("Τόνοι")
    plt.ylabel("Κατηγορία Εμπορεύματος")
    plt.title("Τζίρος ανα Κατηγορία Εμπορεύματος")
    plt.legend()
    plt.show()


def dollars_bar_by_commodity(data):
    _, data_in_tonnes = turnover_by_commodity(data)

    commodities = list(data_in_tonnes.index)

    commodity_list = [
        '\n'.join(wrap(commodity, len(commodity[0:len(commodity) // 2]))) if len(commodity) >= 15 else commodity
        for commodity in commodities]

    plt.barh(commodity_list, data_in_tonnes, alpha=0.8, label='$')
    plt.xlabel("$")
    plt.ylabel("Κατηγορία Εμπορεύματος")
    plt.title("Τζίρος ανα Κατηγορία Εμπορεύματος")
    plt.legend()
    plt.show()


def max_dollars_by_month(data, ax, plt, canvas):
    ax.clear()
    data_by_month, _ = max_turnover_by_month(data)

    date_list = []
    for datetime in data_by_month.index:
        date = datetime.date()
        date_list.append(date.strftime("%B %Y"))

    bars = ax.bar(date_list, data_by_month['$'], width=0.6, alpha=0.8, label='$')
    plt.bar_label(bars)
    plt.title("5 μήνες με το μεγαλύτερο τζίρο")
    plt.xlabel("Μήνες")
    plt.ylabel("$")
    plt.legend()
    canvas.draw()


def max_tonnes_by_month(data, ax, plt, canvas):
    ax.clear()
    _, data_by_month = max_turnover_by_month(data)

    date_list = []
    for datetime in data_by_month.index:
        date = datetime.date()
        date_list.append(date.strftime("%B %Y"))

    bars = ax.bar(date_list, data_by_month['Tonnes'], color="red", width=0.6, alpha=0.8, label='Τόνοι')
    plt.bar_label(bars)
    plt.title("5 μήνες με το μεγαλύτερο τζίρο")
    plt.xlabel("Μήνες")
    plt.ylabel("Tonnes")
    plt.legend()
    canvas.draw()


def max_dollars_by_commodity(data, ax, plt, canvas):
    ax.clear()
    data_by_commodity, _ = max_turnover_by_commodity_country(data)

    countries = set()
    commodities = set()
    for (country, commodity) in data_by_commodity.index:
        countries.add(country)
        commodities.add(commodity)

    countries = list(countries)
    commodities = list(commodities)

    data_to_print = {}
    for country in countries:
        for commodity in commodities:
            try:
                value = data_by_commodity.loc[(country, commodity)]['$']
                if country not in data_to_print:
                    if len(commodity) >= 15:
                        commodity = '\n'.join(wrap(commodity, len(commodity[0:len(commodity) // 2])))
                    data_to_print[country] = []
                    data_to_print[country] += [[commodity]]
                    data_to_print[country] += [[value]]
                else:
                    if len(commodity) >= 15:
                        commodity = '\n'.join(wrap(commodity, len(commodity[0:len(commodity) // 2])))
                    data_to_print[country][0] += [commodity]
                    data_to_print[country][1] += [value]
            except KeyError:
                continue

    for country in countries:
        bars = plt.bar(data_to_print[country][0], data_to_print[country][1], label='Tonnes', width=0.6, alpha=0.8)
        plt.title(f"5 κατηγορίες εμπορευμάτων με το μεγαλύτερο τζίρο,\nγια {country}")
        plt.xlabel("Κατηγορία Εμπορεύματος")
        plt.ylabel("Τόνοι")
        plt.bar_label(bars)
        plt.legend()
        plt.show()

def max_tonnes_by_commodity(data, ax, plt, canvas):
    ax.clear()
    _, data_by_commodity = max_turnover_by_commodity_country(data)

    countries = set()
    commodities = set()
    for (country, commodity) in data_by_commodity.index:
        countries.add(country)
        commodities.add(commodity)

    countries = list(countries)
    commodities = list(commodities)

    data_to_print = {}
    for country in countries:
        for commodity in commodities:
            try:
                value = data_by_commodity.loc[(country, commodity)]['Tonnes']
                if country not in data_to_print:
                    if len(commodity) >= 15:
                        commodity = '\n'.join(wrap(commodity, len(commodity[0:len(commodity) // 2])))
                    data_to_print[country] = []
                    data_to_print[country] += [[commodity]]
                    data_to_print[country] += [[value]]
                else:
                    if len(commodity) >= 15:
                        commodity = '\n'.join(wrap(commodity, len(commodity[0:len(commodity) // 2])))
                    data_to_print[country][0] += [commodity]
                    data_to_print[country][1] += [value]
            except KeyError:
                continue

    for country in countries:
        bars = plt.bar(data_to_print[country][0], data_to_print[country][1], label='Tonnes', width=0.6, alpha=0.8)
        plt.title(f"5 κατηγορίες εμπορευμάτων με το μεγαλύτερο τζίρο,\nγια {country}")
        plt.xlabel("Κατηγορία Εμπορεύματος")
        plt.ylabel("Τόνοι")
        plt.bar_label(bars)
        plt.legend()
        plt.show()


def clc(ax, canvas):
    ax.clear()
    canvas.draw()
