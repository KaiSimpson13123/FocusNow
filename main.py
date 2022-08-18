import PySimpleGUI as sg
import os
import psutil
import wmi

f = wmi.WMI()

theme = sg.theme("Sandybeach")

layout = [
    [sg.Text("FocusNow")],
    [sg.Text("___________________")],
    [sg.Button("Focus")]
]

window = sg.Window("FocusNow", layout, element_justification='c', size=(250, 100))

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == 'Focus':
        maincustomLoop = True

        if maincustomLoop == True:
            flag1 = 0
            flag2 = 0
  
             # Iterating through all the running processes
            for process in f.Win32_Process():
                if "Teams.exe" == process.Name:
                    os.system("taskkill /PID Teams.exe /F")
                    print("Teams R")
                    flag1 = 1
  
            if flag1 == 0:
                print("Teams NR")

            for process in f.Win32_Process():
                if "Discord.exe" == process.Name:
                    os.system("taskkill /PID Discord.exe /F")
                    print("Discord R")
                    flag2 = 1
            
            if flag2 == 0:
                print("Discord NR")
