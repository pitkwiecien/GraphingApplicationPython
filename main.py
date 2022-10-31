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
        points = int(values[0])
        bounds = float(values[1])
        func = values[2]
        if not increased:
            window.extend_layout(window, layouts.extended_layout(points, bounds, func))
            increased = True
        else:
            grapher.graph(points, bounds, func)
            window['img'].update('graph.png')
            window.refresh()


window.close()
print("End of application")
