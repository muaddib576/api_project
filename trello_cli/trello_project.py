from private import trello_key, trello_token
import requests
from pprint import pprint

def api_request():
    """Requests my active to-do list cards from Trello API"""

    member_endpoint = 'members/me/boards'
    lists_endpoint = 'lists/5ffe4253796d4a206734351c/cards'

    url = f"https://api.trello.com/1/{lists_endpoint}"

    response = requests.get(
        url,
        params = {
            'key': trello_key,
            'token': trello_token,
            'filter': 'open',
            'lists': 'open',
            'cards': 'visible'
            }
        )

    if response.ok == False:
        print(f"There was a {response.status_code} error! Because: {response.reason}")
        return

    json_data = response.json()
    return json_data

def print_cards(data):
    """Takes raw data from API_request and formats/prints active cards, more info available if user requests it"""

    #prints card id, name, shorturl, and labels
    for i, card in enumerate(data, 1):
        if card['subscribed'] == False:
            continue
        
        print("-" * 30)
        print(f"Card {i}")
        print("-" * 30)
        print(f"Name: {card['name']}")
        print(f"Url: {card['shortUrl']}")
        print(f"Due: {card['due']}")
        
        label_list = []
        for label in card['labels']:
            label_list.append(label['name'])
        
        print("Labels: " + ", ".join(label_list))
        print()

    card_selection = int(input("Which Card would you like more info on? Card: "))

    for i, card in enumerate(data, 1):
        if i == card_selection:
            print(card['desc'])



def main():
    """Calls api_request and print_card functions"""
    data = api_request()

    print_cards(data)

main()