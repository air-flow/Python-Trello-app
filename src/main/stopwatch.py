# TODO stopwatch function
import datetime
import time


class StopWatch():
    """
    時間計測をおこなう
    機能一覧
    - スタート
    - ストップ
    - 計測時間出力
    - 一定時間ごとに通知
    """

    def __init__(self):
        self._start_time = None
        self._end_time = None
        self._all_time = 0

    def _StartTime(self):
        self._start_time = datetime.datetime.now()

    def _EndTime(self):
        self._end_time = datetime.datetime.now()

    def _MeasurementTime(self):
        self._all_time = self._end_time - self._start_time

    def _Today(self):
        return datetime.datetime.now().strftime('%Y-%m-%d')


if __name__ == "__main__":
    s = StopWatch()
    s._StartTime()
    time.sleep(10)
    s._EndTime()
    s._MeasurementTime()
    print(s._all_time)
