import PySimpleGUI as sg
import time


def show_time():
    jikan = time.strftime('%I:%M:%S')
    return jikan


sg.theme('Dark')

layout = [
    [sg.Text(size=(8, 1), font=('Helvetica', 20),
             justification='center', key='-jikan-')],
    [sg.Button('exec', key='exec'), sg.Button('view', key='view')]
]

window = sg.Window('Watch', layout)

while True:
    event, values = window.read(timeout=100, timeout_key='-timeout-')
    # timeoutを指定することで、timeoutイベントが起こります。timeoutの単位はたぶんms
    # print(event,values)
    # ↑コメントアウトを外すと、どんなイベントが起こっているか確かめることができます。

    if event in (None,):
        break
    elif event in '-timeout-':
        jikan = show_time()
        window['-jikan-'].update(jikan)

window.close()
