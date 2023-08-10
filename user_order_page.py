import tkinter
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkvideo import *
import sqlite3
import os


log = Tk()
log.title("Restaurant Management System")
log.geometry("1024x768")
log.resizable(0, 0)

main_frame = Frame(log)
main_frame.pack()

# Menu Frame

# Adding Menu Background Image
menu_img = Image.open("D:/Python Final Assignment/menu_imgs/menu_back.jpg")
menu_img = menu_img.resize((600,768), Image.ANTIALIAS)
image_menu = ImageTk.PhotoImage(menu_img)
menu_img_label = Label(image = image_menu)
menu_img_label.place(x=0,y=0)


menu_frame = LabelFrame(main_frame, bd=10, width=600, height=768, padx=20, relief=RIDGE,
                           font=('Times New Roman', 12, 'bold'))
menu_frame.pack(side=LEFT)

# Billing Frame
billing_frame = LabelFrame(main_frame, bd=10, width=424, height=768, padx=20, relief=RIDGE,
                           font=('Times New Roman', 12, 'bold'), text="Billing Details:", fg="white", bg="#003e53")
billing_frame.pack(side=LEFT)


# Menu Items
# Food Items Buyer Values
momo = StringVar()
pizza = StringVar()
burger = StringVar()
fried_rice = StringVar()
sandwich = StringVar()
lassi = StringVar()
salad = StringVar()
spring_rolls = StringVar()
panipuri = StringVar()
samosa = StringVar()
chicken_wings = StringVar()
noodles = StringVar()
food_cost = StringVar()
service_charge = StringVar()
total = StringVar()

# Food item initial values
momo.set(0)
pizza.set(0)
burger.set(0)
fried_rice.set(0)
sandwich.set(0)
lassi.set(0)
salad.set(0)
spring_rolls.set(0)
panipuri.set(0)
samosa.set(0)
chicken_wings.set(0)
noodles.set(0)
food_cost.set(0)
service_charge.set(0)


def ref():

    # User Order Entry
    momo_order = float(item1_name.get())
    pizza_order = float(item2_name.get())
    burger_order = float(item3_name.get())
    fried_rice_order = float(item4_name.get())
    sandwich_order = float(item5_name.get())
    lassi_order = float(item6_name.get())
    salad_order = float(item7_name.get())
    spring_rolls_order = float(item8_name.get())
    panipuri_order = float(item9_name.get())
    samosa_order = float(item10_name.get())
    chicken_wings_order = float(item11_name.get())
    noodles_order = float(item12_name.get())

    # User Order Food item cost

    cost_of_momo = momo_order * 100
    cost_of_pizza = pizza_order * 100
    cost_of_burger = burger_order * 100
    cost_of_fried_rice = fried_rice_order * 100
    cost_of_sandwich = sandwich_order * 100
    cost_of_lassi = lassi_order * 100
    cost_of_salad = salad_order * 100
    cost_of_spring_rolls = spring_rolls_order * 100
    cost_of_panipuri = panipuri_order * 100
    cost_of_samosa = samosa_order * 100
    cost_of_chicken_wings = chicken_wings_order * 100
    cost_of_noodles = noodles_order * 100

    user_food_order_cost = (cost_of_momo + cost_of_pizza + cost_of_burger + cost_of_fried_rice + cost_of_sandwich + cost_of_lassi + cost_of_salad + cost_of_spring_rolls
                  + cost_of_panipuri + cost_of_samosa + cost_of_chicken_wings + cost_of_noodles)

    service_charge_cost = user_food_order_cost * 0.05

    total_cost = (user_food_order_cost + service_charge_cost)

    food_price = 'Rs ' + str('%.2f' % user_food_order_cost)

    service = 'Rs ' + str('%.2f' % service_charge_cost)

    total_price = 'Rs ' + str('%.2f' % total_cost)

    food_cost.set(food_price)
    service_charge.set(service)
    total.set(total_price)

# Reset function


def reset_values():
    momo.set(0)
    pizza.set(0)
    burger.set(0)
    fried_rice.set(0)
    sandwich.set(0)
    lassi.set(0)
    salad.set(0)
    spring_rolls.set(0)
    panipuri.set(0)
    samosa.set(0)
    chicken_wings.set(0)
    noodles.set(0)
    food_cost.set(0)
    service_charge.set(0)
    total.set(0)


