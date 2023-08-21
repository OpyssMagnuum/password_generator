import string
import PySimpleGUI as sg
from random import randint as rand

numbs = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
specials = ['!', '#', '@', '$', ']', '[', '*', '?', '(', ')']


def generate(lower, upper, nums, special, length):
    max = int(lower) + int(upper) + int(nums) + int(special)
    res = ''
    possible = []
    if lower:
        possible.append(string.ascii_lowercase)
    if upper:
        possible.append(string.ascii_uppercase)
    if nums:
        possible.append(numbs)
    if specials:
        possible.append(specials)

    if max != 0:
        for i in range(length):
            num = rand(1, max) - 1
            res += possible[num][rand(0, len(possible[num]) - 1)]
    return res


def backg_color_change(lower, upper, nums, special, length):
    points = length // 4 * 2
    if not lower:
        points -= 1
    if not upper:
        points -= 1
    if not nums:
        points -= 1
    if not special:
        points -= 2

    if points < 3:
        return 'red'
    elif points < 7:
        return 'orange'
    else:
        return 'light blue'


layout = [
    [sg.Text('Генератор паролей', key='-TEXT-', font=('Arial', 20),
             border_width=5, justification='left', expand_x=True)],

    [sg.Input('Pass12!&', key='-PASS-', font=('Arial Bold', 20),
              justification='center', background_color='orange')],

    [sg.Text('Длина пароля:', key='-TEXT-', font=('Arial', 14),
             justification='left', expand_x=True)],

    [sg.Slider(range=(3, 24), default_value=8,
               orientation='horizontal', key='-SL-', expand_x=True)],

    [sg.Checkbox('Нижний регистр (a-z)', key='-CHlower-',
                 font=('Arial', 12), expand_x=True, default=True)],

    [sg.Checkbox('Верхний регистр (A-Z)', key='-CHupper-',
                 font=('Arial', 12), expand_x=True, default=True)],

    [sg.Checkbox('Цифры (0-9)', key='-CHnum-',
                 font=('Arial', 12), expand_x=True, default=True)],

    [sg.Checkbox('Специальные символы', key='-CHspecial-',
                 font=('Arial', 12), expand_x=True, default=True)],

    [sg.Button('Сгенерировать', key='-Bgenerate-',
               font=('Arial', 14), expand_x=True)]

]

window = sg.Window('Генератор паролей', layout)
while True:
    event, values = window.read()
    print(event, values)
    if event in (sg.WINDOW_CLOSED, "Exit"):
        break
    if event == '-Bgenerate-':
        window['-PASS-'].update(generate(values['-CHlower-'], values['-CHupper-'],
                                         values['-CHnum-'], values['-CHspecial-'], int(values['-SL-'])),
                                background_color=backg_color_change(values['-CHlower-'], values['-CHupper-'],
                                                                    values['-CHnum-'], values['-CHspecial-'],
                                                                    int(values['-SL-'])))

window.close()
