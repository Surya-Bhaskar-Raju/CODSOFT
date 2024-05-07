import sys
import csv

def add(i):
    with open('data.csv','a+',newline='') as file:
        writer=csv.writer(file)
        writer.writerow(i)
# add(['raju','M','232','data@gmail.com'])
# add(['ravi','F','1234','resa@gmail.com'])

def view():
    data=[]
    with open("data.csv") as file:
        reader=csv.reader(file)
        for i in reader:
            if not []:
                data.append(i)
    return data
# view()
        
def remove(i):
    def save(j):
        with open('data.csv','w',newline='') as f:
            writer=csv.writer(f)
            writer.writerows(j)
    l=[]
    telephone=i
    with open('data.csv','r') as file:
        reader=csv.reader(file)
        for row in reader:
            l.append(row)
            for element in row:
                if element==telephone:
                    l.remove(row)
    save(l)

def update(i):
    def update_newlist(j):
        with open('data.csv','w',newline='') as file:
            w=csv.writer(file)
            w.writerows(j)
    l=[]
    telephone=i[0]
    with open('data.csv','r') as file:
        reader=csv.reader(file)
        for row in reader:
            l.append(row)
            for element in row:
                if element==telephone:
                    name=i[1]
                    gender=i[2]
                    telephone=i[3]
                    email=i[4]
                    data=[name,gender,telephone,email]
                    ind=l.index(row)
                    l[ind]=data
    update_newlist(l)     
sample=['232','asd','f','232','sfsd@gmail.com']
update(sample)       
                            
def search(i):
    data=[]
    telephone=i
    with open('data.csv','r') as f:
        r=csv.reader(f)
        for row in r:
            for element in row:
                if element==telephone:
                    data.append(row)
    return data
print(search('232'))
                