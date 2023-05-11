from tkinter import messagebox

import customtkinter
import mysql.connector
import pandas as pd
from sqlalchemy import create_engine
import pymysql

from dataExtractor import DataExtractor


class ConnectDatabase:
    def __init__(self, frame=None, host=None, user=None, password=None, database=None):
        if frame is None:
            return
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.MYSQL = mysql.connector

        # Creating Database and Tables
        try:
            with self.MYSQL.connect(host=self.host,
                                    user=self.user,
                                    password=self.password,
                                    database=self.database
                                    ) as connection:
                cursor = connection.cursor(dictionary=True)

                # Creating Database and Tables
                with open("queries.sql", "r") as f:
                    query = f.read()
                    cursor.execute(query)

                frame.destroy()

        except self.MYSQL.Error as e:
            print(e)

    def __str__(self):
        pas = ""
        db = ""
        if self.password is not None:
            pas = f":{self.password}"
        if self.database is not None:
            db = f":{self.database}"
        return f"{self.user}{pas}@{self.host}{db}"


def insert_to_database(values, frame=None, host=None, user=None, password=None, database=None):
    server = ConnectDatabase(frame, host, user, password, database)

    engine = create_engine(f"mysql+pymysql://{server.user}:{server.password}@{server.host}/"
                           f"effects_of_covid_19_on_trade_at_15_december_2021_provisional")

    # by day
    tonnes = values.tonnes_by_day
    dollars = values.dollars_by_day
    frames = [tonnes, dollars]
    result = pd.concat(frames, axis=1).reset_index()

    result.to_sql("weekday", con=engine, if_exists='replace', index=False)

    # by commodity
    tonnes = values.tonnes_by_commodity
    dollars = values.dollars_by_commodity
    frames = [tonnes, dollars]
    result = pd.concat(frames, axis=1).reset_index()

    result.to_sql("commodity", con=engine, if_exists='replace', index=False)

    # by country
    tonnes = values.tonnes_by_country
    dollars = values.dollars_by_country
    frames = [tonnes, dollars]
    result = pd.concat(frames, axis=1).reset_index()

    result.to_sql("country", con=engine, if_exists='replace', index=False)

    # by transport
    tonnes = values.tonnes_by_transport
    dollars = values.dollars_by_transport
    frames = [tonnes, dollars]
    result = pd.concat(frames, axis=1).reset_index()

    result.to_sql("transport_mean", con=engine, if_exists='replace', index=False)

    # by month
    tonnes = values.tonnes_by_month
    dollars = values.dollars_by_month
    frames = [tonnes, dollars]
    result = pd.concat(frames, axis=1).reset_index()

    result.to_sql("month", con=engine, if_exists='replace', index=False)

    # Παρουσίαση των 5 μηνών με το μεγαλύτερο τζίρο, ανεξαρτήτως μέσου μεταφοράς και είδους ανακυκλώσιμων ειδών
    tonnes = values.max_tonnes_by_month
    dollars = values.max_dollars_by_month
    frames = [tonnes, dollars]
    result = pd.concat(frames, axis=1).reset_index()

    result.to_sql("5_max_turnout_by_month", con=engine, if_exists='replace', index=False)

    # Παρουσίαση των 5 κατηγοριών εμπορευμάτων με το μεγαλύτερο τζίρο, για κάθε χώρα
    tonnes = values.day_max_tonnes_by_commodity
    tonnes['Measure'] = 'Tonnes'

    dollars = values.day_max_dollars_by_commodity
    dollars['Measure'] = '$'

    frames = [tonnes, dollars]
    result = pd.concat(frames, axis=0).reset_index()

    result = result.drop('index', axis=1)

    result.to_sql("5_max_turnout_by_commodity_for_each_country", con=engine, if_exists='replace', index=False)

    messagebox.showinfo("Επιτυχία", "Τα δεδομένα αποθηκεύτηκαν επιτυχώς!")
