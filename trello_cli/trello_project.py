"""
Trello CLI

Final project for Web APIs lesson
https://alissa-huskey.github.io/python-class/lessons/web-apis.html

TODO
----
[x] Phase 1: Print the open cards from your To Do list.
[x] Phase 2: Show card details
    [x] Include any checklist items

"""
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

def api_request_checklist(checklist_id):
    """Requests checklist info associated with specified card"""

    checklist_endpoint = f"checklists/{checklist_id[0]}"

    url = f"https://api.trello.com/1/{checklist_endpoint}"

    response = requests.get(
        url,
        params = {
            'key': trello_key,
            'token': trello_token
            }
        )

    if response.ok == False:
        print(f"There was a {response.status_code} error! Because: {response.reason}")
        return

    checklist_api_data = response.json()

    checklist_items = checklist_api_data['checkItems']

    return checklist_items

def print_cards(data):
    """Takes raw data from API_request and formats/prints active cards, more info available if user requests it"""

    #prints card id, name, shorturl, and labels for all active cards
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

def print_checklist(list_data):
    """Prints the checklist items associated with the selected card and their status"""

    for i , checklist in enumerate(list_data, 1):        
        if checklist['state'] == 'complete':
            print("[X]", end = " ")
        else:
            print("[ ]", end = " ")
        print(checklist['name'])


def main():
    """Calls api_request and print_card functions"""
    data = api_request()

    print_cards(data)

    #user requests a specific card and the prints the description, checklist items, and maybe more?
    card_selection = input("Which Card would you like more info on? Card: ")

    if card_selection.lower() == 'q' or card_selection.lower() == 'quit':
        print("Buh-Bye...")
        return
    
    card_selection = int(card_selection)

    if card_selection < len(data):
        #prints card description for user selection
        for i, card in enumerate(data, 1):
            if i == card_selection:
                print("-" * 30)
                print(f"Card {i}")
                print("-" * 30)
                print(f"Description: {card['desc']}")
                
                #checks if there are checklist items for card, and prints if applicable
                if bool(card['idChecklists']) == True:
                    print("Checklist:")
                    checklist_data = api_request_checklist(card['idChecklists'])
                    print_checklist(checklist_data)
    else:
        print("There is no such card.")

main()