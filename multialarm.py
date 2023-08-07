# Importing the libraries
from tkinter import *
import datetime
from PIL import ImageTk, Image
from time import strftime
from datetime import datetime
from time import gmtime, strftime
from  tkinter import ttk
from playsound import playsound
import threading

# necessary details

root = Tk()
root.title("MultiAlarm")


# alarm variable

alarm_time = []  
set_alarm_time = [{"time":"Time", "date":"Weekday"}]
snooze_val = 90

# Background setting

image = Image.open('background.png')
photo = ImageTk.PhotoImage(image)
label = Label(root, image=photo, bg="#4a536b")
label.grid(row=1)

# Sound play
def sound_play():
    playsound("./alarm.mp3")
    time.sleep(snooze_val)    

# time compare for alarm  

def com_time():
    threading.Timer(60.0, com_time).start()

# compare with zmanim times
    compare_time = strftime('%I:%M %p')
    if compare_time in alarm_time:
        sound_play()

# compare with setting alarm
    dt = datetime.now()
    weekday=dt.strftime('%A')
    compare_data1={"time":compare_time, "date":weekday}
    compare_data2={"time":compare_time, "date":"Everyday"}
    if compare_data1 in set_alarm_time:
        sound_play()
    if compare_data2 in set_alarm_time:
        sound_play()
        
# String to datetime and get time

def convert_time(data):
    res = datetime.strptime(data, '%Y-%m-%dT%H:%M:%f%z').strftime('%I:%M %p')
    if (datetime.strptime(data, '%Y-%m-%dT%H:%M:%f%z').strftime('%Y-%m-%d') == '0001-01-01'):
        return ''
    return res

# Dates

def time():
    string = strftime('%I:%M:%S %p')
    hour.config(text=string)
    hour.after(1000, time)
  
# Setting alarm time add

def add_alarm():
    h = hour_var.get()
    m = min_var.get()
    p_m = p_m_var.get()
    w = day_var.get()
    get_time = h + ":" + m + " " + p_m
    savedata={"time":get_time, "date":w}
    if (savedata in set_alarm_time):
        return
    set_alarm_time.append(savedata)
    view_alarm_time()
    
# Setting alarm time delete

def del_alarm():
    h = hour_var.get()
    m = min_var.get()
    p_m = p_m_var.get()
    w = day_var.get()
    get_time = h + ":" + m + " " + p_m
    set_alarm_time.remove({"time":get_time, "date":w})
    view_alarm_time()


def view_alarm_time():
    view_data=[]
    for i in set_alarm_time:
        view_data.append("     " + str(i["time"]) + "       " + str(i["date"]))
    alarm_var = Variable(value=view_data)
    alarm_listbox = Listbox(listvariable=alarm_var, font=("Arial", 13, "bold"))
    alarm_listbox.place(x=115, y=450, height=400, width=235)
# -------------------------------------------------------------------------------------------
    
# -------------------------------------------------------------------------------------------


# Latitude and Longtitude
lable_pos_lat = Label(root, text="", width=0, bg='#d7c99c', fg="white", font="Montserrat 30 bold")
lable_pos_lat.place(x=650, y=170)

lable_pos_long = Label(root, text="", width=0, bg='#d7c99c', fg="white", font="Montserrat 30 bold")
lable_pos_long.place(x=650, y=220)

lable_current_weather = Label(root, text="", width=0, bg="#c5ad81", fg="white", font="Montserrat 30 bold")
lable_current_weather.place(x=1200, y=70)

# lable_status = Label(root, text="", width=0, bg='#ebc92a', font="Montserrat 10")
# lable_status.place(x=20, y=130)



# Setting hour min p_a and weekday for alarm
hour_set = ["01" ,"02","03" ,"04","05" ,"06","07" ,"08","09" ,"10","11" ,"12"]
hour_var = StringVar(value=hour_set[0])
hour_dropdown = OptionMenu(root, hour_var, *hour_set)
hour_dropdown.config(font=("Arial", 11, "bold"), width=4, bg="#dbdee5")
hour_dropdown.place(x=25, y=10)

min_set = ["00" ,"05" ,"10","15" ,"20","25" ,"30","35" ,"40","45" ,"50","55"]
min_var = StringVar(value=min_set[0])
min_dropdown = OptionMenu(root, min_var, *min_set)
min_dropdown.config(font=("Arial", 11, "bold"), width=4, bg="#dbdee5")
min_dropdown.place(x=100, y=10)

p_m_set = ["AM" ,"PM"]
p_m_var = StringVar(value=p_m_set[0])
p_m_dropdown = OptionMenu(root, p_m_var, *p_m_set)
p_m_dropdown.config(font=("Arial", 11, "bold"), width=4, bg="#dbdee5")
p_m_dropdown.place(x=175, y=10)

day_set = ["EveryDay" ,"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day_var = StringVar(value=day_set[0])
day_dropdown = OptionMenu(root, day_var, *day_set)
day_dropdown.config(font=("Arial", 11, "bold"), width=7, bg="#dbdee5")
day_dropdown.place(x=250, y=10)

# Alarm List Header

alarm_var = Variable(value=["      Time        Weekday"])

alarm_listbox = Listbox(listvariable=alarm_var, font=("Arial", 13, "bold"))
alarm_listbox.place(x=115, y=100, height=300, width=235)

Button(root, text="Add", command=add_alarm, width=7, fg="red" , bg="#ced2dd" ,cursor="arrow", font="Poppins 12 bold").place(x=10, y=100)
Button(root, text="Delete", command=del_alarm, width=7, fg="red" , bg="#ced2dd" ,cursor="arrow", font="Poppins 12 bold").place(x=135, y=100)

#Snooze part

def get_snooze_val(val):
    global snooze_val
    snooze_val = val

class Snooze:
    def __init__(self, name, val):
        Radiobutton(
            text=name,
            command=lambda i=val: get_snooze_val(i),
            variable=var, value=val).place(x=160, y= int(val / 90) * 30 + 420)

var = IntVar()
var.set(90)

Snooze("90 Seconds", 90)
Snooze(" 3 minutes", 180)
Snooze(" 5 minutes", 300)

# Placing clock and date

dt = datetime.now()
date = Label(root, text=dt.strftime('%A'), bg="#cac198", font="poppins 60 bold", fg="white")
date.place(x=250, y=930, height=150)

month = Label(root, text=dt.strftime('%d %B %Y'), bg="#e4d2a4", fg="White", font="Poppins 60 bold")
month.place(x=650, y=930, height= 150)

#Label(root, text="Current time: ", bg="#edc520", font="Poppins 10").place(x=330, y=460)
# Time
hour = Label(root, 
            font=('calibri', 80, 'bold'),
            background='purple',
            foreground='white')
hour.place(x=1250, y=930, width=700, height=150)

com_time()
time()

root.mainloop()
