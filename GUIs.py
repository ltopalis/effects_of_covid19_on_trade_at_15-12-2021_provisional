import customtkinter
from save_to_csv import save_to_csv
from diagrams import *
from Connect_DB import insert_to_database


def second_window(root, data_extractor):
    root.withdraw()
    main_frame = customtkinter.CTkToplevel(root)
    main_frame.geometry("500x350")

    def connect(data):
        insert_to_database(data, root, main_frame, host_entry.get(), username_entry.get(), password_entry.get())

    inside_frame = customtkinter.CTkFrame(master=main_frame)
    inside_frame.pack(pady=20, padx=60, fill="both", expand=True)

    label = customtkinter.CTkLabel(master=inside_frame, text="Σύνδεση με την Βάση Δεδομένων")
    label.pack(pady=12, padx=10)

    host_entry = customtkinter.CTkEntry(master=inside_frame, placeholder_text="Host")
    host_entry.pack(pady=12, padx=10)

    username_entry = customtkinter.CTkEntry(master=inside_frame, placeholder_text="Username")
    username_entry.pack(pady=12, padx=10)

    password_entry = customtkinter.CTkEntry(master=inside_frame, placeholder_text="Password", show="*")
    password_entry.pack(pady=12, padx=10)

    button = customtkinter.CTkButton(master=inside_frame, text="Σύνδεση",
                                     command=lambda: connect(data_extractor))
    button.pack(pady=12, padx=10)


def main_gui(de):
    # creating the GUI
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("green")

    # main window
    root = customtkinter.CTk()
    root.geometry(f"{60 + 60 + 250 + 60 + 60 + 250 + 60 + 60}x{20 + (20 + 50 + 20) * 7 + 20}")
    root.resizable(False, False)

    frame = customtkinter.CTkFrame(master=root)
    print("HERE")
    frame.pack(pady=20, padx=60, fill='both', expand=True)

    # left side of the GUI - CONTROLS

    dollars_months_button = customtkinter.CTkButton(master=frame, width=250, height=50,
                                                    text="Συνολική παρουσίαση του\nτζίρου ανά μήνα ($)",
                                                    command=lambda: dollars_diagram_by_months(de.dollars_by_month))
    tonnes_months_button = customtkinter.CTkButton(master=frame, width=250, height=50,
                                                   text="Συνολική παρουσίαση του τζίρου\nανά μήνα (Tonnes)",
                                                   command=lambda: tonnes_diagram_by_months(de.tonnes_by_month))
    dollars_country_button = customtkinter.CTkButton(master=frame, width=250, height=50,
                                                     text="Συνολική παρουσίαση του τζίρου\nγια κάθε χώρα ($)",
                                                     command=lambda: dollars_bar_by_country(de.dollars_by_country))
    tonnes_country_button = customtkinter.CTkButton(master=frame, width=250, height=50,
                                                    text="Συνολική παρουσίαση του τζίρου\nγια κάθε χώρα (Tonnes)",
                                                    command=lambda: tonnes_bar_by_country(de.tonnes_by_country))
    dollars_transport_button = customtkinter.CTkButton(master=frame, width=250, height=50,
                                                       text="Συνολική παρουσίαση του τζίρου για\n"
                                                            "κάθε μέσο μεταφοράς ($)",
                                                       command=lambda: dollars_bar_by_transport(
                                                           de.dollars_by_transport))
    tonnes_transport_button = customtkinter.CTkButton(master=frame, width=250, height=50,
                                                      text="Συνολική παρουσίαση του τζίρου για\n"
                                                           "κάθε μέσο μεταφοράς (Tonnes)",
                                                      command=lambda: tonnes_bar_by_transport(de.tonnes_by_transport))
    dollars_day_button = customtkinter.CTkButton(master=frame, width=250, height=50,
                                                 text="Συνολική παρουσίαση του τζίρου για\n"
                                                      "κάθε μέρα της εβδομάδας ($)",
                                                 command=lambda: dollars_bar_by_day(de.dollars_by_day))
    tonnes_day_button = customtkinter.CTkButton(master=frame, width=250, height=50,
                                                text="Συνολική παρουσίαση του τζίρου για\n"
                                                     "κάθε μέρα της εβδομάδας (Tonnes)",
                                                command=lambda: tonnes_bar_by_day(de.tonnes_by_day))
    dollars_commodity_button = customtkinter.CTkButton(master=frame, width=250, height=50,
                                                       text="Συνολική παρουσίαση του τζίρου για\n"
                                                            "κάθε κατηγορία εμπορεύματος ($)",
                                                       command=lambda: dollars_bar_by_commodity(
                                                           de.dollars_by_commodity))
    tonnes_commodity_button = customtkinter.CTkButton(master=frame, width=250, height=50,
                                                      text="Συνολική παρουσίαση του τζίρου για\n"
                                                           "κάθε κατηγορία εμπορεύματος (Tonnes)",
                                                      command=lambda: tonnes_bar_by_commodity(de.tonnes_by_commodity))
    max_dollars_month_button = customtkinter.CTkButton(master=frame, width=250, height=50,
                                                       text="Παρουσίαση των 5 μηνών με\nτο μεγαλύτερο τζίρο ($)",
                                                       command=lambda: max_dollars_by_month(de.max_dollars_by_month))
    max_tonnes_month_button = customtkinter.CTkButton(master=frame, width=250, height=50,
                                                      text="Παρουσίαση των 5 μηνών με\nτο μεγαλύτερο τζίρο (Tonnes)",
                                                      command=lambda: max_tonnes_by_month(de.max_tonnes_by_month))
    # max_dollars_commodity_button = customtkinter.CTkButton(master=frame, width=250, height=50,
    #                                                        text="Παρουσίαση των 5 κατηγοριών εμπορευμάτων\n"
    #                                                             "με το μεγαλύτερο τζίρο, για κάθε χώρα",
    #                                                        command=lambda: max_dollars_by_commodity(data, ax, plt,
    #                                                                                                 canvas))
    # clc_button = customtkinter.CTkButton(master=frame, width=250, height=50, text="Εκκαθάριση Οθόνης",
    #                                      command=lambda: clc(ax, canvas), fg_color="red", hover_color="#970202")
    save_to_database_button = customtkinter.CTkButton(master=frame, width=250, height=50,
                                                      text="Aποθήκευση στην Βάση Δεδομένων",
                                                      command=lambda: second_window(root, de))
    save_to_csv_button = customtkinter.CTkButton(master=frame, width=250, height=50,
                                                 text="Aποθήκευση σε αρχεία .csv",
                                                 command=lambda: save_to_csv(de))

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
    max_dollars_month_button.grid(row=5, column=0, pady=20, padx=60)
    max_tonnes_month_button.grid(row=5, column=1, pady=20, padx=60)

    save_to_database_button.grid(row=7, column=0, pady=20, padx=60)
    save_to_csv_button.grid(row=7, column=1, pady=20, padx=60)
    # max_dollars_commodity_button.pack(pady=5, padx=5)
    # clc_button.pack(pady=5, padx=5, side=customtkinter.BOTTOM)
    #
    #
    # def click():
    #     print(f"{root.winfo_width()}x{root.winfo_height()}")
    #
    #

    root.mainloop()
