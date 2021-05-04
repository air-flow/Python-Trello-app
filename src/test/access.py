import trello
# from trello import trelloclient
import pprint
import os


def cd():
    os.chdir(os.path.dirname(__file__))


def ApigetKeyFile():
    with open("../../mine/Token.txt", encoding="utf-8") as target:
        result = target.readlines()
    return list(map(lambda i: i.rstrip("\n"), result))


if __name__ == "__main__":
    cd()
    temp = ApigetKeyFile()
    # print(type(temp[0]))
    client = trello.TrelloClient(api_key=temp[0],
                                 token=temp[1],
                                 )
    boards = client.list_boards()
    pprint.pprint(boards)
    # print(ApigetKeyFile())
