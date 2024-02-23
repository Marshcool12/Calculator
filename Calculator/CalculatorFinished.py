import tkinter as tk
window = tk.Tk()
window.title('CALCULATOR')

#image_path = os.path.join('Calculator', 'images', 'calculatorlogo.ico')
window.iconbitmap('images/calculatorlogo.ico')

#user entry
getnum = tk.Entry(width=40, borderwidth=5)
getnum.grid(row=0, column=0, columnspan=3)

#validation at the user end
if getnum == str():
    getnum.insert(0, "Invalid!")

#def functions
#===============================================================================================================#
def add():
    global f_num
    global math
    math = ('add')
    f_num = float(getnum.get())
    getnum.delete(0, tk.END)
#===============================================================================================================#
def sub():
    global f_num
    global math
    math = ('sub')
    f_num = float(getnum.get())
    getnum.delete(0, tk.END)
#===============================================================================================================#
def mult():
    global f_num
    global math
    math = ('mult')
    f_num = float(getnum.get())
    getnum.delete(0, tk.END)
#===============================================================================================================#
def div():
    global f_num
    global math
    math = ('div')
    f_num = float(getnum.get())
    getnum.delete(0, tk.END)
#===============================================================================================================#
def square():
    global f_num
    global math
    math = ('square')
    f_num = float(getnum.get())
    getnum.delete(0, tk.END)
#===============================================================================================================#
def root():
    global f_num
    global math
    math = ('root')
    f_num = float(getnum.get())
    getnum.delete(0, tk.END)
#===============================================================================================================#
def equal():
    try:
        s_num = float(getnum.get())
        getnum.delete(0, tk.END)
        if math == 'add':
            getnum.insert(0, f_num + s_num)
        elif math == 'sub':
            getnum.insert(0, f_num - s_num)
        elif math == 'div':
            getnum.insert(0, f_num / s_num)
        elif math == 'mult':
            getnum.insert(0, f_num * s_num)
        elif math == 'square':
            getnum.insert(0, f_num ** s_num)
        elif math == 'root':
            getnum.insert(0, f_num ** (1 / s_num))
    except:
        getnum.delete(0, tk.END) 
        getnum.insert(0, "Invalid!")
#===============================================================================================================#
def clear():
    getnum.delete(0,tk.END)
#===============================================================================================================#
def click(number):
    currentnum = getnum.get()
    getnum.delete(0,tk.END)
    getnum.insert(0, str(currentnum) + str(number))
#===============================================================================================================#
    
#button aesthetics
color_backround = 'light grey'
color_foreground = 'black'
letter_font = ("Helvetica", 12, "bold")
    
#buttons to show the nums on calc

btn_1 = tk.Button(text=('1'), padx=39, pady=10, fg=color_foreground, bg=color_backround, font=letter_font, command=lambda: click(1))
btn_2 = tk.Button(text=('2'), padx=39, pady=10, fg=color_foreground, bg=color_backround, font=letter_font, command=lambda: click(2))
btn_3 = tk.Button(text=('3'), padx=39, pady=10, fg=color_foreground, bg=color_backround, font=letter_font, command=lambda: click(3))
btn_4 = tk.Button(text=('4'), padx=39, pady=10, fg=color_foreground, bg=color_backround, font=letter_font, command=lambda: click(4))
btn_5 = tk.Button(text=('5'), padx=39, pady=10, fg=color_foreground, bg=color_backround, font=letter_font, command=lambda: click(5))
btn_6 = tk.Button(text=('6'), padx=39, pady=10, fg=color_foreground, bg=color_backround, font=letter_font, command=lambda: click(6))
btn_7 = tk.Button(text=('7'), padx=39, pady=10, fg=color_foreground, bg=color_backround, font=letter_font, command=lambda: click(7))
btn_8 = tk.Button(text=('8'), padx=39, pady=10, fg=color_foreground, bg=color_backround, font=letter_font, command=lambda: click(8))
btn_9 = tk.Button(text=('9'), padx=39, pady=10, fg=color_foreground, bg=color_backround, font=letter_font, command=lambda: click(9))
btn_0 = tk.Button(text=('0'), padx=39, pady=10, fg=color_foreground, bg=color_backround, font=letter_font, command=lambda: click(0))

#func buttons
btn_add = tk.Button(text=('+'), fg=color_foreground, bg=color_backround, font=letter_font, padx=38, pady=10, command=add)
btn_sub = tk.Button(text=('-'), fg=color_foreground, bg=color_backround, font=letter_font, padx=39, pady=10, command=sub)
btn_mult = tk.Button(text=('*'), fg=color_foreground, bg=color_backround, font=letter_font, padx=41, pady=10, command=mult)
btn_div = tk.Button(text=('/'), fg=color_foreground, bg=color_backround, font=letter_font, padx=42, pady=10, command=div)
btn_square = tk.Button(text=('^'), fg=color_foreground, bg=color_backround, font=letter_font, padx=39, pady=10, command=square)
btn_root = tk.Button(text=('√'), fg=color_foreground, bg=color_backround, font=letter_font, padx=39, pady=10, command=root)
btn_equal = tk.Button(text=('='), fg=color_foreground, bg=color_backround, font=letter_font, padx=39, pady=10, command=equal)
btn_clear = tk.Button(text=('Clear'), fg=color_foreground, bg=color_backround, font=letter_font, padx=24, pady=10, command=clear)

#button positions
btn_1.grid(row=1, column=0)
btn_2.grid(row=1, column=1)
btn_3.grid(row=1, column=2)

btn_4.grid(row=2, column=0)
btn_5.grid(row=2, column=1)
btn_6.grid(row=2, column=2)

btn_7.grid(row=3, column=0)
btn_8.grid(row=3, column=1)
btn_9.grid(row=3, column=2)

btn_0.grid(row=4, column=0)
btn_clear.grid(row=4, column=1)
btn_root.grid(row=4, column=2)

btn_add.grid(row=5, column=0)
btn_equal.grid(row=5, column=1)
btn_square.grid(row=5, column=2)

btn_sub.grid(row=6, column=0)
btn_div.grid(row=6, column=1)
btn_mult.grid(row=6, column=2)

window.mainloop()