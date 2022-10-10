import PySimpleGUI as sg
import layouts


window = sg.Window("Quizzers", layouts.main_layout())

QUESTIONS = 5

name = ""

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        print("EXIT")
        break
    elif event == 'Calculate':
        i = values[0]
        '''
        new_input = i.split()
        new_input_ints = list(map(int, new_input))
        '''
        window.extend_layout(window, layouts.extended_layout(i))


window.close()
print("End of application")
