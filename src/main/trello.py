# TODO class trello

class TrelloAPI():
    """
    docstring
    """

    def __init__(self):
        """
        docstring
        """
        client = None
        api_key = None
        token = None

    def _TrelloClientAccess(self):
        """
        docstring
        """
        pass

    def _GetApiKeyFile(self, path="../../mine/Token.txt"):
        """
        docstring
        """
        with open(path, encoding="utf-8") as target:
            result = target.readlines()
        result = list(map(lambda i: i.rstrip("\n"), result))
        self.api_key, self.token = result


if __name__ == "__main__":
    temp = [1, 2]
    a, b = temp
    print(a, b)
