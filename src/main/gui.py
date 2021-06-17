# TODO pysimplegui class
import PySimpleGUI as sg
# https://pysimplegui.readthedocs.io/en/latest/#output-element


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
        self._test()
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

    def _test(self, ):
        t = [sg.Text('読み取り対象のファイルとページを指定してください')]
        t.append([sg.Button('読み取り', key='read'),
                 sg.Button('csvに保存', key='save')])
        t.append([sg.Output(size=(40, 10), key="1")])
        t.append([sg.Output(size=(40, 10), key="2")])
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


def main():
    gui = PySimpleGUI()
    gui._MainWindow()


if __name__ == "__main__":
    main()
