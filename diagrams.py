import matplotlib.pyplot as plt
from textwrap import wrap


def tonnes_diagram_by_months(data):
    plt.plot(data, label='Tonnes', color='red')
    plt.title("Τζίρος ανα Μήνα")
    plt.xlabel("Έτη")
    plt.ylabel("$")
    plt.legend()
    plt.grid()
    plt.show()


def dollars_diagram_by_months(data):
    plt.plot(data, label="$")
    plt.title("Τζίρος ανα Μήνα")
    plt.xlabel("Έτη")
    plt.ylabel("$")
    plt.legend()
    plt.grid()
    plt.show()


def tonnes_bar_by_country(data):
    country = tuple(data.index)
    country = ['\n'.join(wrap(l, 9)) for l in country]

    bars = plt.bar(country, data, color='red', alpha=0.8, width=0.6, label="Τόνοι")
    plt.title("Τζίρος ανα Χώρα")
    plt.xlabel("Χώρα")
    plt.ylabel("Τόνοι")
    plt.bar_label(bars)

    plt.legend()
    plt.show()


def dollars_bar_by_country(data):
    country = tuple(data.index)
    country = ['\n'.join(wrap(l, 9)) for l in country]

    bars = plt.bar(country, data, color='blue', alpha=0.8, width=0.6, label="Τόνοι")
    plt.title("Τζίρος ανα Χώρα")
    plt.xlabel("Χώρα")
    plt.ylabel("Τόνοι")
    plt.bar_label(bars)

    plt.legend()
    plt.show()


def tonnes_bar_by_transport(data):
    bars = plt.bar(data.index, data, color='blue', alpha=0.8, width=0.6, label="Τόνοι")
    plt.title("Τζίρος ανα Χώρα")
    plt.xlabel("Χώρα")
    plt.ylabel("Τόνοι")
    plt.bar_label(bars)

    plt.legend()
    plt.show()


def dollars_bar_by_transport(data):
    bars = plt.bar(data.index, data, color='blue', alpha=0.8, width=0.6, label="Τόνοι")
    plt.title("Τζίρος ανα Είδος Μεταφορικού Μέσου")
    plt.xlabel("Είδος Μεταφορικού Μέσου")
    plt.ylabel("$")
    plt.bar_label(bars)

    plt.legend()
    plt.show()


def tonnes_bar_by_day(data):
    bars = plt.bar(data.index, data, color='blue', alpha=0.8, width=0.6, label="Τόνοι")
    plt.title("Τζίρος ανα ημέρα")
    plt.xlabel("Ημέρα")
    plt.ylabel("Τόνοι")
    plt.bar_label(bars)

    plt.legend()
    plt.show()


def dollars_bar_by_day(data):
    bars = plt.bar(data.index, data, color='red', alpha=0.8, width=0.6, label="$")
    plt.title("Τζίρος ανα Ημέρα")
    plt.xlabel("Ημέρα")
    plt.ylabel("$")
    plt.bar_label(bars)

    plt.legend()
    plt.show()


def tonnes_bar_by_commodity(data):
    commodities = list(data.index)

    commodity_list = [
        '\n'.join(wrap(commodity, len(commodity[0:len(commodity) // 2]))) if len(commodity) >= 15 else commodity
        for commodity in commodities]

    plt.barh(commodity_list, data, color='red', alpha=0.8, label='Τόνοι')
    plt.xlabel("Τόνοι")
    plt.ylabel("Κατηγορία Εμπορεύματος")
    plt.title("Τζίρος ανα Κατηγορία Εμπορεύματος")
    plt.legend()
    plt.show()


def dollars_bar_by_commodity(data):
    commodities = list(data.index)

    commodity_list = [
        '\n'.join(wrap(commodity, len(commodity[0:len(commodity) // 2]))) if len(commodity) >= 15 else commodity
        for commodity in commodities]

    plt.barh(commodity_list, data, alpha=0.8, label='$')
    plt.xlabel("$")
    plt.ylabel("Κατηγορία Εμπορεύματος")
    plt.title("Τζίρος ανα Κατηγορία Εμπορεύματος")
    plt.legend()
    plt.show()


def max_dollars_by_month(data):
    date_list = []
    for datetime in data.index:
        date = datetime.date()
        date_list.append(date.strftime("%B %Y"))

    bars = plt.bar(date_list, data['$'], width=0.6, alpha=0.8, label='$')
    plt.bar_label(bars)
    plt.title("5 μήνες με το μεγαλύτερο τζίρο")
    plt.xlabel("Μήνες")
    plt.ylabel("$")
    plt.legend()
    plt.show()


def max_tonnes_by_month(data):
    date_list = []
    for datetime in data.index:
        date = datetime.date()
        date_list.append(date.strftime("%B %Y"))

    bars = plt.bar(date_list, data['Tonnes'], color="red", width=0.6, alpha=0.8, label='Τόνοι')
    plt.bar_label(bars)
    plt.title("5 μήνες με το μεγαλύτερο τζίρο")
    plt.xlabel("Μήνες")
    plt.ylabel("Tonnes")
    plt.legend()
    plt.show()


def max_dollars_by_commodity(data):
    countries = set()

    for country in data['Country']:
        countries.add(country)

    for country in countries:
        df = data.loc[data['Country'] == country]

        bars = plt.bar(df['Commodity'], df['Value'], width=0.6, alpha=0.8, label='$')
        plt.bar_label(bars)
        plt.title(f"5 κατηγορίες εμπορευμάτων με το μεγαλύτερο τζίρο,\nγια {country}")
        plt.xlabel("Κατηγορία Εμπορεύματος")
        plt.ylabel("$")
        plt.legend()
        plt.show()


def max_tonnes_by_commodity(data):
    countries = set()

    for country in data['Country']:
        countries.add(country)

    for country in countries:
        df = data.loc[data['Country'] == country]

        bars = plt.bar(df['Commodity'], df['Value'], width=0.6, alpha=0.8, label='Tonnes', color="red")
        plt.bar_label(bars)
        plt.title(f"5 κατηγορίες εμπορευμάτων με το μεγαλύτερο τζίρο,\nγια {country}")
        plt.xlabel("Κατηγορία Εμπορεύματος")
        plt.ylabel("Tonnes")
        plt.legend()
        plt.show()


def clc(ax, canvas):
    ax.clear()
    canvas.draw()
