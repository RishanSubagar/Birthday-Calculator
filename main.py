from tkinter import *
import datetime 
from datetime import date
from PIL import ImageTk,Image

#Window Setup
root=Tk()
root.geometry("800x700")
root.resizable(False, False)
root.title("Age Caluculator")

root.config(background = "#8EB8E5")

#Calculation function
def calculateAge(): 
  today=date.today()
  try:
    if int(monthEntry.get()) > 12:
      result.config(text=f"I don't think that's possible, {nameValue.get()}",font=30)
    elif int(dayEntry.get()) > 31:
      result.config(text=f"I don't think that's possible, {nameValue.get()}",font=30)
    else:
      birthDate=date(int(yearEntry.get()), int(monthEntry.get()), int(dayEntry.get()))
      age = today.year - birthDate.year - ((today.month,today.day)<(birthDate.month,birthDate.day))
      months = (today.year - birthDate.year) * 12 + birthDate.month 
      days = (today.year - birthDate.year) * 365 + (birthDate.month * 30.437) + birthDate.day
      seconds = ((today.year - birthDate.year) * 365 * 86400) + (birthDate.month * 30.437 * 86400) + (birthDate.day * 86400)

      if age > 0:
        result.config(text=f"{nameValue.get()}, you are {age} years old, and also about...\n{months} months old.\n {days} days old.\n {seconds} seconds old.",font=30)
        result.place(x=230, y=510)
      elif age <= 0:
        result.config(text=f"I don't think that's possible, {nameValue.get()}",font=30)
  except ValueError:
    result.config(text=f"Enter real numbers!",font=30)
  else:
    pass


#GUI Setup

title = Label(text="CALCULATE YOUR AGE!", font=('Roboto', 25))
title.config(bg = "#8EB8E5", fg = "#492C1D")
title.place(x = 190, y = 100)

#Labels 
Label(text="Name", font=24, bg = "#8EB8E5").place(x=200, y=200)
Label(text="Year", font=24, bg = "#8EB8E5").place(x=200, y=250)
Label(text="Month", font=24, bg = "#8EB8E5").place(x=200, y=300)
Label(text="Day", font=24, bg = "#8EB8E5").place(x=200, y=350)

nameValue = StringVar()
yearValue = StringVar()
monthValue = StringVar()
dayValue = StringVar()

#Entry Boxes
nameEntry=Entry(root,textvariable=nameValue, width=20,bd=3,font=20, bg = "#5B5750", fg = "#FFF1BF")
nameEntry.place(x=370, y = 200)

yearEntry=Entry(root,textvariable=yearValue, width=20,bd=3,font=20, bg = "#5B5750", fg = "#FFF1BF")
yearEntry.place(x=370, y = 250)

monthEntry=Entry(root,textvariable=monthValue, width=20,bd=3,font=20, bg = "#5B5750", fg = "#FFF1BF")
monthEntry.place(x=370, y = 300)

dayEntry=Entry(root,textvariable=dayValue, width=20,bd=3,font=20, bg = "#5B5750", fg = "#FFF1BF")
dayEntry.place(x=370, y = 350)

#Result
result = Label(text="",font=30)
result.config(bg = "#8EB8E5")
result.place(x=300,y=520)

#Button
Button(text="Calculate Age", font=20, bg="#492C1D", fg="white", width=10, height=2, command=calculateAge).place(x=325, y=450)


root.mainloop()
