import customtkinter
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from diagrams import *


def main():
    # read data from file or from web
    data = read_data_from_url("effects-of-covid-19-on-trade-at-15-december-2021-provisional.csv")

    fig, ax = plt.subplots()
    fig.set_figwidth(9)
    fig.set_figheight(9)

    # creating the GUI
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("green")

    # main window's size is 1556x1000
    root = customtkinter.CTk()
    root.geometry(f"{60+60+250+60+60+250+60+60}x{20+(20+50+20)*5+20}")
    root.resizable(False, False)

    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill='both', expand=True)


    # left side of the GUI - CONTROLS

    dollars_months_button = customtkinter.CTkButton(master=frame, width=250, height=50,
                                                    text="Συνολική παρουσίαση του\nτζίρου ανά μήνα ($)",
                                                    command=lambda: dollars_diagram_by_months(data))
    tonnes_months_button = customtkinter.CTkButton(master=frame, width=250, height=50,
                                                   text="Συνολική παρουσίαση του τζίρου\nανά μήνα (Tonnes)",
                                                   command=lambda: tonnes_diagram_by_months(data))
    dollars_country_button = customtkinter.CTkButton(master=frame,width=250, height=50,
                                                     text="Συνολική παρουσίαση του τζίρου\nγια κάθε χώρα ($)",
                                                     command=lambda: dollars_bar_by_country(data))
    tonnes_country_button = customtkinter.CTkButton(master=frame,width=250, height=50,
                                                    text="Συνολική παρουσίαση του τζίρου\nγια κάθε χώρα (Tonnes)",
                                                    command=lambda: tonnes_bar_by_country(data))
    dollars_transport_button = customtkinter.CTkButton(master=frame,width=250, height=50,
                                                       text="Συνολική παρουσίαση του τζίρου για\n"
                                                            "κάθε μέσο μεταφοράς ($)",
                                                       command=lambda: dollars_bar_by_transport(data))
    tonnes_transport_button = customtkinter.CTkButton(master=frame,width=250, height=50,
                                                      text="Συνολική παρουσίαση του τζίρου για\n"
                                                           "κάθε μέσο μεταφοράς (Tonnes)",
                                                      command=lambda: tonnes_bar_by_transport(data))
    dollars_day_button = customtkinter.CTkButton(master=frame,width=250, height=50,
                                                 text="Συνολική παρουσίαση του τζίρου για\n"
                                                      "κάθε μέρα της εβδομάδας ($)",
                                                 command=lambda: dollars_bar_by_day(data))
    tonnes_day_button = customtkinter.CTkButton(master=frame,width=250, height=50,
                                                text="Συνολική παρουσίαση του τζίρου για\n"
                                                     "κάθε μέρα της εβδομάδας (Tonnes)",
                                                command=lambda: tonnes_bar_by_day(data))
    dollars_commodity_button = customtkinter.CTkButton(master=frame,width=250, height=50,
                                                       text="Συνολική παρουσίαση του τζίρου για\n"
                                                            "κάθε κατηγορία εμπορεύματος ($)",
                                                       command=lambda: dollars_bar_by_commodity(data))
    tonnes_commodity_button = customtkinter.CTkButton(master=frame,width=250, height=50,
                                                      text="Συνολική παρουσίαση του τζίρου για\n"
                                                           "κάθε κατηγορία εμπορεύματος (Tonnes)",
                                                      command=lambda: tonnes_bar_by_commodity(data))
    # max_dollars_month_button = customtkinter.CTkButton(master=root, width=468, height=50,
    #                                                    text="Παρουσίαση των 5 μηνών με το μεγαλύτερο τζίρο ($)",
    #                                                    command=lambda: max_dollars_by_month(data, ax, plt,
    #                                                                                         canvas))
    # max_tonnes_month_button = customtkinter.CTkButton(master=root, width=468, height=50,
    #                                                   text="Παρουσίαση των 5 μηνών με το μεγαλύτερο τζίρο (Tonnes)",
    #                                                   command=lambda: max_tonnes_by_month(data, ax, plt,
    #                                                                                       canvas))
    # max_dollars_commodity_button = customtkinter.CTkButton(master=root, width=468, height=50,
    #                                                        text="Παρουσίαση των 5 κατηγοριών εμπορευμάτων\n"
    #                                                             "με το μεγαλύτερο τζίρο, για κάθε χώρα",
    #                                                        command=lambda: max_dollars_by_commodity(data, ax, plt,
    #                                                                                                 canvas))
    # clc_button = customtkinter.CTkButton(master=root, width=468, height=50, text="Εκκαθάριση Οθόνης",
    #                                      command=lambda: clc(ax, canvas), fg_color="red", hover_color="#970202")

    dollars_months_button.grid(row=0, column=0, pady=20, padx=60)
    tonnes_months_button.grid(row=0, column=1, pady=20, padx=60)
    dollars_country_button.grid(row=1, column=0, pady=20, padx=60)
    tonnes_country_button.grid(row=1, column=1, pady=20, padx=60)
    dollars_transport_button.grid(row=2, column=0, pady=20, padx=60)
    tonnes_transport_button.grid(row=2, column=1, pady=20, padx=60)
    dollars_day_button.grid(row=3, column=0, pady=20, padx=60)
    tonnes_day_button.grid(row=3, column=1, pady=20, padx=60)
    dollars_commodity_button.grid(row=4, column=0, pady=20, padx=60)
    tonnes_commodity_button.grid(row=4, column=1, pady=20, padx=60)
    # max_dollars_month_button.pack(pady=5, padx=5)
    # max_tonnes_month_button.pack(pady=5, padx=5)
    # max_dollars_commodity_button.pack(pady=5, padx=5)
    # clc_button.pack(pady=5, padx=5, side=customtkinter.BOTTOM)
    #
    #
    # def click():
    #     print(f"{root.winfo_width()}x{root.winfo_height()}")
    #
    #

    root.mainloop()


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
