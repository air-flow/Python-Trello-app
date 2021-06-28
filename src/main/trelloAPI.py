# TODO class trello
from trello import TrelloClient, card
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
        self._board = []
        self._doing_list = []

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
        path = self._GetFile("../../mine/list.txt")
        self._doing_list = self._client.get_list(path[0])
        print(self._doing_list.name)

    def _GetBoardList(self):
        path = self._GetFile("../../mine/Borad.txt")
        self._board = self._client.get_board(path[0])
        cards = self._board.get_cards()
        for i in cards:
            if i.list_id == self._doing_list.id:
                print(i.name)
                print(i.list_id)


if __name__ == "__main__":
    cd()
    t = TrelloAPI()
    t._GetBookList()
    t._GetBoardList()
