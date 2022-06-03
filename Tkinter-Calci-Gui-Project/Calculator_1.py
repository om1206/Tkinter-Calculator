from tkinter import *
def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text =="=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                value = "INVALID OPERATIONS"

        scvalue.set(value)
        screen.update()

    elif text =="C":
        scvalue.set("")
        screen.update()



    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


root=Tk()
root.geometry("470x650")
root.title("Calculator made by MOJ ")
scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvariable=scvalue,font="Lucida 30 bold")
screen.pack(fill=X,ipadx=8,pady=11)


frame = Frame(root,bg="grey")
b = Button(frame, text="C",font="lucida 35 bold",fg="white",bg="black",)
b.pack(side=LEFT,padx=15,pady=10)
b.bind("<Button-1>",click)
b = Button(frame, text="%",font="lucida 35 bold",fg="white",bg="Black",)
b.pack(side=LEFT,padx=15,pady=10)
b.bind("<Button-1>",click)
b = Button(frame, text="del", font="lucida 35 bold", fg="white", bg="black")
b.pack(side=LEFT, padx=15, pady=10)
b.bind("<Button-1>", click)
b = Button(frame, text="÷",font="lucida 35 bold",fg="white",bg="black",)
b.pack(side=LEFT,padx=19,pady=10)
b.bind("<Button-1>",click)
frame.pack()

frame = Frame(root,bg="grey")
b = Button(frame, text="7",font="lucida 35 bold",fg="white",bg="black",)
b.pack(side=LEFT,padx=25,pady=10)
b.bind("<Button-1>",click)
b = Button(frame, text="8",font=" lucida 35 bold",fg="white",bg="black",)
b.pack(side=LEFT,padx=25,pady=10)
b.bind("<Button-1>",click)
b = Button(frame, text="9",font="lucida 35 bold",fg="white",bg="black",)
b.pack(side=LEFT,padx=25,pady=10)
b.bind("<Button-1>",click)
b = Button(frame, text="*",font="lucida 35 bold",fg="white",bg="black",)
b.pack(side=LEFT,padx=26,pady=10)
b.bind("<Button-1>",click)
frame.pack()

frame = Frame(root,bg="grey")
b = Button(frame, text="4",font="lucida 35 bold",fg="white",bg="black",)
b.pack(side=LEFT,padx=25,pady=10)
b.bind("<Button-1>",click)
b = Button(frame, text="5",font="lucida 35 bold",fg="white",bg="black",)
b.pack(side=LEFT,padx=25,pady=10)
b.bind("<Button-1>",click)
b = Button(frame, text="6",font="lucida 35 bold",fg="white",bg="black",)
b.pack(side=LEFT,padx=25,pady=10)
b.bind("<Button-1>",click)
b = Button(frame, text="- ",font="lucida 35 bold",fg="white",bg="black",)
b.pack(side=LEFT,padx=20,pady=10)
b.bind("<Button-1>",click)
frame.pack()

frame = Frame(root,bg="grey")
b = Button(frame, text="1",font="lucida 35 bold",fg="white",bg="black",)
b.pack(side=LEFT,padx=25,pady=10)
b.bind("<Button-1>",click)
b = Button(frame, text="2",font="lucida 35 bold",fg="white",bg="black",)
b.pack(side=LEFT,padx=25,pady=10)
b.bind("<Button-1>",click)
b = Button(frame, text="3",font="lucida 35 bold",fg="white",bg="black",)
b.pack(side=LEFT,padx=25,pady=10)
b.bind("<Button-1>",click)
b = Button(frame, text="+",font="lucida 35 bold",fg="white",bg="black",)
b.pack(side=LEFT,padx=20,pady=10)
b.bind("<Button-1>",click)
frame.pack()

frame = Frame(root,bg="grey")
b = Button(frame, text="00",font="lucida 35 bold",fg="white",bg="black",)
b.pack(side=LEFT,padx=25,pady=10)
b.bind("<Button-1>",click)
b = Button(frame, text="0",font="lucida 35 bold",fg="white",bg="black",)
b.pack(side=LEFT,padx=25,pady=10)
b.bind("<Button-1>",click)
b = Button(frame, text=".",font="lucida 35 bold",fg="white",bg="black",)
b.pack(side=LEFT,padx=25,pady=10)
b.bind("<Button-1>", click)
b = Button(frame, text="=",font="lucida 35 bold",fg="white",bg="black",)
b.pack(side=LEFT,padx=20,pady=10)
b.bind("<Button-1>",click)
frame.pack()
root.mainloop()