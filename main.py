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
    customtkinter.set_appearance_mode("system")
    customtkinter.set_default_color_theme("dark-blue")

    # main window's size is 1556x1000
    root = customtkinter.CTk()
    root.geometry("1556x940")
    root.resizable(False, False)

    # right side of the GUI - GRAPHICS
    right = customtkinter.CTkFrame(root, 1078, 940)
    right.pack(side=customtkinter.RIGHT, fill=customtkinter.X, expand=customtkinter.YES)

    canvas = FigureCanvasTkAgg(fig, master=right)
    canvas.get_tk_widget().pack(fill=customtkinter.X, expand=customtkinter.YES)
    toolbar = NavigationToolbar2Tk(canvas, right, pack_toolbar=False)
    toolbar.update()
    toolbar.pack(anchor="w", fill=customtkinter.BOTH, expand=True)

    # left side of the GUI - CONTROLS
    left = customtkinter.CTkFrame(root, 478, 940)

    dollars_months_button = customtkinter.CTkButton(master=left, width=468, height=50,
                                                    text="Συνολική παρουσίαση του τζίρου ανά μήνα ($)",
                                                    command=lambda: dollars_diagram_by_months(data, ax, plt, canvas))
    tonnes_months_button = customtkinter.CTkButton(master=left, width=468, height=50,
                                                   text="Συνολική παρουσίαση του τζίρου\nανά μήνα (Tonnes)",
                                                   command=lambda: tonnes_diagram_by_months(data, ax, plt, canvas))
    dollars_country_button = customtkinter.CTkButton(master=left, width=468, height=50,
                                                     text="Συνολική παρουσίαση του τζίρου\nγια κάθε χώρα ($)",
                                                     command=lambda: dollars_bar_by_country(data, ax, plt, canvas))
    tonnes_country_button = customtkinter.CTkButton(master=left, width=468, height=50,
                                                    text="Συνολική παρουσίαση του τζίρου\nγια κάθε χώρα (Tonnes)",
                                                    command=lambda: tonnes_bar_by_country(data, ax, plt, canvas))
    dollars_transport_button = customtkinter.CTkButton(master=left, width=468, height=50,
                                                       text="Συνολική παρουσίαση του τζίρου για\n"
                                                            "κάθε μέσο μεταφοράς ($)",
                                                       command=lambda: dollars_bar_by_transport(data, ax, plt, canvas))
    tonnes_transport_button = customtkinter.CTkButton(master=left, width=468, height=50,
                                                      text="Συνολική παρουσίαση του τζίρου για\n"
                                                           "κάθε μέσο μεταφοράς (Tonnes)",
                                                      command=lambda: tonnes_bar_by_transport(data, ax, plt, canvas))
    dollars_day_button = customtkinter.CTkButton(master=left, width=468, height=50,
                                                 text="Συνολική παρουσίαση του τζίρου για\n"
                                                      "κάθε μέρα της εβδομάδας ($)",
                                                 command=lambda: dollars_bar_by_day(data, ax, plt, canvas))
    tonnes_day_button = customtkinter.CTkButton(master=left, width=468, height=50,
                                                text="Συνολική παρουσίαση του τζίρου για\n"
                                                     "κάθε μέρα της εβδομάδας (Tonnes)",
                                                command=lambda: tonnes_bar_by_day(data, ax, plt, canvas))
    dollars_commodity_button = customtkinter.CTkButton(master=left, width=468, height=50,
                                                       text="Συνολική παρουσίαση του τζίρου για\n"
                                                            "κάθε κατηγορία εμπορεύματος ($)",
                                                       command=lambda: dollars_bar_by_commodity(data, ax, plt, canvas))
    tonnes_commodity_button = customtkinter.CTkButton(master=left, width=468, height=50,
                                                      text="Συνολική παρουσίαση του τζίρου για\n"
                                                           "κάθε κατηγορία εμπορεύματος (Tonnes)",
                                                      command=lambda: tonnes_bar_by_commodity(data, ax, plt, canvas))
    max_dollars_month_button = customtkinter.CTkButton(master=left, width=468, height=50,
                                                       text="Παρουσίαση των 5 μηνών με το μεγαλύτερο τζίρο ($)",
                                                       command=lambda: max_dollars_by_month(data, ax, plt,
                                                                                                        canvas))
    max_tonnes_month_button = customtkinter.CTkButton(master=left, width=468, height=50,
                                                       text="Παρουσίαση των 5 μηνών με το μεγαλύτερο τζίρο (Tonnes)",
                                                       command=lambda: max_tonnes_by_month(data, ax, plt,
                                                                                                       canvas))
    clc_button = customtkinter.CTkButton(master=left, width=468, height=50, text="Εκκαθάριση Οθόνης",
                                         command=lambda: clc(ax, canvas), fg_color="red", hover_color="#970202")

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
    max_dollars_month_button.pack(pady=5, padx=5)
    max_tonnes_month_button.pack(pady=5, padx=5)
    clc_button.pack(pady=5, padx=5, side=customtkinter.BOTTOM)
    #
    #
    # def click():
    #     print(f"{root.winfo_width()}x{root.winfo_height()}")
    #
    #

    left.pack(side=customtkinter.LEFT)

    root.mainloop()


if __name__ == '__main__':
    main()