def quit_app():
    response = messagebox.askyesno("QUIT???", "Are You Sure You Wan't To Quit ?")
    if response == 1:
        messagebox.showinfo("Happy Fooding", "😀😀😀Thank You😀😀😀")
        log.destroy()
    else:
        pass

# Item 1 image
item1_img = Image.open("D:/Python Final Assignment/menu_imgs/item1_img.jpg")
item1_img = item1_img.resize((100,100), Image.ANTIALIAS)
image1 = ImageTk.PhotoImage(item1_img)
item1_img_label = Label(image = image1)
item1_img_label.place(x=50,y=30)
# Item 1 name and order entry
item1_name_label = Label(font=('arial', 16, 'bold'),text="MOMO", anchor="w", fg="#003e53", bg="#949999")
item1_name_label.place(x=67, y=133)
item1_name = Entry(font=('arial',16,'bold'), textvariable=momo, bd=3, width=8, insertwidth=4, fg='#003e53', bg="dark grey", justify='center')
item1_name.place(x=50, y=160)

# Item 2 image
item2_img = Image.open("/Python Final Assignment/menu_imgs/item2_img.jpg")
item2_img = item2_img.resize((100,100), Image.ANTIALIAS)
image2 = ImageTk.PhotoImage(item2_img)
item2_img_label = Label(image = image2)
item2_img_label.place(x=250,y=30)
# Item 2 name and order entry
item2_name_label = Label(font=('arial', 16, 'bold'),text="PIZZA", anchor="w", fg="#003e53", bg="#949999")
item2_name_label.place(x=270, y=135)
item2_name = Entry(font=('arial',16,'bold'), textvariable=pizza, bd=3, width=8, insertwidth=4, fg='#003e53', bg="dark grey", justify='center')
item2_name.place(x=250, y=160)

# Item 3  image
item3_img = Image.open("D:/Python Final Assignment/menu_imgs/item3_img.jpg")
item3_img = item3_img.resize((100,100), Image.ANTIALIAS)
image3 = ImageTk.PhotoImage(item3_img)
item3_img_label = Label(image = image3)
item3_img_label.place(x=450,y=30)
# Item 3 name and order entry
item3_name_label = Label(font=('arial', 16, 'bold'),text="BURGER", anchor="w", fg="#003e53", bg="#949999")
item3_name_label.place(x=455, y=135)
item3_name = Entry(font=('arial',16,'bold'), textvariable=burger, bd=3, width=8, insertwidth=4, fg='#003e53', bg="dark grey", justify='center')
item3_name.place(x=450, y=160)

# Item 4 image
item4_img = Image.open("D:/Python Final Assignment/menu_imgs/item4_img.jpg")
item4_img = item4_img.resize((100,100), Image.ANTIALIAS)
image4 = ImageTk.PhotoImage(item4_img)
item4_img_label = Label(image = image4)
item4_img_label.place(x=50,y=210)
# Item 4 name and order entry
item4_name_label = Label(font=('arial', 16, 'bold'),text="FRIED RICE", anchor="w", fg="#003e53", bg="#949999")
item4_name_label.place(x=40, y=315)
item4_name = Entry(font=('arial',16,'bold'), textvariable=fried_rice, bd=3, width=8, insertwidth=4, fg='#003e53', bg="dark grey", justify='center')
item4_name.place(x=50, y=345)

# Item 5 image
item5_img = Image.open("D:/Python Final Assignment/menu_imgs/item5_img.jpg")
item5_img = item5_img.resize((100,100), Image.ANTIALIAS)
image5 = ImageTk.PhotoImage(item5_img)
item5_img_label = Label(image = image5)
item5_img_label.place(x=250,y=210)
# Item 5 name and order entry
item5_name_label = Label(font=('arial', 16, 'bold'),text="SANDWICH", anchor="w", fg="#003e53", bg="#949999")
item5_name_label.place(x=245, y=315)
item5_name = Entry(font=('arial',16,'bold'), textvariable=sandwich, bd=3, width=8, insertwidth=4, fg='#003e53', bg="dark grey", justify='center')
item5_name.place(x=250, y=345)

