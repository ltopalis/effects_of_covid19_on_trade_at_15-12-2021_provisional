import pandas as pd
import os
from tkinter import messagebox

folder_to_save = r"./csv_files/"


def _folder():
    if not os.path.exists(folder_to_save):
        os.makedirs(folder_to_save)


def save_to_csv(data):
    _folder()

    # by day
    tonnes = data.tonnes_by_day
    dollars = data.dollars_by_day
    frames = [tonnes, dollars]
    result = pd.concat(frames, axis=1).reset_index()

    result.to_csv(f"{folder_to_save}weekday.csv", index=False)

    # by commodity
    tonnes = data.tonnes_by_commodity
    dollars = data.dollars_by_commodity
    frames = [tonnes, dollars]
    result = pd.concat(frames, axis=1).reset_index()

    result.to_csv(f"{folder_to_save}commodity.csv", index=False)

    # by country
    tonnes = data.tonnes_by_country
    dollars = data.dollars_by_country
    frames = [tonnes, dollars]
    result = pd.concat(frames, axis=1).reset_index()

    result.to_csv(f"{folder_to_save}country.csv", index=False)

    # by transport
    tonnes = data.tonnes_by_transport
    dollars = data.dollars_by_transport
    frames = [tonnes, dollars]
    result = pd.concat(frames, axis=1).reset_index()

    result.to_csv(f"{folder_to_save}transport_mean.csv", index=False)

    # by month
    tonnes = data.tonnes_by_month
    dollars = data.dollars_by_month
    frames = [tonnes, dollars]
    result = pd.concat(frames, axis=1).reset_index()

    result.to_csv(f"{folder_to_save}month.csv", index=False)

    # Παρουσίαση των 5 μηνών με το μεγαλύτερο τζίρο, ανεξαρτήτως μέσου μεταφοράς και είδους ανακυκλώσιμων ειδών
    tonnes = data.max_tonnes_by_month
    dollars = data.max_dollars_by_month
    frames = [tonnes, dollars]
    result = pd.concat(frames, axis=1).reset_index()

    result.to_csv(f"{folder_to_save}5_max_turnout_by_month.csv", index=False)

    # Παρουσίαση των 5 κατηγοριών εμπορευμάτων με το μεγαλύτερο τζίρο, για κάθε χώρα
    tonnes = data.max_tonnes_by_commodity_in_country
    tonnes['Measure'] = 'Tonnes'

    dollars = data.max_dollars_by_commodity_in_country
    dollars['Measure'] = '$'

    frames = [tonnes, dollars]
    result = pd.concat(frames, axis=0).reset_index()

    result = result.drop('index', axis=1)

    result.to_csv(f"{folder_to_save}5_max_turnout_by_commodity_for_each_country.csv", index=False)

    # Παρουσίαση της ημέρας με το μεγαλύτερο τζίρο, για κάθε κατηγορία εμπορεύματος
    tonnes = data.tonnes_by_day_commodity
    tonnes['Measure'] = 'Tonnes'

    dollars = data.dollars_by_day_commodity
    dollars['Measure'] = '$'

    frames = [tonnes, dollars]
    result = pd.concat(frames, axis=0).reset_index()

    result = result.drop('index', axis=1)

    result.to_csv(f"{folder_to_save}max_turnout_by_day_for_each_commodity.csv", index=False)

    messagebox.showinfo("Επιτυχία", "Τα δεδομένα αποθηκεύτηκαν επιτυχώς!")
