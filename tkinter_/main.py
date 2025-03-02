import tkinter

window = tkinter.Tk()
window.title("MILE TO KM CONVERTER")
window.minsize(100,100)

# LABELS
label = tkinter.Label(text="Miles", font=("arial",12))
label.grid(row=2,column=7)

label2 = tkinter.Label(text="is equal to", font=("arial",12))
label3 = tkinter.Label(text="0", font=("arial",12))
label4 = tkinter.Label(text="Km", font=("arial",12))
label2.grid(row=3,column=1)
label3.grid(row=3,column=5)
label4.grid(row=3,column=7)
def button_clicked():
    miles = float(entry.get())
    km = round(miles * 1.609344)
    label3.config(text=km)
    
# BUTTONS
button = tkinter.Button(text="Calculate" , command=button_clicked)
button.grid(row=4,column=5)

entry = tkinter.Entry(width=10)
# entry.insert(tkinter.END, string="Email")
entry.grid(row=2,column=5)
entry.get()

# # TEXT

# text_box = tkinter.Text(width= 30 , height=5)
# text_box.focus()
# text_box.pack()

# # SPINBOX
# spinbox = tkinter.Spinbox(from_ = 0 , to=300)
# spinbox.pack()

# # SCALE
# scale = tkinter.Scale(from_=0 , to= 10)
# scale.pack()

# #CHECK BOX
# checked_state =     tkinter.IntVar()
# check_button = tkinter.Checkbutton(text="Is On")
# check_button.pack()

# # CHECKED BUTTON
# radio_state = tkinter.IntVar()
# rb_1 = tkinter.Radiobutton(text ="Option 1", value = 1, variable = radio_state)
# rb_2 = tkinter.Radiobutton(text ="Option 2", value = 2, variable = radio_state)
# rb_1.pack()
# rb_2.pack()

# # LIST BOX
# listbox = tkinter.Listbox(height=4)
# fruits = ["apple","mango","orange","pineapple"]
# for fruit in fruits:
#     listbox.insert(fruits.index(fruit), fruit)
# listbox.bind("<<ListboxSelect")

# listbox.pack()


window.mainloop()