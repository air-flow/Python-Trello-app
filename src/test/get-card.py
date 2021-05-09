
import requests
import json
import access
import os
import pprint


def cd():
    os.chdir(os.path.dirname(__file__))


if __name__ == "__main__":
    cd()
    url = "https://api.trello.com/1/cards/{id}"

    headers = {
        "Accept": "application/json"
    }
    temp = access.ApigetKeyFile()
    query = {
        'key': temp[0],
        'token': temp[1]
    }

    response = requests.request(
        "GET",
        url,
        headers=headers,
        params=query
    )
    pprint.pprint(response)
# print(json.dumps(json.loads(response.text),
#       sort_keys=True, indent=4, separators=(",", ": ")))
