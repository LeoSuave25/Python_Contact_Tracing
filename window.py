import tkinter as tk
from tkinter import ttk
from data_manager import DataManager
from tkinter import messagebox
from datetime import datetime

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
question_label4 = ttk.Label(main_Frame, text="4. Have you had contact with somebody with body pains, headache, sore throat, "
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

# Respondent Details Label
details_label = ttk.Label(main_Frame, text="Respondent Details", font=("Arial", 12), background="#B4C5E4")
details_label.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

# Respondent Name Label
name_label = ttk.Label(main_Frame, text="6.a Name*", font=("Arial", 10), justify=tk.LEFT, background="#B4C5E4")
name_label.place(relx=0.03, rely=0.65, anchor=tk.W)

# Respondent Name Entry Field
respondent_name_entry = ttk.Entry(main_Frame, width=20)
respondent_name_entry.place(relx=0.13, rely=0.65, anchor=tk.W)

# Respondent Email Address Label
email_label = ttk.Label(main_Frame, text="6.b Email Address*", font=("Arial", 10), justify=tk.LEFT, background="#B4C5E4")
email_label.place(relx=0.30, rely=0.65, anchor=tk.W)

# Respondent Email Address Entry Field
email_entry = ttk.Entry(main_Frame, width=20)
email_entry.place(relx=0.46, rely=0.65, anchor=tk.W)

# Respondent Contact Number Label
contact_label = ttk.Label(main_Frame, text="6.c Contact Number*", font=("Arial", 10), justify=tk.LEFT,
                          background="#B4C5E4")
contact_label.place(relx=0.63, rely=0.65, anchor=tk.W)

# Respondent Contact Number Entry Field
contact_entry = ttk.Entry(main_Frame, width=20)
contact_entry.place(relx=0.8, rely=0.65, anchor=tk.W)

# Contact Person Details Label
details_label2 = ttk.Label(main_Frame, text="Contact Person Details", font=("Arial", 12), background="#B4C5E4")
details_label2.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

# Contact Person Name Label
name_label = ttk.Label(main_Frame, text="7.a Name*", font=("Arial", 10), justify=tk.LEFT, background="#B4C5E4")
name_label.place(relx=0.05, rely=0.75, anchor=tk.W)

# Contact Person Name Entry Field
name_entry = ttk.Entry(main_Frame, width=25)
name_entry.place(relx=0.25, rely=0.75, anchor=tk.W)

# Contact Person Contact Number Label
contact_label2 = ttk.Label(main_Frame, text="7.b Contact Number*", font=("Arial", 10), justify=tk.LEFT,
                          background="#B4C5E4")
contact_label2.place(relx=0.5, rely=0.75, anchor=tk.W)

# Contact Person Contact Number Entry Field
contact_entry2 = ttk.Entry(main_Frame, width=25)
contact_entry2.place(relx=0.7, rely=0.75, anchor=tk.W)

# Contact Person Email Address Label
email_label2 = ttk.Label(main_Frame, text="7.c Email Address*", font=("Arial", 10), justify=tk.LEFT,
                         background="#B4C5E4")
email_label2.place(relx=0.05, rely=0.8, anchor=tk.W)

# Contact Person Email Address Entry Field
email_entry2 = ttk.Entry(main_Frame, width=25)
email_entry2.place(relx=0.25, rely=0.8, anchor=tk.W)

# Contact Person Relationship Label
relationship_label = ttk.Label(main_Frame, text="7.d Relationship to the \ncontact person*", font=("Arial", 10),
                               justify=tk.LEFT, background="#B4C5E4")
relationship_label.place(relx=0.5, rely=0.8, anchor=tk.W)

# Contact Person Relationship Entry Field
relationship_entry = ttk.Entry(main_Frame, width=25)
relationship_entry.place(relx=0.7, rely=0.8, anchor=tk.W)

def submit():
    # Check if all fields are filled
    if (
        selected_option.get() and
        any(var.get() == 1 for var in selected_symptoms) and
        selected_option3.get() and
        selected_option4.get() and
        selected_option5.get() and
        respondent_name_entry.get() and
        email_entry.get() and
        contact_entry.get() and
        name_entry.get() and
        contact_entry2.get() and
        email_entry2.get() and
        relationship_entry.get()
    ):
        # Gather data from Tkinter widgets
        data = [
            selected_option.get(),  # First Question
            ', '.join([symptoms[i] for i, var in enumerate(selected_symptoms) if var.get() == 1]),  # Second Question
            selected_option3.get(),  # Third Question
            selected_option4.get(),  # Fourth Question
            selected_option5.get(),  # Fifth Question
            respondent_name_entry.get(),  # Respondent Name
            email_entry.get(),  # Respondent Email Address
            contact_entry.get(),  # Respondent Contact Number
            name_entry.get(),  # Contact Person Name
            contact_entry2.get(),  # Contact Person Contact Number
            email_entry2.get(),  # Contact Person Email Address
            relationship_entry.get()  # Contact Person Relationship
        ]
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data.append(current_time)

        questions = [
            "1. Have you been vaccinated for COVID-19?",
            "2. Are you experiencing any symptoms in the past 7 days such as:",
            "3. Have you had exposure to a probable or confirmed case in the last 14 days?",
            "4. Have you had contact with somebody with body pains, headache, sore throat, "
            "fever, diarrhea, cough, colds, shortness of breath, loss of taste, or loss of smell in the past 7 days?",
            "5. Have you been tested for Covid-19 in the last 14 days?",
            "6.a Respondent's Name*",
            "6.b Email Address*",
            "6.c Contact Number*",
            "7.a Name*",
            "7.b Contact Number*",
            "7.c Email Address*",
            "7.d Relationship to the contact person*",
            "Submit Time"
        ]

        # Save data to CSV file using DataManager
        DataManager.save_data('data.csv', questions, data)

        # Clear the entry fields and checkboxes
        respondent_name_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        contact_entry.delete(0, tk.END)
        name_entry.delete(0, tk.END)
        contact_entry2.delete(0, tk.END)
        email_entry2.delete(0, tk.END)
        relationship_entry.delete(0, tk.END)
        for var in selected_symptoms:
            var.set(0)
        # Show successful submission message box
        messagebox.showinfo("Success", "Submission successful!")
    else:
        # Show error message if any field is empty
        messagebox.showerror("Error", "Please fill in all fields.")


# Create a submit button
submit_button = ttk.Button(main_Frame, text="Submit", command=submit)
submit_button.place(relx=0.8, rely=0.9, anchor=tk.CENTER)


main_window.mainloop()
