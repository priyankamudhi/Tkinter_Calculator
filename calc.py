import tkinter as tk

def click(x):
    entry.insert(tk.END,x)
def clear():
    entry.delete(0,tk.END)
def calc():
    try:
        result=eval(entry.get())
        entry.delete(0,tk.END)
        entry.insert(0,result)
    except:
        entry.delete(0,tk.END)
        entry.insert(0,"Error")
root=tk.Tk()
root.title("Calculator")
root.configure(bg="black")
root.resizable(1,1)
entry=tk.Entry(root,font=("arial",20),bg="red",fg="white",bd=0,justify="right")
entry.grid(row=0,column=0,columnspan=4,padx=5,pady=5,ipadx=5,ipady=5)

buttons=['7','8','9','/','4','5','6','*','1','2','3','-','0','.','=','+']
r=1
c=0
for b in buttons:
    cmd=calc if b=="=" else lambda x=b:click(x)
    tk.Button(root,text=b,command=cmd,font=("Arial",20),bg="green" if b in "+-*/=" else "black",fg="white",bd=0).grid(row=r,column=c,padx=3,pady=3,ipady=5)
    c=c+1
    if c==4:
        c=0
        r=r+1
tk.Button(root,text="clear",command=clear,font=("TNR",20),bg="red",fg="white",bd=0,width=20,height=5).grid(row=r,column=0,columnspan=4)
root.mainloop()    
  
