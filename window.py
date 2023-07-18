import tkinter as tk
from tkinter import ttk

main_window = tk.Tk()

# ============================ STYLING

window_color = ttk.Style()
window_color.configure('main_Frame.TFrame', background='#3C3744')

main_Frame = ttk.Frame(main_window, width=800, height=600, style='main_Frame.TFrame')
main_window.title("COVID-19 CONTACT TRACING APP")

main_Frame.pack()

main_window.resizable(width= False, height=False)
#============================== WIDGETS

top_frame = ttk.Label(main_Frame, text="Contact Tracing App", font=("Arial",24), background= "#B4C5E4")
top_frame.place(relx=0.5, rely=0.05, anchor=tk.CENTER)

main_window.mainloop()
