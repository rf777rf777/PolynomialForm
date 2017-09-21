from tkinter import Frame,Tk,Label,Entry,Button,END
from sympy import expand
import sys
import os

class Window(Frame):
  
    def __init__(self,master = None):
        Frame.__init__(self,master)
        self.master = master
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.label1 = Label(self,text = 'H = ')
        self.label1.grid(row=0, column=0,columnspan=1)
        self.inputField1 = Entry(self,width = 15)
        self.inputField1.grid(row=0, column=1, columnspan=1)
        self.label2 = Label(self,text = 'X + ')
        self.label2.grid(row=0, column=2,columnspan=1)
        self.inputField2 = Entry(self,width = 15)
        self.inputField2.grid(row=0, column=3, columnspan=1)

        self.label3 = Label(self,text = 'Q = ')
        self.label3.grid(row=1,column=0,columnspan=1)
        self.inputField3 = Entry(self,width = 15)
        self.inputField3.grid(row=1,column=1, columnspan=1)
        self.label4 = Label(self,text = 'H ^ 2 +')
        self.label4.grid(row=1,column=2,columnspan=1)
        self.inputField4 = Entry(self,width = 15)
        self.inputField4.grid(row=1,column=3, columnspan=1)
        self.label5 = Label(self,text = 'H')
        self.label5.grid(row=1,column=4,columnspan=1)

        self.label6 = Label(self,text = '')
        self.label6.grid(row=2,column=0,columnspan=1)
        self.start = Button(self,text = '展開',width=10,command=self.click)
        self.start.grid(row=3, column=0,columnspan=1)

        self.label7 = Label(self,text = '')
        self.label7.grid(row=4,column=0,columnspan=1)
        self.label8 = Label(self,text = '展開結果:')
        self.label8.grid(row=5,column=0,columnspan=1)

        self.outputField = Entry(self,width = 45,text='')
        self.outputField.grid(row=5,column=1,columnspan=3)

    def click(self):
        string_H = '({})*X+({})'.format(self.inputField1.get(),self.inputField2.get())
        string_Q = '({})*({string_H})^2+({})*({string_H})'.format(self.inputField3.get(),self.inputField4.get(),string_H = string_H)

        self.outputField.delete(0,END)
        string_Error = "發生錯誤，請檢查輸入式！"
        try:
            self.outputField.insert(0,self.calculate(string_Q)) 
        except:
            self.outputField.insert(0,string_Error)
        

    def calculate(self,function):
        return expand(function)
        

root = Tk()
root.title('一元二次多項式展開')
if os.name == 'mac':
    root.geometry("600x170")
elif os.name == 'nt':
    root.geometry("420x150")
Window(root)
root.mainloop()