# Item 6  image
item6_img = Image.open("D:/Python Final Assignment/menu_imgs/item6_img.jpg")
item6_img = item6_img.resize((100,100), Image.ANTIALIAS)
image6 = ImageTk.PhotoImage(item6_img)
item6_img_label = Label(image = image6)
item6_img_label.place(x=450,y=210)
# Item 6 name and order entry
item6_name_label = Label(font=('arial', 16, 'bold'),text="LASSI", anchor="w", fg="#003e53", bg="#949999")
item6_name_label.place(x=470, y=315)
item6_name = Entry(font=('arial',16,'bold'), textvariable=lassi, bd=3, width=8, insertwidth=4, fg='#003e53', bg="dark grey", justify='center')
item6_name.place(x=450, y=345)

# Item 7 image
item7_img = Image.open("D:/Python Final Assignment/menu_imgs/item7_img.jpg")
item7_img = item7_img.resize((100,100), Image.ANTIALIAS)
image7 = ImageTk.PhotoImage(item7_img)
item7_img_label = Label(image = image7)
item7_img_label.place(x=50,y=395)
# Item 7 name and order entry
item7_name_label = Label(font=('arial', 16, 'bold'),text="SALAD", anchor="w", fg="#003e53", bg="#949999")
item7_name_label.place(x=60, y=500)
item7_name = Entry(font=('arial',16,'bold'), textvariable=salad, bd=3, width=8, insertwidth=4, fg='#003e53', bg="dark grey", justify='center')
item7_name.place(x=50, y=530)

# Item 8 image
item8_img = Image.open("D:/Python Final Assignment/menu_imgs/item8_img.jpg")
item8_img = item8_img.resize((100,100), Image.ANTIALIAS)
image8 = ImageTk.PhotoImage(item8_img)
item8_img_label = Label(image = image8)
item8_img_label.place(x=250,y=395)
# Item 8 name and order entry
item8_name_label = Label(font=('arial', 16, 'bold'),text="SPRING ROLLS", anchor="w", fg="#003e53", bg="#949999")
item8_name_label.place(x=225, y=500)
item8_name = Entry(font=('arial',16,'bold'), textvariable=spring_rolls, bd=3, width=8, insertwidth=4, fg='#003e53', bg="dark grey", justify='center')
item8_name.place(x=250, y=530)

# Item 9  image
item9_img = Image.open("D:/Python Final Assignment/menu_imgs/item9_img.jpg")
item9_img = item9_img.resize((100,100), Image.ANTIALIAS)
image9 = ImageTk.PhotoImage(item9_img)
item9_img_label = Label(image = image9)
item9_img_label.place(x=450,y=395)
# Item 9 name and order entry
item9_name_label = Label(font=('arial', 16, 'bold'),text="PANIPURI", anchor="w", fg="#003e53", bg="#949999")
item9_name_label.place(x=450, y=500)
item9_name = Entry(font=('arial',16,'bold'), textvariable=panipuri, bd=3, width=8, insertwidth=4, fg='#003e53', bg="dark grey", justify='center')
item9_name.place(x=450, y=530)

# Item 10  image
item10_img = Image.open("D:/Python Final Assignment/menu_imgs/item10_img.jpg")
item10_img = item10_img.resize((100,100), Image.ANTIALIAS)
image10 = ImageTk.PhotoImage(item10_img)
item10_img_label = Label(image = image10)
item10_img_label.place(x=50,y=580)
# Item 10 name and order entry
item10_name_label = Label(font=('arial', 16, 'bold'),text="SAMOSA", anchor="w", fg="#003e53", bg="#949999")
item10_name_label.place(x=55, y=685)
item10_name = Entry(font=('arial',16,'bold'), textvariable=samosa, bd=3, width=8, insertwidth=4, fg='#003e53', bg="dark grey", justify='center')
item10_name.place(x=50, y=715)

# Item 11  image
item11_img = Image.open("D:/Python Final Assignment/menu_imgs/item11_img.jpg")
item11_img = item11_img.resize((100,100), Image.ANTIALIAS)
image11 = ImageTk.PhotoImage(item11_img)
item11_img_label = Label(image = image11)
item11_img_label.place(x=250,y=580)
# Item 11 name and order entry
item11_name_label = Label(font=('arial', 16, 'bold'),text="CHICKEN WINGS", anchor="w", fg="#003e53", bg="#949999")
item11_name_label.place(x=215, y=685)
item11_name = Entry(font=('arial',16,'bold'), textvariable=chicken_wings, bd=3, width=8, insertwidth=4, fg='#003e53', bg="dark grey", justify='center')
item11_name.place(x=250, y=715)

