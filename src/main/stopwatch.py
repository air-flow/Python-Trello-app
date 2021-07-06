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
        self._EndTime()
        self._all_time = self._end_time - self._start_time
        return self._all_time
        # return self._strftime(self._all_time)

    def _Today(self):
        return datetime.datetime.now().strftime('%Y-%m-%d')

    def _TimeUp(self):
        temp = datetime.datetime.now() - self._start_time
        # print(temp, type(temp))
        return temp
        # return self._strftime(temp)

    def _strftime(self, time):
        return time.strftime('%H:%M:%S')


if __name__ == "__main__":
    s = StopWatch()
    s._StartTime()
    # time.sleep(10)
    s._EndTime()
    # s._MeasurementTime()
    s._TimeUp()
    print(s._all_time)
    for i in range(5):
        time.sleep(1)
        print(s._TimeUp())
