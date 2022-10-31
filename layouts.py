import PySimpleGUI as sg
import grapher


def main_layout():
    return [[sg.Text("Points: "), sg.InputText(size=10), sg.Text("Value Bounds: "), sg.InputText(size=10), sg.Text("Domain: "), sg.InputText(size=10)],
            [sg.Text("Imports: "), sg.InputText()],
            [sg.Text("f(x): "), sg.InputText(key="func_input"), sg.Button("Calculate")]]


def extended_layout(points, bounds, domain, imports, func):
    grapher.graph(points, bounds, domain, imports, func)
    return [[sg.Image("graph.png", key='img')]]