# Item 12  image
item12_img = Image.open("D:/Python Final Assignment/menu_imgs/item12_img.jpg")
item12_img = item12_img.resize((100,100), Image.ANTIALIAS)
image12 = ImageTk.PhotoImage(item12_img)
item12_img_label = Label(image = image12)
item12_img_label.place(x=450,y=580)
# Item 12 name and order entry
item12_name_label = Label(font=('arial', 16, 'bold'),text="NOODLES", anchor="w", fg="#003e53", bg="#949999")
item12_name_label.place(x=450, y=685)
item12_name = Entry(font=('arial',16,'bold'), textvariable=noodles, bd=3, width=8, insertwidth=4, fg='#003e53', bg="dark grey", justify='center')
item12_name.place(x=450, y=715)


# Billing Items
# Showing Bill, calculations


# Mini Restaurant Calculator
# Display window
e = Entry( width=28, bd=10, borderwidth=6, insertwidth=10, fg="black", bg="#c3c4c0", font=("Times New Roman", 20, "bold"), justify=CENTER)
e.place(x=610, y=20, height=50)

# Defining the functions
# creating button functions
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)


def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    e.delete(0, END)


def btn_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, f_num + float(second_number))
    if math == "subtraction":
        e.insert(0, f_num - float(second_number))
    if math == "multiplication":
        e.insert(0, f_num * float(second_number))
    if math == "division":
        e.insert(0, f_num / float(second_number))


def button_sub():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    e.delete(0, END)


def button_mul():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    e.delete(0, END)


def button_div():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    e.delete(0, END)

# Defining the buttons

button_1 = Button(text="1", width=4, borderwidth=3, fg="dark grey", bg="grey",
                  font=("Bariol", 30, "bold"), cursor="hand2", command=lambda: button_click(1))
button_2 = Button(text="2", width=3, borderwidth=3, fg="dark grey", bg="grey",
                  font=("Bariol", 30, "bold"), cursor="hand2", command=lambda: button_click(2))
button_3 = Button(text="3", width=4, borderwidth=3, fg="dark grey", bg="grey",
                  font=("Bariol", 30, "bold"), cursor="hand2", command=lambda: button_click(3))


button_4 = Button(text="4", width=4, borderwidth=3, fg="dark grey", bg="grey",
                  font=("Bariol", 30, "bold"), cursor="hand2", command=lambda: button_click(4))
button_5 = Button(text="5", width=3, borderwidth=3, fg="dark grey", bg="grey",
                  font=("Bariol", 30, "bold"), cursor="hand2", command=lambda: button_click(5))
button_6 = Button(text="6", width=4, borderwidth=3, fg="dark grey", bg="grey",
                  font=("Bariol", 30, "bold"), cursor="hand2", command=lambda: button_click(6))


button_7 = Button(text="7", width=4, borderwidth=3, fg="dark grey", bg="grey",
                  font=("Bariol", 30, "bold"), cursor="hand2", command=lambda: button_click(7))
button_8 = Button(text="8", width=3, borderwidth=3, fg="dark grey", bg="grey",
                  font=("Bariol", 30, "bold"), cursor="hand2", command=lambda: button_click(8))
button_9 = Button(text="9", width=4, borderwidth=3, fg="dark grey", bg="grey",
                  font=("Bariol", 30, "bold"), cursor="hand2", command=lambda: button_click(9))


button_0 = Button(text="0", width=3, borderwidth=3, fg="dark grey", bg="grey",
                  font=("Bariol", 30, "bold"), cursor="hand2", command=lambda: button_click(0))


button_add = Button(text="+", width=4, borderwidth=3, fg="dark grey", bg="grey",
                    font=("Bariol", 30, "bold"), cursor="hand2", command=button_add)
button_sub = Button(text="-", width=4, borderwidth=3, fg="dark grey", bg="grey",
                    font=("Bariol", 30, "bold"), cursor="hand2", command=button_sub)
button_mul = Button(text="*", width=4, borderwidth=3, fg="dark grey", bg="grey",
                    font=("Bariol", 30, "bold"), cursor="hand2", command=button_mul)
button_div = Button(text="/", width=4, borderwidth=3, fg="dark grey", bg="grey",
                    font=("Bariol", 30, "bold"), cursor="hand2", command=button_div)
button_clear = Button(text="Clear", width=4, borderwidth=3, fg="dark grey", bg="grey",
                      font=("Bariol", 30, "bold"), cursor="hand2", command=button_clear)

