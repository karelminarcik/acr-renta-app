import tkinter
import pandas as pd
import customtkinter

customtkinter.set_appearance_mode("Dark")

window = customtkinter.CTk()
window.title("Renta AČR")
window.geometry("230x250")
window.resizable(False, False)
window.iconbitmap("soldier_icon.ico")



df = pd.read_excel("salary.xlsx")
df_2 = pd.read_excel("Rokyvsprocenta.xlsx")

# Gain salary amount
def get_month_salary():
    rank = df["Hodnost"].values.tolist()
    rank = [el.replace('\xa0', '') for el in rank]
    for one_rank in rank:
        if one_rank == drop_down_rank.get():
            return df.iloc[(rank.index(one_rank)), 1]

# Gain percentage
def get_percentages():
    age = df_2["Roky"].values.tolist()
    for one_age in age:
        if one_age == int(drop_down_age.get()):
            return df_2.iloc[(age.index(one_age)),1]

def bonus_amount():
    bonus = bonus_entry.get()
    try:
        bonus = float(bonus.replace(",", ".")) * 0.01
        return bonus
    except ValueError:
        info_label.configure(text="Zadejte prosím číslo. Desetinné místo oddělte tečkou.",wraplength=200)
        return 0

def renta_count():
    info_label.configure(text="")
    bonus = bonus_amount()
    print(bonus)
    salary = float((get_month_salary()))
    percentages = get_percentages()
    result_label.configure(text=f"{(round((salary + (salary * bonus)) * percentages))} Kč")


# frames
label_frame = customtkinter.CTkFrame(master=window)
label_frame.configure(width=300)
button_frame = customtkinter.CTkFrame(window)
result_frame = customtkinter.CTkFrame(window)
info_frame = customtkinter.CTkFrame(window)
label_frame.grid(row=0, column=0, padx=20, pady=10)
button_frame.grid(row=1, column=0, padx=20, pady=5)
result_frame.grid(row=2, column=0, padx=20, pady=5)
info_frame.grid(row=3, column=0, padx=20, pady=5)

# label_frame
def optionmenu_callback(selection):
    if selection != "Vyberte":
        print(selection, type(selection))

rank_label = customtkinter.CTkLabel(label_frame, text="Hodnost", font=("Arial", 12))
rank_label.grid(row=0, column=0)

drop_down_rank = customtkinter.CTkOptionMenu(master=label_frame,
                                       values=["Vojín", "Svobodník", "Destátník", "Četař", "Rotný", "Rotmistr", "Nadrotmistr", "Praporčík", "Nadpraporčík", "Štábní praporčík", "Poručík", "Nadporučík", "Kapitán", "Major", "Podplukovník", "Plukovník", "Brigádní generál", "Generálmajor", "Generálporučík", "Armádní generál"],
                                        width=30,
                                       command=optionmenu_callback)
drop_down_rank.place(rely=0.15, relheight=0.35, x=100, anchor=tkinter.W)
drop_down_rank.set("Vyberte")  # set initial value

age_label = customtkinter.CTkLabel(label_frame, text="Délka služby", font=("Arial", 12))
age_label.grid(row=1, column=0)

drop_down_age = customtkinter.CTkOptionMenu(master=label_frame,
                                       values=["15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30"],
                                        width=30,
                                       command=optionmenu_callback)
drop_down_age.place(rely=0.5, relheight=0.35, x=100, anchor=tkinter.W)
drop_down_age.set("Vyberte")  # set initial value

bonus_label = customtkinter.CTkLabel(label_frame, text="Výkonnostní příplatek", font=("Arial", 12))
bonus_label.grid(row=2, column=0)

bonus_entry = customtkinter.CTkEntry(label_frame, width=40)
bonus_entry.grid(row=2,column=1, padx=20)

# button label
count_button = customtkinter.CTkButton(button_frame, text="Spočítat", font=("Arial", 12), command=renta_count)
count_button.pack(pady=10)

# result_frame

describe_label = customtkinter.CTkLabel(result_frame, text="Vaše měsíční renta je", font=("Arial", 12))
describe_label.grid(row=0, column=0)

result_label = customtkinter.CTkLabel(result_frame, text="0", font=("Arial", 12))
result_label.grid(row=0, column=1, padx=10)

# info frame

info_label = customtkinter.CTkLabel(info_frame, wraplength=300, text="", font=("Arial", 12))
info_label.grid(row=0, column=0)

# main cycle
window.mainloop()