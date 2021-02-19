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
# if the file and the file being executed are in the same directory you can do
# it this way
# from private import trello_key, trello_token

# the . means in this same package (in the same directory)
# from .private import trello_key, trello_token

# or you can use the module name
from trello_cli.private import trello_key, trello_token

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
    """Takes raw data and creates a string with id, name, due date, shorturl, and labels for active cards"""
    text = ""
    for i, card in enumerate(data, 1):
        if card['subscribed'] == False:
            continue
        # '!!!' is placeholder for a line of '-'s
        text += '!!!\n'
        text += f"Card {i}\n"
        text += '!!!\n'
        text += f"Name: {card['name']}\n"
        text += f"Url: {card['shortUrl']}\n"
        text += f"Due: {card['due']}\n"
        text += "Labels: "
        for label in card['labels']:
            text += f"{label['name']}, "
        #removes comma/space from final label and adds new line
        text = text[:-2] + "\n"
    # replaces '!!!' with a line of '-'s equal to longest line length
    # in retrospect this is not smart if terminal is small...
    temp_text = text.split('\n')
    max_line = 0
    for i in temp_text:
        line_length = len(i)
        if line_length > max_line:
            max_line = line_length
    max_line = ('-' * max_line)
    text = text.replace('!!!', max_line)
    return text

def print_card_selection(selected_card, card_checklist, card_data):
    """Prints selected card description and any checklist items"""

    text = "!!!\n"
    text += f"Card {selected_card}: {card_data['name']}\n"
    text += "!!!\n"
    text += f"Description: {card_data['desc']}\n"
    
    # checks if there are checklist items for card, and prints if applicable
    if card_checklist:
        text += "Checklist:\n"
        for i , checklist in enumerate(card_checklist, 1):        
            if checklist['state'] == 'complete':
                text += "[X] "
            else:
                text += "[ ] "
            text += f"{checklist['name']}\n"

    # replaces '!!!' with a line of '-'s equal to longest line length
    temp_text = text.split('\n')
    max_line = 0
    for i in temp_text:
        line_length = len(i)
        if line_length > max_line:
            max_line = line_length
    max_line = ('-' * max_line)
    text = text.replace('!!!', max_line)

    return text

def card_select_validation(selection, num_cards):
    """Checks if user card selection is a valid integer"""

    try:
        int(selection)
    except ValueError:
        return False

    # isinstance(value, type) checks if selection is boolean
    if isinstance(selection, bool):
        return False

    selection = int(selection)

    if selection > 0 and selection <= num_cards:
        return True
    else:
        return False

def main():
    """Calls api_request and print_card functions"""
    data = api_request()
    text = print_cards(data)
    print(text)

    #user requests a specific card and the prints the description, checklist items, and maybe more?
    card_selection = input("Which Card would you like more info on? Card: ")
    while card_select_validation(card_selection, len(data)) == False:
        # ends cli if user inputs Q or Quit
        if card_selection.lower() == 'q' or card_selection.lower() == 'quit':
            print("Buh-Bye...")
            return
        card_selection = input("That is not a valid card... Which Card would you like more info on? Card: ")
    card_selection = int(card_selection)
    # because index 0 is card 1
    selected_card_data = data[card_selection-1]
    # requests checklist data from API if checklist ID is present
    checklist_data = []
    if selected_card_data['idChecklists']:
        checklist_data = api_request_checklist(selected_card_data['idChecklists'])
    text = print_card_selection(card_selection, checklist_data, selected_card_data)
    print(text)


# main()