button_point = Button(text=".", width=4, borderwidth=3, fg="dark grey", bg="grey",
                      font=("Bariol", 30, "bold"), cursor="hand2", command=lambda: button_click("."))

# Making function for hover effect
def on_equal_enter(e):
    button_equal.config(background='#949999', foreground="white")

def on_equal_leave(e):
    button_equal.config(background='grey', foreground='dark grey')

button_equal = Button(text="=", width=16, borderwidth=9, fg="dark grey", bg="grey", activeforeground="white", activebackground="black",
                      font=("Bariol", 30, "bold"), cursor="hand2", command=btn_equal)

# Making the hovering effect active
button_equal.bind('<Enter>', on_equal_enter)
button_equal.bind('<Leave>', on_equal_leave)


# Putting buttons on the screen
button_7.place(x=610, y=70)
button_8.place(x=718, y=70)
button_9.place(x=802, y=70)

button_4.place(x=610, y=152)
button_5.place(x=718, y=152)
button_6.place(x=802, y=152)

button_1.place(x=610, y=233)
button_2.place(x=718, y=233)
button_3.place(x=802, y=233)

button_0.place(x=718, y=315)

button_add.place(x=910, y=70)
button_sub.place(x=910, y=152)
button_mul.place(x=910, y=233)
button_div.place(x=910, y=315)
button_equal.place(x=610, y=398 , height=60)
button_clear.place(x=610, y=315)
button_point.place(x=802, y=315)


# Making Buttons for Total cost, food cost, service charge


user_food_cost_label = Label(font=('arial', 20, 'bold'),text="FOOD COST", width=23, bg="#49f2f5").place(x=610, y=520)

user_food_cost_total = Entry(font=('arial', 16, 'bold'), textvariable=food_cost, bd=10, width=32, insertwidth=4,
                 bg='orange', justify='right')
user_food_cost_total.place(x=605, y=555)


service_charge_label = Label(font=('arial', 20, 'bold'),text="SERVICE CHARGE", width=23, bg="#49f2f5").place(x=610, y=600)
service_charge_ = Entry(font=('arial', 16, 'bold'), textvariable=service_charge, bd=10, width=32, insertwidth=4,
                 bg='orange', justify='right')
service_charge_.place(x=605, y=635)



total_cost_label = Label(font=('arial', 20, 'bold'),text="TOTAL COST", width=15, bg="#49f2f5").place(x=610, y=680)
txtTotal = Entry(font=('arial', 16, 'bold'), textvariable=total, bd=10, width=32, insertwidth=4,
                 bg='orange', justify='right')
txtTotal.place(x=605, y=715)

# Making function for hover effect
def on_total_enter(t):
    btnTotal.config(background='#949999', foreground="white")

def on_total_leave(t):
    btnTotal.config(background='grey', foreground='dark grey')

def on_reset_enter(r):
    reset_button.config(background='#949999', foreground="white")

def on_reset_leave(r):
    reset_button.config(background='grey', foreground='dark grey')

def on_quit_enter(q):
    quit_button.config(background='#949999', foreground="white")

def on_quit_leave(q):
    quit_button.config(background='powder blue', foreground='black')





quit_button = Button(font=('arial', 13, 'bold'), width=13, bd=1, activeforeground="white", activebackground="black",
                  text='QUIT', fg='black', bg='powder blue', command=quit_app)
quit_button.place(x=873, y=683)


btnTotal = Button(padx=16, bd=10, font=('arial', 16, 'bold'), width=11, activeforeground="white", activebackground="black",
                  text='TOTAL', fg='dark grey', bg='grey', command=lambda: ref())
btnTotal.place(x=610, y=460)

reset_button = Button(padx=16, bd=10, font=('arial', 16, 'bold'), width=11, activeforeground="white", activebackground="black",
                  text='RESET', fg='dark grey', bg='grey', command=lambda: reset_values())
reset_button.place(x=812, y=460)

# Making the hovering effect active
btnTotal.bind('<Enter>', on_total_enter)
btnTotal.bind('<Leave>', on_total_leave)

reset_button.bind('<Enter>', on_reset_enter)
reset_button.bind('<Leave>', on_reset_leave)

quit_button.bind('<Enter>', on_quit_enter)
quit_button.bind('<Leave>', on_quit_leave)



log.mainloop()