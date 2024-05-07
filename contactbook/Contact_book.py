from tkinter import *
from tkinter import ttk
from views import *
from tkinter import messagebox
c0='#FDECEF'
c1='#0E3B43'
c2='#000000'

page=Tk()
page.title('CONTACT BOOK')
page.geometry('500x450')
page.config(bg=c0)
page.resizable(width=FALSE,height=FALSE)


#FRAMES 
frame1=Frame(page,bg=c1,width=500,height=50)
frame1.grid(row=0,column=0,padx=0,pady=1)
frame2=Frame(page,bg=c0,width=500,height=150)
frame2.grid(row=1,column=0,padx=0,pady=1)
frame3=Frame(page,bg=c0,width=500,height=100,relief='flat')
frame3.grid(row=2,columnspan=2,padx=10,pady=1,sticky=NW)

#functions
def show():
    header=['Name','Gender','Telephone','Email']
    demo=view()
    
    global tree
    tree=ttk.Treeview(frame3,selectmode='extended',columns=header,show='headings')
    v_scrollbar=ttk.Scrollbar(frame3,orient='vertical',command=tree.yview)
    h_scrollbar=ttk.Scrollbar(frame3,orient='horizontal',command=tree.xview)
    tree.config(yscrollcommand=v_scrollbar.set,xscrollcommand=h_scrollbar.set)
    
    tree.grid(column=0,row=0,sticky='nsew')
    v_scrollbar.grid(column=1,row=0,sticky='ns')
    h_scrollbar.grid(column=0,row=1,sticky='ew')
    
    tree.heading(0,text='Name',anchor=NW)
    tree.heading(1,text='Gender',anchor=NW)
    tree.heading(2,text='Telephone',anchor=NW)
    tree.heading(3,text='Email',anchor=NW)
    
    tree.column(0,width=120,anchor='nw')
    tree.column(1,width=70,anchor='nw')
    tree.column(2,width=100,anchor='nw')
    tree.column(3,width=180,anchor='nw')
    
    for item in demo:
        tree.insert('','end',values=item)
show()

def insert():
    name=e_name.get()
    gender=c_gender.get()
    telephone=e_telephone.get()
    email=e_email.get()
    
    data=[name,gender,telephone,email]
    
    if name=='' or gender=='' or telephone=='' or email=='':
        messagebox.showwarning('data','Please fill all the fields')
    else:
        add(data)
        messagebox.showinfo('data','Data added succesfully')
        e_name.delete(0,'end')
        c_gender.delete(0,'end')
        e_telephone.delete(0,'end')
        e_email.delete(0,'end')
        
        show()
        
def to_update():
    try:
        tree_data=tree.focus()
        tree_dictionary=tree.item(tree_data)
        tree_list=tree_dictionary['values']
        
        name=str(tree_list[0])
        gender=str(tree_list[1])
        telephone=str(tree_list[2])
        email=str(tree_list[3])
        
        e_name.insert(0,name)
        c_gender.insert(0,gender)
        e_telephone.insert(0,telephone)
        e_email.insert(0,email)
        
        def confirm():
            nname=e_name.get()
            ngender=c_gender.get()
            ntelephone=e_telephone.get()
            nemail=e_email.get()
            
            data=[ntelephone,nname,ngender,ntelephone,nemail]
            update(data)
            
            messagebox.showinfo('Success', 'Data is updated')
            
            e_name.delete(0,'end')
            c_gender.delete(0,'end')
            e_telephone.delete(0,'end')
            e_email.delete(0,'end')
        
            for widget in frame3.winfo_children():
                widget.destroy()
                
            b_confirm.destroy()
        
            show()
        b_confirm=Button(frame2,text='Confirm',width=8,height=1,bg=c1,fg=c0,font='Ivy 8 bold',command=confirm)
        b_confirm.place(x=290,y=110)
    except IndexError:
        messagebox.showerror('Error','Select on e of them from the table')
        
def to_del():
    try:
        tree_data=tree.focus()
        tree_dictionary=tree.item(tree_data)
        tree_list=tree_dictionary['values']
        t=str(tree_list[2])
        
        remove(t)
        
        messagebox.showinfo('Success','Data has been deleted Successfully')
        
        for widget in frame3.winfo_children():
            widget.destroy()
        show()
    except IndexError:
        messagebox.showerror('Error','Select one from the table')
        
def search_data():
    t=e_search.get()
    data=search(t)
    
    def delete_command():
        tree.delete(*tree.get_children())
    delete_command()
    
    for item in data:
        tree.insert('','end',values=item)
    e_search.delete(0,'end')
# frame1
Appname=Label(frame1,text="CONTACT BOOK",height=1,font='verdana 20 ',fg='#ffffff',bg=c1).place(x=7,y=6)

# frame2
l_name=Label(frame2,text='Name*',width=20,height=1,font='Ivy 10', bg="#ffffff",anchor=NW).place(x=10,y=20)
e_name=Entry(frame2,width=25, justify='left',highlightthickness=1,relief='solid')
e_name.place(x=80,y=20)

l_gender=Label(frame2,text='Gender',width=20,height=1,font='Ivy 10', bg="#ffffff",anchor=NW).place(x=10,y=50)
c_gender=ttk.Combobox(frame2,width=27)
c_gender['values']=['F','M']
c_gender.place(x=80,y=50)


l_telephone=Label(frame2,text='Telephone',width=20,height=1,font='Ivy 10', bg="#ffffff",anchor=NW).place(x=10,y=80)
e_telephone=Entry(frame2,width=25, justify='left',highlightthickness=1,relief='solid')
e_telephone.place(x=80,y=80)


l_email=Label(frame2,text='Email*',width=20,height=1,font='Ivy 10', bg="#ffffff",anchor=NW).place(x=10,y=110)
e_email=Entry(frame2,width=25, justify='left',highlightthickness=1,relief='solid')
e_email.place(x=80,y=110)

b_search=Button(frame2,text='Search',height=1,bg=c1,fg=c0,font='Ivy 8 bold',command=search_data).place(x=290,y=20)
e_search=Entry(frame2,width=16,justify='left',font='ivy 11',highlightthickness=1,relief='solid',)
e_search.place(x=350,y=20)

b_view=Button(frame2,text='View',width=8,height=1,bg=c1,fg=c0,font='Ivy 8 bold',command=show).place(x=290,y=50)

b_add=Button(frame2,text='Add',width=8,height=1,bg=c1,fg=c0,font='Ivy 8 bold',command=insert).place(x=400,y=50)

b_update=Button(frame2,text='Update',width=8,height=1,bg=c1,fg=c0,font='Ivy 8 bold',command=to_update).place(x=400,y=80)

b_delete=Button(frame2,text='Delete',width=8,height=1,bg=c1,fg=c0,font='Ivy 8 bold',command=to_del).place(x=400,y=110)


page.mainloop()