import tkinter as tk
from tkinter import ttk

main_window = tk.Tk()

# ============================ STYLING

window_color = ttk.Style()
window_color.configure('main_Frame.TFrame', background='#3C3744')

main_Frame = ttk.Frame(main_window, width=800, height=600, style='main_Frame.TFrame')
main_window.title("COVID-19 CONTACT TRACING APP")

main_Frame.pack()

main_window.resizable(width=False, height=False)
# ============================== WIDGETS

top_frame = ttk.Label(main_Frame, text="Contact Tracing App", font=("Arial", 24), background="#B4C5E4")
top_frame.place(relx=0.5, rely=0.05, anchor=tk.CENTER)

# First Question Label
question_label = ttk.Label(main_Frame, text="Have you been vaccinated for COVID-19?", font=("Arial", 10),justify=tk.LEFT, wraplength=400, background="#B4C5E4")
question_label.place(relx=0.05, rely=0.2, anchor=tk.W)

# Options
first_options = [
    "Not Yet",
    "1st Dose",
    "2nd Dose (Fully Vaccinated)",
    "1st Booster Shot",
    "2nd Booster Shot"
]

# Dropdown Menu
selected_option = tk.StringVar()
dropdown_menu = ttk.OptionMenu(main_Frame, selected_option, first_options[0], *first_options)
dropdown_menu.place(relx=0.4, rely=0.2, anchor=tk.W)

# Second Question Label
question_label2 = ttk.Label(main_Frame, text="Are you experiencing any symptoms in the past 7 days such as:",font=("Arial", 10), justify=tk.LEFT, wraplength=400, background="#B4C5E4")
question_label2.place(relx=0.05, rely=0.3, anchor=tk.W)

# Second Question Checkboxes
symptoms = [
    "Fever",
    "Cough",
    "Colds",
    "Muscle/body pains",
    "Sore throat",
    "Diarrhea",
    "Headache",
    "Shortness of breath",
    "Difficulty of breathing",
    "Loss of taste",
    "Loss of smell",
    "None of the above"
]

selected_symptoms = []
checkboxes = []

rows = 4  # Number of lines for the checkboxes
cols = len(symptoms) // rows  # Number of checkboxes in each line

for i, symptom in enumerate(symptoms):
    var = tk.IntVar()
    checkbox = ttk.Checkbutton(main_Frame, text=symptom, variable=var)
    checkbox.place(relx=0.05 + (i % cols) * 0.3, rely=0.35 + (i // cols) * 0.05, anchor=tk.W)
    checkboxes.append(checkbox)
    selected_symptoms.append(var)

main_window.mainloop()
