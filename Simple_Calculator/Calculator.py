from tkinter import *
expression=''



def press(num):
    global expression
    expression+=str(num)
    equation.set(expression)
    
def equalpress():
        
    try:
        global expression
        total=str(eval(expression))
        equation.set(total)
        expression=''
    
    except:
        
        equation.set('ERROR')
        expression=''
        
def clear():
    global expression
    expression=''
    equation.set('')
    
    
if __name__=="__main__":
    gui=Tk()
    gui.configure(background='#ACBDBA')
    gui.title("Simple Calculator")
    gui.geometry("270x150")
    
    equation=StringVar()
    
    expression_field=Entry(gui,textvariable=equation)
    
    expression_field.grid(columnspan=5,ipadx=80)
    
    
    b1=Button(gui,text='1',fg='white',bg='black',height=1,width=7,command=lambda: press('1'))
    b1.grid(row=2,column=0)
    b2=Button(gui,text='2',fg='white',bg='black',height=1,width=7,command=lambda: press('2'))
    b2.grid(row=2,column=1)
    b3=Button(gui,text='3',fg='white',bg='black',height=1,width=7,command=lambda: press('3'))
    b3.grid(row=2,column=2)
    b4=Button(gui,text='4',fg='white',bg='black',height=1,width=7,command=lambda: press('4'))
    b4.grid(row=3,column=0)
    b5=Button(gui,text='5',fg='white',bg='black',height=1,width=7,command=lambda: press(5))
    b5.grid(row=3,column=1)
    b6=Button(gui,text='6',fg='white',bg='black',height=1,width=7,command=lambda: press(6))
    b6.grid(row=3,column=2)
    b7=Button(gui,text='7',fg='white',bg='black',height=1,width=7,command=lambda: press(7))
    b7.grid(row=4,column=0)
    b8=Button(gui,text='8',fg='white',bg='black',height=1,width=7,command=lambda: press(8))
    b8.grid(row=4,column=1)
    b9=Button(gui,text='9',fg='white',bg='black',height=1,width=7,command=lambda: press(9))
    b9.grid(row=4,column=2)
    b0=Button(gui,text='0',fg='white',bg='black',height=1,width=7,command=lambda: press(0))
    b0.grid(row=5,column=1)
    
    plus=Button(gui,text='+',fg='white',bg='black',height=1,width=7,command=lambda: press('+'))
    plus.grid(row=2,column=3)
    
    minus=Button(gui,text='-',fg='white',bg='black',height=1,width=7,command=lambda: press('-'))
    minus.grid(row=3,column=3)
    
    multiply=Button(gui,text='*',fg='white',bg='black',height=1,width=7,command=lambda: press('*'))
    multiply.grid(row=4,column=3)
    
    divide=Button(gui,text='/',fg='white',bg='black',height=1,width=7,command=lambda: press('/'))
    divide.grid(row=5,column=3)
    
    equal=Button(gui,text='=',fg='white',bg='black',height=1,width=7,command=equalpress)
    equal.grid(row=5,column=2)
    
    dot=Button(gui,text='.',fg='white',bg='black',height=1,width=7,command=lambda: press('.'))
    dot.grid(row=5,column=0)
    
    clear=Button(gui,text='Clear',fg='red',bg='white',height=1,width=7,command=clear)
    clear.grid(row=0,column=3)
    
    
    
    
    
    
    gui.mainloop()
    