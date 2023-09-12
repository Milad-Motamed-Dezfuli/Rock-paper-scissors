from tkinter import *
r=Tk()
r.title('سنگ کاغذ قیچی')
h=Label(r, textvariable="hi", font=("Tohoma",20), pady=10,padx=10)
h.grid(columnspan=7)
pcchoice=StringVar()
result=StringVar()

# s emtiyaz karbar ast
s=0
#n emtiyaz pc
n=0
i=1
h=IntVar()
h.set(1)
def bazi(b):
    a=['sang','kaghaz','gheychi']
    import random as ra
    l=ra.choice(a)    
    pcchoice.set(l)
    global s 
    global n
    global i
    if b=="sang"and l=="gheychi" or b=="kaghaz" and l=="sang" or b=="gheychi" and l=="kaghaz":
        s=s+1
        if s<5:
            result.set("User :"+str(s)+" Pc : "+str(n))
    elif b==l:
        result.set("draw! "+ "User :"+str(s)+" Pc : "+str(n))
    if s>4:
        i=-1
        s=0 
        n=0
        result.set("You won!!! yay :) ")

    if n>4:
        i=-1
        s=0
        n=0
        result.set("Pc has won :( " )
    if l=="sang"and b=="gheychi" or l=="kaghaz" and b=="sang" or l=="gheychi" and b=="kaghaz":
        n=n+1
        if n<5:
            result.set("User : "+str(s)+" Pc : "+str(n))
    i=i+1
    h.set(i)
    


btn1=Button(r,text="سنگ "+"\n"+ "■",width=5,height=2, font=("Courier",20),command=lambda:bazi("sang"))
btn1.grid(row=1, column=0)
btn2=Button(r,text="کاغذ "+"\n"+ " ▒",width=5,height=2, font=("Tohoma",20),command=lambda:bazi("kaghaz"))
btn2.grid(row=1, column=1)
btn3=Button(r,text="قیچی "+"\n"+ " ◄",width=5,height=2, font=("Tohoma",20),command=lambda:bazi("gheychi"))
btn3.grid(row=1, column=3)

Label(r,text="",bg="lightgrey").grid(row=2,column=134)
Label(r,text="",bg="lightgrey").grid(row=3,column=134)
Label(r,text="round number ",font=("Arial",15)).grid(row=4,column=0)
Label(r,textvariable=h,font=("Arial",15)).grid(row=4,column=1)


Label(r,text="Pc's choice was : ",font=("Arial",15)).grid(row=6,column=0)
Label(r,textvariable=pcchoice,font=("Arial",15)).grid(row=6,column=1)
Label(r,text="",bg="lightgrey").grid(row=7,column=134)


Label(r,text="",bg="lightgrey").grid(row=5,column=134)
Label(r,text="Results : ",font=("Arial",20)).grid(row=8,column=0)
Label(r,textvariable=result  ,font=("Arial",15)).grid(row=8,column=1)

mainloop()