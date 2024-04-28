from tkinter import *
import random

computer_values={
    '0':'ROCK',
    '1':'PAPER',
    '2':'SCISSORS'
}

   
def reset():
    b1['state']='active'
    b2['state']='active'
    b3['state']='active'
    l1.config(text='Player       ')
    l3.config(text='        Computer')
    l4.config(text='')
    
def disable():
    b1['state']='disable'
    b2['state']='disable'
    b3['state']='disable'

def isrock():
    computer=computer_values[str(random.randint(0,2))]
    if computer=='ROCK':
        result='MATCH DRAW'
    elif computer=='PAPER':
        result='COMPUTER WINS'
    else:
        result='PLAYER WINS'
    l4.config(text=result)
    l1.config(text='ROCK          ')
    l3.config(text='       '+computer)
    disable()    
    
def ispaper():
    computer=computer_values[str(random.randint(0,2))]
    if computer=='ROCK':
        result='PLAYER WINS'
    elif computer=='PAPER':
        result='MATCH DRAW'
    else:
        result='COMPUTER WINS'
    l4.config(text=result)
    l1.config(text='PAPER         ')
    l3.config(text='       '+computer)
    disable()   

def isscissors():
    computer=computer_values[str(random.randint(0,2))]
    if computer=='ROCK':
        result='COMPUTER WINS'
    elif computer=='PAPER':
        result='PLAYER WINS'
    else:
        result='MATCH DRAW'
    l4.config(text=result)
    l1.config(text='SCISSORS     ')
    l3.config(text='       '+computer)
    disable()  
    
    
root=Tk()
root.geometry('600x600')
root.title('Rock Paper Scissors')
Label(root,text='ROCK PAPER SCISSORS',font='normal 20 underline bold',fg='black').pack(pady=60)


f1=Frame(root)
f1.pack()
l1=Label(f1,text='PLAYER        ',font=20)
l2=Label(f1,text='vs',font='normal 40 bold')
l3=Label(f1,text='       COMPUTER',font=20)
l1.pack(side=LEFT)
l2.pack(side=LEFT)
l3.pack(side=LEFT)
l4=Label(root,text='',font='normal 30 bold',bg='white',fg='red',width=20,borderwidth=2,relief='solid' )
l4.pack(pady=40)


f2=Frame(root)
f2.pack()
b1=Button(f2,text='ROCK',font=40,width=14,bd=2,command=isrock)
b1.pack(side=LEFT,padx=20)
b2=Button(f2,text='PAPER',font=40,width=14,bd=2,command=ispaper)
b2.pack(side=LEFT,padx=20)
b3=Button(f2,text='SCISSSORS',font=40,width=14,bd=2,command=isscissors)
b3.pack(side=LEFT,padx=20)

B=Button(root,text='RESET GAME',font=20,fg='white',bg='black',width=14,command=reset)
B.pack(pady=50)

root.mainloop()