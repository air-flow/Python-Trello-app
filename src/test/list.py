import os
import access
import pprint


def cd():
    os.chdir(os.path.dirname(__file__))


def main():
    client = access.main()
    boards = client.list_boards()
    pprint.pprint(boards[-1])
    board = client.get_board(boards[-1].id)
    # cards = board.get_cards()
    # pprint.pprint(cards)
    print(board.open_lists())


if __name__ == "__main__":
    cd()
    main()
