import json

import requests


def format_content(content):
    url = "https://ai-kcs.51talk.com/v1/completion-messages"

    payload = json.dumps({
        "inputs": {
            "query": content
        },
        "response_mode": "blocking",
        "user": "abc-123",
    })
    headers = {
        'Authorization': 'Bearer app-cipSpdKUkXex0U31SUB9CM4C',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response)
    response = response.json()
    return response["answer"]


if __name__ == "__main__":
    content = "Of he populatign despite their age or social stardaurds"
    print(format_content(content))
