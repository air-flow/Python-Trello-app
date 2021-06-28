# TODO class trello
from trello import TrelloClient
import os


def cd():
    os.chdir(os.path.dirname(__file__))


class TrelloAPI():
    """
    docstring
    """

    def __init__(self):
        """
        docstring
        """
        self._api_key = None
        self._token = None
        result = self._GetFile()
        self._SetAPIKeyToken(result)
        self._client = None
        self._TrelloClientAccess()

    def _TrelloClientAccess(self):
        """
        docstring
        """
        self._client = TrelloClient(
            api_key=self._api_key,
            api_secret=self._token,
        )

    def _GetFile(self, path="../../mine/Token.txt"):
        """
        docstring
        """
        with open(path, encoding="utf-8") as target:
            result = target.readlines()
            result = list(map(lambda i: i.rstrip("\n"), result))
            return result

    def _SetAPIKeyToken(self, files):
        """
        docstring
        """
        self._api_key, self._token = files

    def _GetBookList(self):
        """
        docstring
        """
        path = self._GetFile("../../mine/Borad.txt")
        print(self._client.get_board(path[0]))


if __name__ == "__main__":
    cd()
    t = TrelloAPI()
    t._GetBookList()
