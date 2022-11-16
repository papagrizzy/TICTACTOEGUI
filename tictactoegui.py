from tkinter import *
import tkinter.messagebox

tictactoe = Tk()

tictactoe.geometry("690x690")
tictactoe.maxsize(690, 690)
tictactoe.minsize(690, 690)
tictactoe.config(background="black")
tictactoe.title("Tic-Tac-Toe ~ Pritish")

ph1 = PhotoImage(file="/home/kraken/Desktop/pyrate/Assets/Untitled.png")
cross1 = (
    cross2
) = cross3 = cross4 = cross5 = cross6 = cross7 = cross8 = cross9 = PhotoImage(
    file="/home/kraken/Desktop/pyrate/Assets/cross.png"
)
circle1 = (
    circle2
) = circle3 = circle4 = circle5 = circle6 = circle7 = circle8 = circle9 = PhotoImage(
    file="/home/kraken/Desktop/pyrate/Assets/circle.png"
)

bool_cross_check1 = True
bool_cross_check2 = True
bool_cross_check3 = True
bool_cross_check4 = True
bool_cross_check5 = True
bool_cross_check6 = True
bool_cross_check7 = True
bool_cross_check8 = True
bool_cross_check9 = True


fin1 = "1"
fin2 = "2"
fin3 = "3"
fin4 = "4"
fin5 = "5"
fin6 = "6"
fin7 = "7"
fin8 = "8"
fin9 = "9"


click_count = 0
increment = True


def reset():
    global click_count
    global bool_cross_check1
    global bool_cross_check2
    global bool_cross_check3
    global bool_cross_check4
    global bool_cross_check5
    global bool_cross_check6
    global bool_cross_check7
    global bool_cross_check8
    global bool_cross_check9
    global fin1
    global fin2
    global fin3
    global fin4
    global fin5
    global fin6
    global fin7
    global fin8
    global fin9
    if game_stat():
        click_count = 0
        button1.config(image=ph1)
        button2.config(image=ph1)
        button3.config(image=ph1)
        button4.config(image=ph1)
        button5.config(image=ph1)
        button6.config(image=ph1)
        button7.config(image=ph1)
        button8.config(image=ph1)
        button9.config(image=ph1)
        bool_cross_check1 = True
        bool_cross_check2 = True
        bool_cross_check3 = True
        bool_cross_check4 = True
        bool_cross_check5 = True
        bool_cross_check6 = True
        bool_cross_check7 = True
        bool_cross_check8 = True
        bool_cross_check9 = True
        fin1 = "1"
        fin2 = "2"
        fin3 = "3"
        fin4 = "4"
        fin5 = "5"
        fin6 = "6"
        fin7 = "7"
        fin8 = "8"
        fin9 = "9"
        tkinter.messagebox.showinfo(
            "Message", "The screen has been reset. You can play again."
        )


def game_stat():
    if fin1 == fin5 and fin5 == fin9:
        tkinter.messagebox.showinfo("Result", f"{fin1.upper()} Wins!")
        return True
    elif fin1 == fin4 == fin7:
        tkinter.messagebox.showinfo("Result", f"{fin1.upper()} Wins!")
        return True
    elif fin1 == fin2 == fin3:
        tkinter.messagebox.showinfo("Result", f"{fin1.upper()} Wins!")
        return True
    elif fin2 == fin5 == fin8:
        tkinter.messagebox.showinfo("Result", f"{fin2.upper()} Wins!")
        return True
    elif fin3 == fin6 == fin9:
        tkinter.messagebox.showinfo("Result", f"{fin3.upper()} Wins!")
        return True
    elif fin3 == fin5 == fin7:
        tkinter.messagebox.showinfo("Result", f"{fin3.upper()} Wins!")
        return True
    elif fin4 == fin5 == fin6:
        tkinter.messagebox.showinfo("Result", f"{fin4.upper()} Wins!")
        return True
    elif fin7 == fin8 == fin9:
        tkinter.messagebox.showinfo("Result", f"{fin7.upper()} Wins!")
        return True
    elif (
        fin1.isalpha()
        and fin2.isalpha()
        and fin3.isalpha()
        and fin4.isalpha()
        and fin5.isalpha()
        and fin6.isalpha()
        and fin7.isalpha()
        and fin8.isalpha()
        and fin9.isalpha()
    ):
        tkinter.messagebox.showinfo("Result", "Draw!")
        return True


# CLICK FUNCTION#
def clicked():
    global click_count
    global increment
    if increment:
        click_count += 1
    else:
        increment = True


# <----Cross Functions---->

# 1
def place_cross1():
    global fin1
    global increment
    global bool_cross_check1
    if bool_cross_check1 and click_count % 2 == 0:
        fin1 = "cross"
        button1.config(image=cross1)
        bool_cross_check1 = False
    elif bool_cross_check1 and click_count % 2 == 1:
        fin1 = "circle"
        button1.config(image=circle1)
        bool_cross_check1 = False
    else:
        increment = False
        tkinter.messagebox.showerror("Message", "Already occupied!")


# 2
def place_cross2():
    global fin2
    global increment
    global bool_cross_check2
    if bool_cross_check2 and click_count % 2 == 0:
        fin2 = "cross"
        button2.config(image=cross1)
        bool_cross_check2 = False
    elif bool_cross_check2 and click_count % 2 == 1:
        fin2 = "circle"
        button2.config(image=circle2)
        bool_cross_check2 = False
    else:
        increment = False
        tkinter.messagebox.showerror("Message", "Already occupied!")


