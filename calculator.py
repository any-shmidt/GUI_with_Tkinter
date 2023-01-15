from tkinter import *
from tkinter import ttk
import math


def click_button(event):
    count = 0
    digit = event.widget.cget('text')
    value = calc.get()
    
    for i in '+-*/%':
        if i in value:
            count += 1
        
    if count == 0:
        if len(value) == 1 and value == '0' and digit == '0':
            value = value[:-1]
        if len(value) == 1 and value == '0' and digit != '.':
            value = ''
    elif count == 1:
        if value[-1] == '0' and digit != '.' and value[-2] in '+-*/%':
            value = value[:-1]
        
    calc.delete(0, END)
    calc.insert(0, value + digit)


def get_operation(event):
    operation = event.widget.cget('text')
    value = calc.get()
    
    if operation == '+' or operation == '-' or operation == '*' or operation == '/' or operation == '%':
        if len(value) > 0 and value[-1] in '+-*/%.':
            value = value[:-1]
        
            
    elif operation == '.':
        float_button()
           
    elif operation == '+/-':
        plus_minus()
    elif '+' in value or '-' in value or '*' in value or '/' in value or '%' in value:
        calculate()
        value = calc.get()      
        
    if operation == '+' or operation == '-' or operation == '*' or operation == '/' or operation == '%':
        calc.delete(0, END)
        calc.insert(0, value + operation)
    elif operation == '+/-':
        calc.delete(0, END)
        calc.insert(0, value)


def calculate():
    value = calc.get()

    if '+' in value or '-' in value or '*' in value or '/' in value:
        calc.delete(0, END)
        if value[-1] in '+-*/':
            value = value + value[:-1]

        try:
            if value[0] == '+' or value[0] == '-' or value[0] == '*' or value[0] == '/':
                value = '0' + value
            result = eval(value)
             
            if (result * 10) % 10 == 0:
                result = int(result)
            elif (result * 10) % 10 != 0:
                result = round(result, 2)
        except ZeroDivisionError:
            result = ''
            messagebox.showwarning('Warning', 'На 0 делить нельзя!')
        calc.insert(0, result)
    elif '%' in value:
        percent()
        

def percent():
    value = calc.get()
    calc.delete(0, END)
    value_list = value.split('%')
    if value_list[0] == '':
        value_list[0] = '0'

    if value_list[-1] == '':
        value_list[-1] = '1'

    percent_result = ((float(value_list[0])) /100) * float(value_list[-1])
    if (percent_result * 10) % 10 == 0:
        percent_result = int(percent_result)
    elif (percent_result * 10) % 10 != 0:
        percent_result = float(round(percent_result, 2))
    calc.insert(0, str(percent_result))

        
def plus_minus():
    value = calc.get()
    if len(value) == 0:
        value = '-'
    elif value[0] != '-': 
        value = '-' + value
    elif value[0] == '-':
        value = value[1:]
    calc.delete(0, END)
    calc.insert(0, value)

    
def float_button():
    value = calc.get()
    count = value.count('.')
    
    try:
        if count == 0 and ('+' not in value or '-'  not in value or '*' not in value \
                           or '/'  not in value or '%' not in value):
        
            if value[-1] != '.':
                value = value + '.'
            elif value[-1] == '.':
                value = value[:-1]
        
        elif count == 1 and ('+' in value or '-' in value or '*' in value or '/' in value or '%' in value):
            if value[-1] != '.':
                value = value + '.'
                
        if value[-2] in '+-*/%' and value[-1] == '.':
            value = value[:-1]
            value = value + '0.'
        
    except IndexError:
        if len(value) == 0:
            value = '0.'
            calc.insert(0, value)
            
    calc.delete(0, END)
    calc.insert(0, value)


