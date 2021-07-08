# TODO pysimplegui class
import PySimpleGUI as sg
# https://pysimplegui.readthedocs.io/en/latest/#output-element
import stopwatch as sw
import os
import trelloAPI


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
    - 結果表示 ボタンllll
    """

    def __init__(self,):
        sg.theme('DarkAmber')
        self._layout = []
        self._flag = None
        self._stopwatch_flag = False

    def _Exec(self, window=True):
        layout = None
        if window:
            layout = self._Initlayout()
        else:
            layout = self._InitSublayout()
        self._AppendLayout(layout)
        self._window = sg.Window('サンプルプログラム', self._layout)

    def _MainWindow(self):
        self._Exec()
        while True:
            event, values = self._window.read(
                timeout=1000, timeout_key='-timeout-')
            self._JugeEventParameter(event, values)
            if not self._flag:
                break
        self._EndWindow()

    def _EndWindow(self,):
        self._window.close()

    def _Initlayout(self, ):
        t = []
        select_books = self._SelectBook()
        t.append([sg.Text('書籍選択', size=(15, 1)), sg.Combo(
            select_books, default_value=select_books[0], size=(25, 1), key='SelectBook'),
            sg.Button('書籍追加', key='AddBook'),
            sg.Button('書籍リセット', key='ResetBook')])
        t.append([sg.Text(self._StringToday(), size=(15, 1), key="date")])
        t.append([sg.Text("00:00:00", size=(15, 1), key="stopwatch"), sg.Button(
            'START', key='swstart'), sg.Button('STOP', key='swstop')])
        t.append([sg.Checkbox("toay list add", default=True,
                 font=("Meiryo", 10), key="today")])
        t.append([sg.Checkbox("time add", default=True,
                 font=("Meiryo", 10), key="time")])
        t.append([sg.Checkbox("book finish checkd",
                 default=False, font=("Meiryo", 10), key="finish")])
        t.append([
            sg.Button('exec', key='exec'), sg.Button('view', key='view')])
        return t

    def _InitSublayout(self, ):
        pass

    def _AppendLayout(self, layout):
        self._layout.append(layout)

    def _SelectBook(self):
        books = trelloAPI.TrelloGetBooks()
        return tuple(books.keys())

    def _JugeEventParameter(self, event, values):
        self._flag = False
        print(values)
        if event == sg.WIN_CLOSED:  # ウィンドウのXボタンを押したときの処理
            self._flag = False
        if event == "read":
            self._flag = False
        if event == "AddBook":
            text = sg.popup_get_text('書籍名入力', '書籍追加')
            self._flag = self._AddBook(text)
            print(self._flag, "flag")
        if event == "ResetBook":
            temp = self._SelectBook()
            self._window.find_element("SelectBook").Update(temp[-1])
            self._flag = True
        if event == "save":
            print(values)
            self._flag = False
        if event == "view":
            self._flag = self._ViewPopUp(values["SelectBook"])
        if event == "swstart":
            self._stopwatch_flag = self._StopWatchStart()
            self._flag = True
        if event == "swstop":
            self._stopwatch_flag = False
            self._flag = True
        if event == '-timeout-':
            if self._stopwatch_flag:
                self._window.FindElement('stopwatch').Update(
                    self._StopWatchTime())
            self._flag = True

    def _StopWatchInit(self, ):
        self._stopwatch = sw.StopWatch()

    def _StopWatchStart(self, ):
        self._StopWatchInit()
        self._stopwatch._StartTime()
        if self._stopwatch._start_time is not None:
            return True
        else:
            return False

    # def _StopWatchEnd(self, ):
    #     self._StopWatchInit()
    #     result = self._stopwatch._MeasurementTime()
    #     return self._stopwatch._strftime(result)

    def _StopWatchTime(self):
        result = self._stopwatch._TimeUp()
        return result

    def _AddBook(self, book_name):
        """
        TrelloAPI 書籍追加関数作成
        """
        result = trelloAPI.TrelloAddBooks(book_name)
        return result

    def _StringToday(self, ):
        s = sw.StopWatch()
        return s._Today()

    def _ViewPopUp(self, book):
        """
        確認表示する内容
        - 対象書籍
        - 読書時間
        - 日付
        """
        time_to_calculate = self._stopwatch._MeasurementTime()
        self._result = {
            "date": self._StringToday(),
            "read_time": time_to_calculate,
            "book_name": book
        }
        result = sg.popup_ok_cancel(
            self._result["date"], self._result["read_time"], self._result["book_name"])
        return result

    def _Save(self, check_list):
        pass


def main():
    cd()
    gui = PySimpleGUI()
    gui._MainWindow()


def test():
    gui = PySimpleGUI()
    print(gui._SelectBook())


def cd():
    os.chdir(os.path.dirname(__file__))


if __name__ == "__main__":
    main()
    # test()
