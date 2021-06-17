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


if __name__ == "__main__":
    pass
