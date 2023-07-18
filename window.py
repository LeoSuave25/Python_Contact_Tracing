import tkinter as tk
from tkinter import ttk
    
    
main_window = tk.Tk()

# ============================ STYLING

window_color = ttk.Style()
window_color.configure('main_Frame.TFrame', background='#3C3744')

main_Frame = ttk.Frame(main_window, width=800, height=700, style='main_Frame.TFrame')
main_window.title("COVID-19 CONTACT TRACING APP")

main_Frame.pack()

main_window.resizable(width=False, height=False)
# ============================== WIDGETS

top_frame = ttk.Label(main_Frame, text="Contact Tracing App", font=("Arial", 24), background="#B4C5E4")
top_frame.place(relx=0.5, rely=0.05, anchor=tk.CENTER)

# First Question Label
question_label = ttk.Label(main_Frame, text="1. Have you been vaccinated for COVID-19?", font=("Arial", 10),
                            justify=tk.LEFT, wraplength=400, background="#B4C5E4")
question_label.place(relx=0.05, rely=0.11, anchor=tk.W)

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
dropdown_menu.place(relx=0.4, rely=0.11, anchor=tk.W)

# Second Question Label
question_label2 = ttk.Label(main_Frame, text="2. Are you experiencing any symptoms in the past 7 days such as:",
                            font=("Arial", 10), justify=tk.LEFT, wraplength=400, background="#B4C5E4")
question_label2.place(relx=0.05, rely=0.15, anchor=tk.W)

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
    checkbox.place(relx=0.05 + (i % cols) * 0.3, rely=0.2 + (i // cols) * 0.05, anchor=tk.W)
    checkboxes.append(checkbox)
    selected_symptoms.append(var)

# Third Question Label
question_label3 = ttk.Label(main_Frame, text="3. Have you had exposure to a probable or confirmed case in the last 14 days?",
                            font=("Arial", 10), justify=tk.LEFT, wraplength=400, background="#B4C5E4")
question_label3.place(relx=0.05, rely=0.4, anchor=tk.W)

# Third Question Dropdown
third_options = [
    "Yes",
    "No",
    "Uncertain"
]

selected_option3 = tk.StringVar()
dropdown_menu3 = ttk.OptionMenu(main_Frame, selected_option3, third_options[0], *third_options)
dropdown_menu3.place(relx=0.6, rely=0.4, anchor=tk.W)

# Fourth Question Label
question_label4 = ttk.Label(main_Frame, text="4. Have you had in contact with somebody with body pains, headache, sore throat, "
                                              "fever, diarrhea, cough, colds, shortness of breath, loss of taste, "
                                              "or loss of smell in the past 7 days?",
                            font=("Arial", 10), justify=tk.LEFT, wraplength=400, background="#B4C5E4")
question_label4.place(relx=0.05, rely=0.48, anchor=tk.W)

# Fourth Question Dropdown
fourth_options = [
    "Yes",
    "No"
]

selected_option4 = tk.StringVar()
dropdown_menu4 = ttk.OptionMenu(main_Frame, selected_option4, fourth_options[0], *fourth_options)
dropdown_menu4.place(relx=0.6, rely=0.48, anchor=tk.W)

# Fifth Question Label
question_label5 = ttk.Label(main_Frame, text="5. Have you been tested for Covid-19 in the last 14 days?",
                            font=("Arial", 10), justify=tk.LEFT, wraplength=400, background="#B4C5E4")
question_label5.place(relx=0.05, rely=0.55, anchor=tk.W)

# Fifth Question Dropdown
fifth_options = [
    "No",
    "Yes-Positive",
    "Yes-Negative",
    "Yes-Pending"
]

selected_option5 = tk.StringVar()
dropdown_menu5 = ttk.OptionMenu(main_Frame, selected_option5, fifth_options[0], *fifth_options)
dropdown_menu5.place(relx=0.6, rely=0.55, anchor=tk.W)


main_window.mainloop()
