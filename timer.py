from tkinter import *
import time

root = Tk()

root.geometry("400x300+200+200")
root.title("Study Timer")
root.resizable(width = FALSE, height = FALSE)

def start1():
    my_string_var.set("Study Session")
    root.configure(background='green') # set the colour to the next colour generated
    root.after(7, countdowntimer)
#     root.after(33*60*1000, start2) # run this function again after 1000ms

def start2():
    my_string_var.set("Break")
    mins.set('30')
    root.configure(background='red') # set the colour to the next colour generated
    root.deiconify()
    root.lift()
    root.attributes('-topmost',True)
    root.after_idle(root.attributes,'-topmost',False)
    
def countdowntimer():
    times = int(hrs.get())*3600+ int(mins.get())*60 + int(sec.get())
    while times > -1:
        minute,second = (times // 60 , times % 60)
        hour =0
        if minute > 60:
            hour , minute = (minute // 60 , minute % 60)
        sec.set(second)
        mins.set(minute)
        hrs.set(hour)
        #Update the time
        root.update()
        time.sleep(1)
        if(times == 0):
            sec.set('00')
            mins.set('00')
            hrs.set('00')
            root.after(7, start2)
        times -= 1

my_string_var = StringVar()
my_string_var.set("Start")
my_label = Label(root,textvariable = my_string_var,font=("Arial", 25))

sec = StringVar()
Entry(root, textvariable=sec, width = 2, font = 'Helvetica 14').place(x=220, y=120)
sec.set('00')
mins= StringVar()
Entry(root, textvariable = mins, width =2, font = 'Helvetica 14').place(x=180, y=120)
mins.set('30')
hrs= StringVar()
Entry(root, textvariable = hrs, width =2, font = 'Helvetica 14').place(x=142, y=120)
hrs.set('00')

startButton = Button(root,width=15,text='start',command=start1)
my_label.pack()
startButton.pack()

root.mainloop()