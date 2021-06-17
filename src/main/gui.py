# TODO pysimplegui class
import PySimpleGUI as sg


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

    def _Exec(self,):
        self._test()
        self._window = sg.Window('サンプルプログラム', self._layout)

    def _MainWindow(self):
        self._Exec()
        while True:
            event, values = self._window.read()
            if event == "read":
                break
        self._EndWindow()

    def _EndWindow(self,):
        self._window.close()

    def _test(self, ):
        t = [sg.Text('読み取り対象のファイルとページを指定してください')]
        t.append([sg.Button('読み取り', key='read'),
                 sg.Button('csvに保存', key='save')])
        self._layout.append(t)


def main():
    gui = PySimpleGUI()
    gui._MainWindow()


if __name__ == "__main__":
    main()