def sqrt_value():
    value = calc.get()
    calc.delete(0, END)
    if len(value) == 0 or value[-1] in '+-*/.%':
        value = '0'
    if value[-1] not in '0123456789':
        value = value[:-1]
    value = float(value)
    value = math.sqrt(value)
    if (value * 10) % 10 == 0:
        value = int(value)
    elif (value * 10) % 10 != 0:
        value = round(value, 2)
    value = str(value)
    calc.insert(0, value)


def delete_digit():
    value = calc.get()
    value = value[:-1]
    calc.delete(0, END)
    calc.insert(0, value)

   
def clear_entry():
    calc.delete(0, END)

root = Tk()
root.title('Calculator')
root.resizable(width=False, height=False)

style = ttk.Style()
style.theme_use('clam')
style.configure('TFrame', background='black')
style.configure("Orange.TButton", background="orange", foreground="black")
style.configure("Green.TButton", background="green", foreground="black")

frame = ttk.Frame(root)
frame['padding'] = 10
frame.grid()

calc = ttk.Entry(frame, justify=RIGHT, font=('Calibri', 15, 'bold'))
calc.grid(row=0, column=0, columnspan=4, sticky='nwse', padx=(0, 0), pady =(0, 10))

button_c = ttk.Button(frame, text='C', style='Orange.TButton', command=clear_entry)
button_c.grid(row=1, column=3)

button_delete = ttk.Button(frame, text='del', command=delete_digit)
button_delete.grid(row=2, column=0)

button_sqrt = ttk.Button(frame, text='sqrt', command=sqrt_value)
button_sqrt.grid(row=2, column=1)

button_percent = ttk.Button(frame, text='%')
button_percent.grid(row=2, column=2)
button_percent.bind('<Button-1>', get_operation)

button_divide = ttk.Button(frame, text='/')
button_divide.grid(row=2, column=3)
button_divide.bind('<Button-1>', get_operation)

button7 = ttk.Button(frame, text='7')
button7.grid(row=3, column=0)
button7.bind('<Button-1>', click_button)

button8 = ttk.Button(frame, text='8')
button8.grid(row=3, column=1)
button8.bind('<Button-1>', click_button)

button9 = ttk.Button(frame, text='9')
button9.grid(row=3, column=2)
button9.bind('<Button-1>', click_button)

button_multiply = ttk.Button(frame, text='*')
button_multiply.grid(row=3, column=3)
button_multiply.bind('<Button-1>', get_operation)

button4 = ttk.Button(frame, text='4')
button4.grid(row=4, column=0)
button4.bind('<Button-1>', click_button)

button5 = ttk.Button(frame, text='5')
button5.grid(row=4, column=1)
button5.bind('<Button-1>', click_button)

button6 = ttk.Button(frame, text='6')
button6.grid(row=4, column=2)
button6.bind('<Button-1>', click_button)

button_subtract = ttk.Button(frame, text='-')
button_subtract.grid(row=4, column=3)
button_subtract.bind('<Button-1>', get_operation)

button1 = ttk.Button(frame, text='1')
button1.grid(row=5, column=0)
button1.bind('<Button-1>', click_button)

button2 = ttk.Button(frame, text='2')
button2.grid(row=5, column=1)
button2.bind('<Button-1>', click_button)

button3 = ttk.Button(frame, text='3')
button3.grid(row=5, column=2)
button3.bind('<Button-1>', click_button)

button_add = ttk.Button(frame, text='+')
button_add.grid(row=5, column=3)
button_add.bind('<Button-1>', get_operation)

button_plus_minus = ttk.Button(frame, text='+/-', command=plus_minus)
button_plus_minus.grid(row=6, column=0)

button0 = ttk.Button(frame, text='0')
button0.grid(row=6, column=1)
button0.bind('<Button-1>', click_button)

button_float = ttk.Button(frame, text='.')
button_float.grid(row=6, column=2)
button_float.bind('<Button-1>', get_operation)

button_result = ttk.Button(frame, text='=', style='Green.TButton', command=calculate)
button_result.grid(row=6, column=3)

calc.bind('<Key>', lambda e: 'break')


root.mainloop()
