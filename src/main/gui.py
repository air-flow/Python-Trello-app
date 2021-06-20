# TODO pysimplegui class
import PySimpleGUI as sg
# https://pysimplegui.readthedocs.io/en/latest/#output-element
import stopwatch as sw
import os


class PySimpleGUI():
    """
    GUI操作するクラス
    機能一覧
    - 書籍選択 プルダウン
    - 書籍追加 ボタン
    - 日付 出力
    - ストップウォッチ タイム 出力
    - ストップウォッチ start ボタン
    - ストップウォッチ end ボタン
    - Trello リスト追加 チェックボックス
    - Trello 読破追加 チェックボックス
    - Trello 時間追加 チェックボックス
    - 実行 ボタン
    - 結果表示 ボタン
    """

    def __init__(self,):
        sg.theme('DarkAmber')
        self._layout = []
        self._flag = None

    def _Exec(self,):
        self._Initlayout()
        self._window = sg.Window('サンプルプログラム', self._layout)

    def _MainWindow(self):
        self._Exec()
        while True:
            event, values = self._window.read()
            self._JugeEventParameter(event, values)
            if not self._flag:
                break
        self._EndWindow()

    def _EndWindow(self,):
        self._window.close()

    def _Initlayout(self, ):
        t = []
        # t.append([sg.Button('読み取り', key='read'),
        #          sg.Button('csvに保存', key='save')])
        # t.append([sg.Output(size=(40, 10), key="stopwatch")])
        t.append([sg.Text('書籍選択', size=(15, 1)), sg.Combo(
            ('あり', 'なし'), default_value="あり", size=(10, 1), key='SelectBook'), sg.Button('書籍追加', key='AddBook')])
        # t.append([
        #     sg.Button('書籍追加', key='AddBook')])
        # t.append([sg.Output(size=(40, 3), key="stopwatch")])
        t.append([sg.Text(self._StringToday(), size=(15, 1), key="date")])
        t.append([sg.Text("00:00:00", size=(15, 1), key="stopwatch"), sg.Button(
            'START', key='swstart'), sg.Button('STOP', key='swstop')])
        t.append([sg.Checkbox("today list add", font=("Meiryo", 10))])
        t.append([sg.Checkbox("list not exists create list", font=("Meiryo", 10))])
        t.append([sg.Checkbox("time add", font=("Meiryo", 10))])
        t.append([sg.Checkbox("book finish checkd", font=("Meiryo", 10))])
        t.append([
            sg.Button('exec', key='exec'), sg.Button('view', key='view')])
        self._layout.append(t)

    def _JugeEventParameter(self, event, values):
        self._flag = False
        if event == sg.WIN_CLOSED:  # ウィンドウのXボタンを押したときの処理
            self._flag = False
        if event == "read":
            self._flag = False
        if event == "save":
            self._window.FindElement('2').Update('python')
            self._flag = True

    def _StopWatch(self, ):
        s = sw.StopWatch()
        s._StartTime()
        # self._window.FindElement('stopwatch').Update(
        #     s._start_time.strftime('%H:%M:%S'))
        s._EndTime()
        return s._start_time.strftime('%H:%M:%S')

    def _StringToday(self, ):
        s = sw.StopWatch()
        return s._Today()


def main():
    cd()
    gui = PySimpleGUI()
    gui._MainWindow()


def cd():
    os.chdir(os.path.dirname(__file__))


if __name__ == "__main__":
    main()
