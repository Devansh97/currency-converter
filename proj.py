from Tkinter import *
from tkMessageBox import *
import random
root1=Tk()
def enter():
    
    root=Toplevel(root1)
    root.title('Currency Convertor')

    e=Entry(root,width=25,font='Arial 30 bold',bd=7,bg='Orange',justify='right')
    e.grid(row=0,column=0,columnspan=3)

    v1=IntVar()
    v2=IntVar()


    def add_entry(x):
        e.insert(16,x)
    def clear():
        e.delete(0,END)
    def backspace():
        e.delete((len(e.get())-1),END)
    #------------------------------------------------------------Conversion Function---------------------------------------------------------------------------------------
    def convert():
        if v1.get()==1:
            if v2.get()==1:
                x1=float(e.get())
                showinfo(title='INR to INR',message=x1*1)
            elif v2.get()==2:
                x2=float(e.get())
                showinfo(title='INR to $',message=x2*0.015)
            elif v2.get()==3:
                x3=float(e.get())
                showinfo(title='INR to Yen',message=x3*1.65)
            elif v2.get()==4:
                x4=float(e.get())
                showinfo(title='INR to Pound',message=x4*0.012)
            elif v2.get()==5:
                x5=float(e.get())
                showinfo(title='INR to Euro',message=x5*0.014)
            elif v2.get()==6:
                x6=float(e.get())
                showinfo(title='INR to Ruble',message=x6*0.94)
            elif v2.get()==7:
                x7=float(e.get())
                showinfo(title='INR to Dinar',message=x7*17.01)
            elif v2.get()==8:
                x8=float(e.get())
                showinfo(title='INR to Peso',message=x8*0.30)
            elif v2.get()==9:
                x9=float(e.get())
                showinfo(title='INR to Yuan',message=x9*0.10)
            else:
                x10=float(e.get())
                showinfo(title='INR to Dirham',message=x10*0.054)
                
        elif v1.get()==2:
            if v2.get()==1:
                x1=float(e.get())
                showinfo(title='$ to INR',message=x1*68.76)
            elif v2.get()==2:
                x2=float(e.get())
                showinfo(title='$ to $',message=x2*1)
            elif v2.get()==3:
                x3=float(e.get())
                showinfo(title='$ to Yen',message=x3*113.39)
            elif v2.get()==4:
                x4=float(e.get())
                showinfo(title='$ to Pound',message=x4*0.80)
            elif v2.get()==5:
                x5=float(e.get())
                showinfo(title='$ to Euro',message=x5*0.95)
            elif v2.get()==6:
                x6=float(e.get())
                showinfo(title='$ to Ruble',message=x6*64.53)
            elif v2.get()==7:
                x7=float(e.get())
                showinfo(title='$ to Dinar',message=x7*1164.20)
            elif v2.get()==8:
                x8=float(e.get())
                showinfo(title='$ to Peso',message=x8*20.70)
            elif v2.get()==9:
                x9=float(e.get())
                showinfo(title='$ to Yuan',message=x9*6.92)
            else:
                x10=float(e.get())
                showinfo(title='$ to Dirham',message=x10*3.67)
                
        elif v1.get()==3:
            if v2.get()==1:
                x1=float(e.get())
                showinfo(title='Yen to INR',message=x1*0.61)
            elif v2.get()==2:
                x2=float(e.get())
                showinfo(title='Yen to $',message=x2*0.0088)
            elif v2.get()==3:
                x3=float(e.get())
                showinfo(title='Yen to Yen',message=x3*1)
            elif v2.get()==4:
                x4=float(e.get())
                showinfo(title='Yen to Pound',message=x4*0.0071)
            elif v2.get()==5:
                x5=float(e.get())
                showinfo(title='Yen to Euro',message=x5*0.0084)
            elif v2.get()==6:
                x6=float(e.get())
                showinfo(title='Yen to Ruble',message=x6*0.57)
            elif v2.get()==7:
                x7=float(e.get())
                showinfo(title='Yen to Dinar',message=x7*10.31)
            elif v2.get()==8:
                x8=float(e.get())
                showinfo(title='Yen to Peso',message=x8*0.18)
            elif v2.get()==9:
                x9=float(e.get())
                showinfo(title='Yen to Yuan',message=x9*0.061)
            else:
                x10=float(e.get())
                showinfo(title='Yen to Dirham',message=x10*0.033)
            
        elif v1.get()==4:
            if v2.get()==1:
                x1=float(e.get())
                showinfo(title='Pound to INR',message=x1*85.57)
            elif v2.get()==2:
                x2=float(e.get())
                showinfo(title='Pound to $',message=x2*1.24)
            elif v2.get()==3:
                x3=float(e.get())
                showinfo(title='Pound to Yen',message=x3*141.20)
            elif v2.get()==4:
                x4=float(e.get())
                showinfo(title='Pound to Pound',message=x4*1)
            elif v2.get()==5:
                x5=float(e.get())
                showinfo(title='Pound to Euro',message=x5*1.18)
            elif v2.get()==6:
                x6=float(e.get())
                showinfo(title='Pound to Ruble',message=x6*80.42)
            elif v2.get()==7:
                x7=float(e.get())
                showinfo(title='Pound to Dinar',message=x7*1449.20)
            elif v2.get()==8:
                x8=float(e.get())
                showinfo(title='Pound to Peso',message=x8*25.68)
            elif v2.get()==9:
                x9=float(e.get())
                showinfo(title='Pound to Yuan',message=x9*8.61)
            else:
                x10=float(e.get())
                showinfo(title='Pound to Dirham',message=x10*4.57)
                
        elif v1.get()==5:
            if v2.get()==1:
                x1=float(e.get())
                showinfo(title='Euro to INR',message=x1*72.58)
            elif v2.get()==2:
                x2=float(e.get())
                showinfo(title='Euro to $',message=x2*1.06)
            elif v2.get()==3:
                x3=float(e.get())
                showinfo(title='Euro to Yen',message=x3*119.71)
            elif v2.get()==4:
                x4=float(e.get())
                showinfo(title='Euro to Pound',message=x4*0.85)
            elif v2.get()==5:
                x5=float(e.get())
                showinfo(title='Euro to Euro',message=x5*1)
            elif v2.get()==6:
                x6=float(e.get())
                showinfo(title='Euro to Ruble',message=x6*68.41)
            elif v2.get()==7:
                x7=float(e.get())
                showinfo(title='Euro to Dinar',message=x7*1230.16)
            elif v2.get()==8:
                x8=float(e.get())
                showinfo(title='Euro to Peso',message=x8*21.84)
            elif v2.get()==9:
                x9=float(e.get())
                showinfo(title='Euro to Yuan',message=x9*7.33)
            else:
                x10=float(e.get())
                showinfo(title='Euro to Dirham',message=x10*3.89)

        elif v1.get()==6:
            if v2.get()==1:
                x1=float(e.get())
                showinfo(title='Ruble to INR',message=x1*1.06)
            elif v2.get()==2:
                x2=float(e.get())
                showinfo(title='Ruble to $',message=x2*0.015)
            elif v2.get()==3:
                x3=float(e.get())
                showinfo(title='Ruble to Yen',message=x3*1.75)
            elif v2.get()==4:
                x4=float(e.get())
                showinfo(title='Ruble to Pound',message=x4*0.012)
            elif v2.get()==5:
                x5=float(e.get())
                showinfo(title='Ruble to Euro',message=x5*0.015)
            elif v2.get()==6:
                x6=float(e.get())
                showinfo(title='Ruble to Ruble',message=x6*1)
            elif v2.get()==7:
                x7=float(e.get())
                showinfo(title='Ruble to Dinar',message=x7*17.97)
            elif v2.get()==8:
                x8=float(e.get())
                showinfo(title='Ruble to Peso',message=x8*0.32)
            elif v2.get()==9:
                x9=float(e.get())
                showinfo(title='Ruble to Yuan',message=x9*0.11)
            else:
                x10=float(e.get())
                showinfo(title='Ruble to Dirham',message=x10*0.057)

        elif v1.get()==7:
            if v2.get()==1:
                x1=float(e.get())
                showinfo(title='Dinar to INR',message=x1*0.059)
            elif v2.get()==2:
                x2=float(e.get())
                showinfo(title='Dinar to $',message=x2*0.00086)
            elif v2.get()==3:
                x3=float(e.get())
                showinfo(title='Dinar to Yen',message=x3*0.097)
            elif v2.get()==4:
                x4=float(e.get())
                showinfo(title='Dinar to Pound',message=x4*0.00069)
            elif v2.get()==5:
                x5=float(e.get())
                showinfo(title='Dinar to Euro',message=x5*0.00081)
            elif v2.get()==6:
                x6=float(e.get())
                showinfo(title='Dinar to Ruble',message=x6*0.056)
            elif v2.get()==7:
                x7=float(e.get())
                showinfo(title='Dinar to Dinar',message=x7*1)
            elif v2.get()==8:
                x8=float(e.get())
                showinfo(title='Dinar to Peso',message=x8*0.018)
            elif v2.get()==9:
                x9=float(e.get())
                showinfo(title='Dinar to Yuan',message=x9*0.0060)
            else:
                x10=float(e.get())
                showinfo(title='Dinar to Dirham',message=x10*0.0032)

        elif v1.get()==8:
            if v2.get()==1:
                x1=float(e.get())
                showinfo(title='Peso to INR',message=x1*3.32)
            elif v2.get()==2:
                x2=float(e.get())
                showinfo(title='Peso to $',message=x2*0.048)
            elif v2.get()==3:
                x3=float(e.get())
                showinfo(title='Peso to Yen',message=x3*5.47)
            elif v2.get()==4:
                x4=float(e.get())
                showinfo(title='Peso to Pound',message=x4*0.039)
            elif v2.get()==5:
                x5=float(e.get())
                showinfo(title='Peso to Euro',message=x5*0.046)
            elif v2.get()==6:
                x6=float(e.get())
                showinfo(title='Peso to Ruble',message=x6*3.13)
            elif v2.get()==7:
                x7=float(e.get())
                showinfo(title='Peso to Dinar',message=x7*56.30)
            elif v2.get()==8:
                x8=float(e.get())
                showinfo(title='Peso to Peso',message=x8*1)
            elif v2.get()==9:
                x9=float(e.get())
                showinfo(title='Peso to Yuan',message=x9*0.34)
            else:
                x10=float(e.get())
                showinfo(title='Peso to Dirham',message=x10*0.18)

        elif v1.get()==9:
            if v2.get()==1:
                x1=float(e.get())
                showinfo(title='Yuan to INR',message=x1*9.90)
            elif v2.get()==2:
                x2=float(e.get())
                showinfo(title='Yuan to $',message=x2*0.14)
            elif v2.get()==3:
                x3=float(e.get())
                showinfo(title='Yuan to Yen',message=x3*16.32)
            elif v2.get()==4:
                x4=float(e.get())
                showinfo(title='Yuan to Pound',message=x4*0.12)
            elif v2.get()==5:
                x5=float(e.get())
                showinfo(title='Yuan to Euro',message=x5*0.14)
            elif v2.get()==6:
                x6=float(e.get())
                showinfo(title='Yuan to Ruble',message=x6*9.34)
            elif v2.get()==7:
                x7=float(e.get())
                showinfo(title='Yuan to Dinar',message=x7*167.84)
            elif v2.get()==8:
                x8=float(e.get())
                showinfo(title='Yuan to Peso',message=x8*2.98)
            elif v2.get()==9:
                x9=float(e.get())
                showinfo(title='Yuan to Yuan',message=x9*1)
            else:
                x10=float(e.get())
                showinfo(title='Yuan to Dirham',message=x10*0.53)

        else:
            if v2.get()==1:
                x1=float(e.get())
                showinfo(title='Dirham to INR',message=x1*18.65)
            elif v2.get()==2:
                x2=float(e.get())
                showinfo(title='Dirham to $',message=x2*0.27)
            elif v2.get()==3:
                x3=float(e.get())
                showinfo(title='Dirham to Yen',message=x3*30.74)
            elif v2.get()==4:
                x4=float(e.get())
                showinfo(title='Dirham to Pound',message=x4*0.22)
            elif v2.get()==5:
                x5=float(e.get())
                showinfo(title='Dirham to Euro',message=x5*0.26)
            elif v2.get()==6:
                x6=float(e.get())
                showinfo(title='Dirham to Ruble',message=x6*17.58)
            elif v2.get()==7:
                x7=float(e.get())
                showinfo(title='Dirham to Dinar',message=x7*316.19)
            elif v2.get()==8:
                x8=float(e.get())
                showinfo(title='Dirham to Peso',message=x8*5.62)
            elif v2.get()==9:
                x9=float(e.get())
                showinfo(title='Dirham to Yuan',message=x9*1.88)
            else:
                x10=float(e.get())
                showinfo(title='Dirham to Dirham',message=x10*1)
            
    #--------------------------------------------------------------------RadioButtons--------------------------------------------------------------------------------------
                
    Label(root,text="From",font='Arial 40 bold').grid(row=5,column=0,sticky=N+W+E+S,columnspan=2)
    Radiobutton(root,text="INR",padx=20,variable=v1,value=1).grid(row=6,column=0,sticky=N+W)
    Radiobutton(root,text="$",padx=20,variable=v1,value=2).grid(row=7,column=0,sticky=N+W)
    Radiobutton(root,text="Yen",padx=20,variable=v1,value=3).grid(row=8,column=0,sticky=N+W)
    Radiobutton(root,text="Pound",padx=20,variable=v1,value=4).grid(row=9,column=0,sticky=N+W)
    Radiobutton(root,text="Euro",padx=20,variable=v1,value=5).grid(row=10,column=0,sticky=N+W)
    Radiobutton(root,text="Ruble",padx=20,variable=v1,value=6).grid(row=6,column=1,sticky=N+W)
    Radiobutton(root,text="Dinar",padx=20,variable=v1,value=7).grid(row=7,column=1,sticky=N+W)
    Radiobutton(root,text="Peso",padx=20,variable=v1,value=8).grid(row=8,column=1,sticky=N+W)
    Radiobutton(root,text="Yuan",padx=20,variable=v1,value=9).grid(row=9,column=1,sticky=N+W)
    Radiobutton(root,text="Dirham",padx=20,variable=v1,value=10).grid(row=10,column=1,sticky=N+W)

    Label(root,text="To",font='Arial 40 bold').grid(row=5,column=4,sticky=N+W+E+S,columnspan=2)
    Radiobutton(root,text="INR",padx=20,variable=v2,value=1 ).grid(row=6,column=4,sticky=N+W)
    Radiobutton(root,text="$",padx=20,variable=v2,value=2).grid(row=7,column=4,sticky=N+W)
    Radiobutton(root,text="Yen",padx=20,variable=v2,value=3).grid(row=8,column=4,sticky=N+W)
    Radiobutton(root,text="Pound",padx=20,variable=v2,value=4).grid(row=9,column=4,sticky=N+W)
    Radiobutton(root,text="Euro",padx=20,variable=v2,value=5).grid(row=10,column=4,sticky=N+W)
    Radiobutton(root,text="Ruble",padx=20,variable=v2,value=6).grid(row=6,column=5,sticky=N+W)
    Radiobutton(root,text="Dinar",padx=20,variable=v2,value=7).grid(row=7,column=5,sticky=N+W)
    Radiobutton(root,text="Peso",padx=20,variable=v2,value=8).grid(row=8,column=5,sticky=N+W)
    Radiobutton(root,text="Yuan",padx=20,variable=v2,value=9).grid(row=9,column=5,sticky=N+W)
    Radiobutton(root,text="Dirham",padx=20,variable=v2,value=10).grid(row=10,column=5,sticky=N+W)
    #----------------------------------------------------------------------------------------------------------------------------------------------------------------------
    Button(root,text='7',width=20,height=5,command=lambda:add_entry('7'),bg='Light Blue').grid(row=1,column=0,sticky=E+W+N+S,columnspan=1)
    Button(root,text='8',width=20,height=5,command=lambda:add_entry('8'),bg='Light Blue').grid(row=1,column=1,sticky=E+W+N+S,columnspan=1)
    Button(root,text='9',width=20,height=5,command=lambda:add_entry('9'),bg='Light Blue').grid(row=1,column=2,sticky=E+W+N+S,columnspan=1)

    Button(root,text='4',width=20,height=5,command=lambda:add_entry('4'),bg='Light Blue').grid(row=2,column=0,sticky=E+W+N+S,columnspan=1)
    Button(root,text='5',width=20,height=5,command=lambda:add_entry('5'),bg='Light Blue').grid(row=2,column=1,sticky=E+W+N+S,columnspan=1)
    Button(root,text='6',width=20,height=5,command=lambda:add_entry('6'),bg='Light Blue').grid(row=2,column=2,sticky=E+W+N+S,columnspan=1)

    Button(root,text='1',width=20,height=5,command=lambda:add_entry('1'),bg='Light Blue').grid(row=3,column=0,sticky=E+W+N+S,columnspan=1)
    Button(root,text='2',width=20,height=5,command=lambda:add_entry('2'),bg='Light Blue').grid(row=3,column=1,sticky=E+W+N+S,columnspan=1)
    Button(root,text='3',width=20,height=5,command=lambda:add_entry('3'),bg='Light Blue').grid(row=3,column=2,sticky=E+W+N+S,columnspan=1)

    Button(root,text='.',width=20,height=5,command=lambda:add_entry('.'),bg='Light Blue').grid(row=4,column=0,sticky=E+W+N+S,columnspan=1)
    Button(root,text='0',width=20,height=5,command=lambda:add_entry('0'),bg='Light Blue').grid(row=4,column=1,sticky=E+W+N+S,columnspan=1)
    Button(root,text='C',width=20,height=5,command=lambda:clear(),bg='Light Blue').grid(row=4,column=2,sticky=E+W+N+S,columnspan=1)

    Button(root,padx=16,bd=4,fg='black',font='Arial 16 bold',width=5,text="Convert",command=lambda:convert()).grid(row=17,column=2)

    root.mainloop()
