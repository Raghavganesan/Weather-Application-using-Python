from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=62e24b617ed051706797ad2ac717132b").json()
    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"]-273.15)) + "°C")
    p_label1.config(text=str(data["main"]["pressure"]) + " hPa")

# Create main window
win = Tk()
win.title("Weather Application")
win.config(bg="#283747")
win.geometry("500x600")

# Header label
name_label = Label(win, text="Weather Application", font=("Helvetica", 24, "bold"), bg="#283747", fg="white")
name_label.pack(pady=20)

# Combobox for city selection
city_name = StringVar()
com = ttk.Combobox(win, textvariable=city_name, values=[
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana",
    "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh",
    "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan",
    "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal",
    "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli", "Daman and Diu", "Lakshadweep",
    "National Capital Territory of Delhi", "Puducherry"
], font=("Helvetica", 14), state="readonly")
com.pack(pady=10)
com.set("Select a City")

# Function to configure label styles
def create_label(parent, text, font_size=14, fg="white"):
    return Label(parent, text=text, font=("Helvetica", font_size), bg="#283747", fg=fg)

# Weather info labels
info_frame = Frame(win, bg="#283747")
info_frame.pack(pady=20)

w_label = create_label(info_frame, "Weather Climate", 16)
w_label.grid(row=0, column=0, padx=20, pady=10, sticky=W)
w_label1 = create_label(info_frame, "", 16, "#AED6F1")
w_label1.grid(row=0, column=1, padx=20, pady=10, sticky=E)

wb_label = create_label(info_frame, "Weather Description", 14)
wb_label.grid(row=1, column=0, padx=20, pady=10, sticky=W)
wb_label1 = create_label(info_frame, "", 14, "#AED6F1")
wb_label1.grid(row=1, column=1, padx=20, pady=10, sticky=E)

temp_label = create_label(info_frame, "Temperature", 16)
temp_label.grid(row=2, column=0, padx=20, pady=10, sticky=W)
temp_label1 = create_label(info_frame, "", 16, "#AED6F1")
temp_label1.grid(row=2, column=1, padx=20, pady=10, sticky=E)

p_label = create_label(info_frame, "Pressure", 16)
p_label.grid(row=3, column=0, padx=20, pady=10, sticky=W)
p_label1 = create_label(info_frame, "", 16, "#AED6F1")
p_label1.grid(row=3, column=1, padx=20, pady=10, sticky=E)

# Button to trigger the API call
done_button = Button(win, text="Get Weather", font=("Helvetica", 14, "bold"), command=data_get, bg="#5DADE2", fg="white")
done_button.pack(pady=20)

win.mainloop()