# 3
def place_cross3():
    global fin3
    global increment
    global bool_cross_check3
    if bool_cross_check3 and click_count % 2 == 0:
        fin3 = "cross"
        button3.config(image=cross3)
        bool_cross_check3 = False
    elif bool_cross_check3 and click_count % 2 == 1:
        fin3 = "circle"
        button3.config(image=circle3)
        bool_cross_check3 = False
    else:
        increment = False
        tkinter.messagebox.showerror("Message", "Already occupied!")


# 4
def place_cross4():
    global fin4
    global increment
    global bool_cross_check4
    if bool_cross_check4 and click_count % 2 == 0:
        fin4 = "cross"
        button4.config(image=cross4)
        bool_cross_check4 = False
    elif bool_cross_check4 and click_count % 2 == 1:
        fin4 = "circle"
        button4.config(image=circle4)
        bool_cross_check4 = False
    else:
        increment = False
        tkinter.messagebox.showerror("Message", "Already occupied!")


# 5
def place_cross5():
    global fin5
    global increment
    global bool_cross_check5
    if bool_cross_check5 and click_count % 2 == 0:
        fin5 = "cross"
        button5.config(image=cross5)
        bool_cross_check5 = False
    elif bool_cross_check5 and click_count % 2 == 1:
        fin5 = "circle"
        button5.config(image=circle5)
        bool_cross_check5 = False
    else:
        increment = False
        tkinter.messagebox.showerror("Message", "Already occupied!")


# 6
def place_cross6():
    global fin6
    global increment
    global bool_cross_check6
    if bool_cross_check6 and click_count % 2 == 0:
        fin6 = "cross"
        button6.config(image=cross6)
        bool_cross_check6 = False
    elif bool_cross_check6 and click_count % 2 == 1:
        fin6 = "circle"
        button6.config(image=circle6)
        bool_cross_check6 = False
    else:
        increment = False
        tkinter.messagebox.showerror("Message", "Already occupied!")


# 7
def place_cross7():
    global fin7
    global increment
    global bool_cross_check7
    if bool_cross_check7 and click_count % 2 == 0:
        fin7 = "cross"
        button7.config(image=cross7)
        bool_cross_check7 = False
    elif bool_cross_check7 and click_count % 2 == 1:
        fin7 = "circle"
        button7.config(image=circle7)
        bool_cross_check7 = False
    else:
        increment = False
        tkinter.messagebox.showerror("Message", "Already occupied!")


# 8
def place_cross8():
    global fin8
    global increment
    global bool_cross_check8
    if bool_cross_check8 and click_count % 2 == 0:
        fin8 = "cross"
        button8.config(image=cross8)
        bool_cross_check8 = False
    elif bool_cross_check8 and click_count % 2 == 1:
        fin8 = "circle"
        button8.config(image=circle8)
        bool_cross_check8 = False
    else:
        increment = False
        tkinter.messagebox.showerror("Message", "Already occupied!")


# 9
def place_cross9():
    global fin9
    global increment
    global bool_cross_check9
    if bool_cross_check9 and click_count % 2 == 0:
        fin9 = "cross"
        button9.config(image=cross9)
        bool_cross_check9 = False
    elif bool_cross_check9 and click_count % 2 == 1:
        fin9 = "circle"
        button9.config(image=circle9)
        bool_cross_check9 = False
    else:
        increment = False
        tkinter.messagebox.showerror("Message", "Already occupied!")


# <----Cross Buttons---->

# 1
button1 = Button(
    tictactoe, image=ph1, bd=15, command=lambda: [place_cross1(), clicked(), reset()]
)
button1.place(x=0, y=0)
# 2
button2 = Button(
    tictactoe, image=ph1, bd=15, command=lambda: [place_cross2(), clicked(), reset()]
)
button2.place(x=230, y=0)
# 3
button3 = Button(
    tictactoe, image=ph1, bd=15, command=lambda: [place_cross3(), clicked(), reset()]
)
button3.place(x=460, y=0)
# 4
button4 = Button(
    tictactoe, image=ph1, bd=15, command=lambda: [place_cross4(), clicked(), reset()]
)
button4.place(x=0, y=230)
# 5
button5 = Button(
    tictactoe, image=ph1, bd=15, command=lambda: [place_cross5(), clicked(), reset()]
)
button5.place(x=230, y=230)
# 6
button6 = Button(
    tictactoe, image=ph1, bd=15, command=lambda: [place_cross6(), clicked(), reset()]
)
button6.place(x=460, y=230)
# 7
button7 = Button(
    tictactoe, image=ph1, bd=15, command=lambda: [place_cross7(), clicked(), reset()]
)
button7.place(x=0, y=460)
# 8
button8 = Button(
    tictactoe, image=ph1, bd=15, command=lambda: [place_cross8(), clicked(), reset()]
)
button8.place(x=230, y=460)
# 9
button9 = Button(
    tictactoe, image=ph1, bd=15, command=lambda: [place_cross9(), clicked(), reset()]
)
button9.place(x=460, y=460)


tictactoe.mainloop()
