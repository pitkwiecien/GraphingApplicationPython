import PySimpleGUI as sg
import grapher

points = 0


def main_layout():
    return [[sg.Text("f(x): "), sg.InputText(), sg.Button("Calculate")]]


def extended_layout(i):
    grapher.graph(i)
    return [[sg.Image("graph.png")]]
