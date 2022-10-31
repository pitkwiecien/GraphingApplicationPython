import PySimpleGUI as sg

import grapher
import layouts

window = sg.Window("Grapher", layouts.main_layout(), finalize=True)

window['func_input'].bind("<Return>", "_Enter")

QUESTIONS = 5

increased = False
name = ""

while True:
    event, values = window.read()
    print(event)
    print(values)
    if event == sg.WIN_CLOSED or event == "Exit":
        print("EXIT")
        break
    elif event == 'Calculate' or event == "func_input_Enter":
        points = int(values[0])
        bounds = float(values[1])
        domain = values[2]
        imports = values[3].split(",") if values[3] != '' else []
        func = values["func_input"]

        for i in range(len(imports)):
            imports[i] = imports[i].strip()

        if not increased:
            window.extend_layout(window, layouts.extended_layout(points, bounds, domain, imports, func))
            increased = True
        else:
            grapher.graph(points, bounds, domain, imports, func)
            window['img'].update('graph.png')
            window.refresh()


window.close()
print("End of application")