root1.attributes('-fullscreen',True)
i1=PhotoImage(file="Money.gif")
l1=Label(root1,image=i1,font="Arial 70 bold",text=" Currency Convertor      ",compound=CENTER,bd=10,fg='red')
def aboutus():
        master=Tk()
        
        master.attributes('-fullscreen',True)

        shortcutbar = Frame(master, height=30, bg='light green')
        Button(shortcutbar,justify=CENTER,text='CLOSE',activeforeground='khaki',overrelief=SOLID,relief=GROOVE,command=master.destroy,bg='red',activebackground='#00A0A0').pack(side=RIGHT,anchor=NE,fill=Y)
        toolbar = Label(shortcutbar, text='CURRENCY CONVERTOR',bg='yellow',fg='dark green',font='CalibriLight 25 bold')
        
        toolbar.pack(side=TOP,fill=X)
        
        shortcutbar.pack(side=TOP,fill=X)
        Label(master, text='').pack(side=TOP,fill=X)
        Label(master,text=" ").pack(side=TOP,expand=NO, fill=X)
        Label(master,text=" ").pack(side=TOP,expand=NO, fill=X)
        Label(master,text=" ").pack(side=TOP,expand=NO, fill=X)
        Label(master,text=" ").pack(side=TOP,expand=NO, fill=X)
        Label(master, text='\n\n\n\n\nYOU CAN CONTACT US ON',fg='black',font='Constantia 18 bold').pack(side=TOP,anchor=CENTER)
        #Label(master, text='BOBBY SHUKLA ( 9412349479 )\nDEEPU SHUKLA ( 9997990597 )',fg='blue',font='castellar 20 bold').pack(side=TOP,anchor=CENTER)
        Label(master, text='DEVANSH BABBAR\n( 7240915271 ) ',fg='blue',font='castellar 20 bold').pack(side=TOP,anchor=CENTER)

        Label(master, text='Email : devubabbar@gmail.com',fg='#00A0A0',font='Rockwell 15 bold',relief=RAISED,width=50).pack(side=BOTTOM,anchor=CENTER,fill=X)
        Label(master,text='Project made by :  DEVANSH BABBAR',justify=CENTER,relief=RIDGE,fg='brown',font='Georgia 18 bold',bg='khaki').pack(side=BOTTOM,fill=X)
        #s = Frame(master, height=30, bg='light green')
        #Button(s, text='EXIT',justify=CENTER,cursor="hand2",relief=RIDGE,width=16,height=1,bg='light blue',fg='black',font='SegoeUISemibold 15 bold',command=master.destroy,activebackground='#00A0A0').pack(side=LEFT, anchor=SW)
        #s.pack(side=BOTTOM,expand=NO, fill=X)

Button(l1,padx=16,bd=4,fg='black',font='Arial 16 bold',width=5,text="About Us",command=aboutus).pack(side=RIGHT,anchor=E)
Button(l1,padx=16,bd=4,fg='black',font='Arial 16 bold',width=5,text="ENTER",command=enter).pack(side=TOP,anchor=N)
Button(l1,padx=16,bd=4,fg='black',font='Arial 16 bold',width=5,text="EXIT",command=root1.destroy).pack(side=BOTTOM,anchor=S)
l1.pack(side=TOP,fill="both",expand="yes")
root1.mainloop()

