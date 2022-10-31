import PySimpleGUI as sg
import grapher


def main_layout():
    return [[sg.Text("Points: "), sg.InputText(size=20), sg.Text("Value Bounds: "), sg.InputText(size=20)],
            [sg.Text("f(x): "), sg.InputText(), sg.Button("Calculate")]]


def extended_layout(points, bounds, func):
    grapher.graph(points, bounds, func)
    return [[sg.Image("graph.png", key='img')]]
