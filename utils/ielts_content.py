import json

import requests


def format_content(content):
    url = "http://ai-kcs.51talk.com/v1/completion-messages"

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
    print(response.text)
    response = response.json()
    return response["answer"].strip().strip("```json").strip()


if __name__ == "__main__":
    content = "['Shopping is very popular among the mojority', 'Of he populatign despite their age or social stardaurds', 'This is due do the fact ihat most people find shopping', 'as an experience which makes a difference in her day', 'to day life Some pecple find themselveo ir a diferenr', 'worldsurrounded by vauriow material things which hey', 'may or may not be ab to pwrchase. Even if hey Cre not', 'able to rance hesehey fird much pleasure in ocking', 'and feeling hese things crd imaginirg owning them some', 'daySome people go shopping when thay really cocnt t', 'purchase thrgs and they prefer to look arourd ard', 'compore tha prices before buyirg tham.I think most', 'people love to go shopping bercuse then +hey cowd mee+', 'is in the', 'latest rend. prouida hern q pleasant', 'disraction fron dher routire and somelimes dull life', 'The most importaunt effect shoppirg has on an', 'ndiuidual is that + nourishe the self-esteemAn', 'and ths makes people come out of their shels and', 'be more extrovert.Purchasing sorethingas we a', 'knowing dhat yoy cre Firancially abl to perchase', 'something', 'give more self corfidencs to peoplo', 'The ncrease in popwarity t go shoppirg', 'hop many effects on tha society, People mcy be encowrag', 'to gointo new businesses and it cill improve dh', 'wllbe cregted for', 'by the', 'increase', 'o populari+y manufachurers wil try to', 'mprove dheir', 'productsso that the onsumers can', 'amoy.', 'a wide raunge', 'Of products', 'he product as wel a the servce prouided by', 'the sales staff cill be mproved', 'More job opprtunities will be created', 'n', 'advertising', 'as tha manufatwrers try to sell their prodict', 'prodet', 'So dhat they will not be misleaced by infericr qualiny', 'products', 'find', 'shopping an', 'inreresting', 'crd pleasurabk', 'experience', 'qs eachyear', 'passe by', 'Simply', 'pecause', 'it enriches my', 'heart', 'ad', 'mind.']"
    print(format_content(content))
    print(json.loads(format_content(content)))
