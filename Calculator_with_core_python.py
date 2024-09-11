#create a simple calculator using tkinter
def findsum():
    a=int(entryfirstnum.get())
    b=int(entrysecnum.get())
    sum=a+b;
    outputmsg=str(sum)
    labeloutput.configure(text=outputmsg)

def finddif():
    a=int(entryfirstnum.get())
    b=int(entrysecnum.get())
    dif=a-b;
    outputmsg=str(dif)
    labeloutput.configure(text=outputmsg)

def findpro():
    a=int(entryfirstnum.get())
    b=int(entrysecnum.get())
    pro=a*b;
    outputmsg=str(pro)
    labeloutput.configure(text=outputmsg)

def findquo():
    a=int(entryfirstnum.get())
    b=int(entrysecnum.get())
    quo=a/b;
    outputmsg=str(quo)
    labeloutput.configure(text=outputmsg)

import tkinter as bot

root_window=bot.Tk()
root_window.geometry('800x700')
root_window.configure(background= "coral")
root_window.title("Calculator")

#create the frame to hold the heading
frame1 = bot.Frame(master=root_window,padx=10,pady=10,background='red')
frame1.pack()

frame2 = bot.Frame(master=root_window,padx=10,pady=10,background='orange')
frame2.pack()

frame3 = bot.Frame(master=root_window,padx=10,pady=10,background='orange')
frame3.pack()

frame4 = bot.Frame(master=root_window,padx=10,pady=10,background='orange')
frame4.pack()

#create the heading
labelheading = bot.Label(master=frame1,text='Simple Calculator',background='red',font=('arial',24,'bold','underline'))

#Create input for the first number
labelfirstnum=bot.Label(master=frame2,text='Enter the first number:',background='orange',font=('arial',16,'bold'))

entryfirstnum=bot.Entry(master=frame2,font=('arial',16,'bold'))

#create input for the second number
labelsecnum=bot.Label(master=frame3,text='Enter the second number:',background='orange',font=('arial',16,'bold'))

entrysecnum=bot.Entry(master=frame3,font=('arial',16,'bold'))

#button part for computation
buttonsum = bot.Button(master=frame3,text='+',font=('arial',16,'bold'),command=findsum)
buttondif=bot.Button(master=frame3,text='-',font=("arial',16,'bold"),command=finddif)
buttonpro=bot.Button(master=frame3,text='x',font=('arial',16,'bold'),command=findpro)
buttonquo=bot.Button(master=frame3,text='/',font=('arial',16,'bold'),command=findquo)

#output
labeloutput=bot.Label(master=frame4,text='answer is seen here',font=('arial',16,'bold'))

#packing
labelheading.pack(pady=10)
labelfirstnum.pack(pady=10)
entryfirstnum.pack(pady=10)
labelsecnum.pack(pady=10)
entrysecnum.pack(pady=10)
buttonsum.pack(pady=10)
labeloutput.pack(pady=10)
buttondif.pack(pady=10)
buttonpro.pack(pady=10)
buttonquo.pack(pady=10)

root_window.mainloop()