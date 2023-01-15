from tkinter import *
import random

count = 0 # количество неправильных попыток
correct_list = []
incorrect_list = []


words_dict = {'Фрукт': 'банан яблоко'.split(),
              'Техника': 'компьютер холодильник'.split(),
              'Музыкальный инструмент': 'гитара пианино скрипка аккордеон'.split(),
              'Транспорт': 'трамвай автобус поезд метро автомобиль самолёт'.split(),
              'Наука': 'психология астрономия биология физика'.split(),
              'Цвет': 'чёрный красный голубой серый розовый зелёный'.split(),
              'Фигура': 'квадрат круг треугольник прямоугольник'.split(),
              'Страна': 'германия англия россия'.split()}

word_key = random.choice(list((words_dict).keys()))
print(word_key)

secret_word = random.choice(list(words_dict[word_key]))
print(secret_word)


blanks = []
for letter in secret_word:
    blanks += '_'
print(blanks)


def restart():
    pass


def click_button(event):
    global count
    global word
    global blanks
    text = event.widget.cget('text').lower()
    print(text)

    for position in range(len(secret_word)):
        letter = secret_word[position]
        if letter == text:
            blanks[position] = letter
    print(blanks)
    word.set(' '.join(blanks).upper())
    
    event.widget.config(state='disabled')

    if blanks.count('_') == 0 and count != 7:
        for button in buttons:
            button.config(state='disabled')
            
        win_label = Label(root, text='YOU WIN!', bg='green', fg='yellow', font=40)
        win_label.grid(row=1, column=0)
    
    if text not in secret_word and blanks.count('_') != 0:
        count += 1
        if count == 1:
            c.create_line(50, 50, 50, 350, width=5)
            c.create_line(40, 100, 150, 50, width=5) 
            c.create_line(40, 350, 200, 350, width=5) 
            c.create_line(40, 50, 200, 50, width=5)
            c.create_line(150, 50, 150, 100, width=5) 
        elif count == 2:
            c.create_line(50, 50, 50, 350, width=5) 
            c.create_line(40, 100, 150, 50, width=5) 
            c.create_line(40, 350, 200, 350, width=5) 
            c.create_line(40, 50, 200, 50, width=5)
            c.create_line(150, 50, 150, 100, width=5) 
            c.create_oval(125, 100, 175, 150, width=5, fill='yellow')
        elif count == 3:
            c.create_line(50, 50, 50, 350, width=5) 
            c.create_line(40, 100, 150, 50, width=5) 
            c.create_line(40, 350, 200, 350, width=5) 
            c.create_line(40, 50, 200, 50, width=5) 
            c.create_line(150, 50, 150, 100, width=5) 
            c.create_oval(125, 100, 175, 150, width=5, fill='yellow')
            c.create_line(150, 150, 150, 250, width=5) 
        elif count == 4:
            c.create_line(50, 50, 50, 350, width=5) 
            c.create_line(40, 100, 150, 50, width=5) 
            c.create_line(40, 350, 200, 350, width=5) 
            c.create_line(40, 50, 200, 50, width=5) 
            c.create_line(150, 50, 150, 100, width=5) 
            c.create_oval(125, 100, 175, 150, width=5, fill='yellow')
            c.create_line(150, 150, 150, 250, width=5) 
            c.create_line(150, 160, 200, 210, width=5) 
        elif count == 5:
            c.create_line(50, 50, 50, 350, width=5) 
            c.create_line(40, 100, 150, 50, width=5) 
            c.create_line(40, 350, 200, 350, width=5) 
            c.create_line(40, 50, 200, 50, width=5)
            c.create_line(150, 50, 150, 100, width=5)
            c.create_oval(125, 100, 175, 150, width=5, fill='yellow')
            c.create_line(150, 150, 150, 250, width=5)
            c.create_line(150, 160, 200, 210, width=5)
            c.create_line(100, 210, 150, 160, width=5)
        elif count == 6:
            c.create_line(50, 50, 50, 350, width=5)
            c.create_line(40, 100, 150, 50, width=5) 
            c.create_line(40, 350, 200, 350, width=5)
            c.create_line(40, 50, 200, 50, width=5) 
            c.create_line(150, 50, 150, 100, width=5) 
            c.create_oval(125, 100, 175, 150, width=5, fill='yellow')
            c.create_line(150, 150, 150, 250, width=5) 
            c.create_line(150, 160, 200, 210, width=5)
            c.create_line(100, 210, 150, 160, width=5)
            c.create_line(150, 250, 200, 300, width=5) 
        elif count == 7:
            c.create_line(50, 50, 50, 350, width=5) # вертикаль
            c.create_line(40, 100, 150, 50, width=5) # диагональ
            c.create_line(40, 350, 200, 350, width=5) # нижняя горизонталь
            c.create_line(40, 50, 200, 50, width=5) # верхняя горизонталь
            c.create_line(150, 50, 150, 100, width=5) # виселица
            c.create_oval(125, 100, 175, 150, width=5, fill='yellow')
            c.create_line(150, 150, 150, 250, width=5) # тело
            c.create_line(150, 160, 200, 210, width=5) # левая рука
            c.create_line(100, 210, 150, 160, width=5) # правая рука
            c.create_line(150, 250, 200, 300, width=5) # левая нога
            c.create_line(150, 250, 100, 300, width=5) # правая нога нога
            
            game_over_label = Label(root, text='GAME OVER!', bg='red', fg='yellow', font=40)
            game_over_label.grid(row=1, column=0)
                      
            count = count
            for button in buttons:
                button.config(state='disabled')
            
            blanks = list(secret_word)
            word.set(' '.join(blanks).upper())
                
    return word


root = Tk()
root.geometry('700x600')
root.title('HANGMAN')
root['bg'] = 'silver'
root.resizable(width=False, height=False)

c = Canvas(root, width=300, height=350)
c.create_line(50, 50, 50, 350, width=5)
c.create_line(40, 100, 150, 50, width=5) 
c.create_line(40, 350, 200, 350, width=5) 
c.create_line(40, 50, 200, 50, width=5)

c.grid(row=1, column=0)

# restart_button = Button(root, text='Restart', height=2, width=10, command=restart, relief=RAISED)
# restart_button.grid(row=0, column=1)

hint_label = Label(root, text=word_key, font=('Arial', 16), bg='silver', width=25)
hint_label.grid(row=1, column=1) # подсказка, к какой категории относится слово

label = Label(root, text='ВИСЕЛИЦА', font='Verdana 20 bold', fg='white', bg='blue')
label.grid(row=0, column=0)

word = StringVar(value=' '.join(blanks))

word_label = Label(root, textvariable=word, font='Verdana 20 bold', bg='silver', fg='blue')
word_label.grid(row=2, column=1)

frame = Frame(root)
frame.grid(row=3, column=0, columnspan=2)


letters = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й',
           'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф',
           'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']

buttons = [Button(frame, font=('Arial', 15, 'bold'), bg='wheat', cursor='hand2') for i in range(33)]
for button in buttons:
    button.bind('<Button-1>', click_button)

for button in buttons:
    for letter in letters:
        if buttons.index(button) == letters.index(letter):
            button['text'] = letter

row=0
col=0
for i in range(len(buttons)):
    buttons[i].grid(row=row, column=col)
    col += 1
    if col == 11:
        row += 1
        col = 0

root.mainloop()
