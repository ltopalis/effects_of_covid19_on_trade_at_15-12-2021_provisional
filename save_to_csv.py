import pandas as pd
import os

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

    result.to_csv(f"{folder_to_save}/weekday.csv", index=False)

    # by commodity
    tonnes = data.tonnes_by_commodity
    dollars = data.dollars_by_commodity
    frames = [tonnes, dollars]
    result = pd.concat(frames, axis=1).reset_index()

    result.to_csv(f"{folder_to_save}/commodity.csv", index=False)

    # by country
    tonnes = data.tonnes_by_country
    dollars = data.dollars_by_country
    frames = [tonnes, dollars]
    result = pd.concat(frames, axis=1).reset_index()

    result.to_csv(f"{folder_to_save}/country.csv", index=False)

    # by transport
    tonnes = data.tonnes_by_transport
    dollars = data.dollars_by_transport
    frames = [tonnes, dollars]
    result = pd.concat(frames, axis=1).reset_index()

    result.to_csv(f"{folder_to_save}/transport_mean.csv", index=False)

    # by month
    tonnes = data.tonnes_by_month
    dollars = data.dollars_by_month
    frames = [tonnes, dollars]
    result = pd.concat(frames, axis=1).reset_index()

    result.to_csv(f"{folder_to_save}/month.csv", index=False)
