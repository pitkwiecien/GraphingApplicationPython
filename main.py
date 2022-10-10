import PySimpleGUI as sg

import grapher
import layouts

window = sg.Window("Quizzers", layouts.main_layout())

QUESTIONS = 5

increased = False
name = ""
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        print("EXIT")
        break
    elif event == 'Calculate':
        i = values[0]
        if not increased:
            window.extend_layout(window, layouts.extended_layout(i))
            increased = True
        else:
            grapher.graph(i)
            window['img'].update('graph.png')
            window.refresh()


window.close()
print("End of application")
