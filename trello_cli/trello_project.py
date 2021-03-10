"""
Trello CLI

Final project for Web APIs lesson
https://alissa-huskey.github.io/python-class/lessons/web-apis.html

TODO
----
[ ] change flow such that "view card" is a called action, rather than assumed
[ ] change initial api call to include all list types (To Do, In-Progress, etc)
[ ] present user cards grouped by list (w/ only name and number of card)
[ ] add command to move from to-do to in-progress
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

    if not checklist_id:
        return []

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

def format_lines(raw_card_lines):
    """Formats lines with a header"""
    # print_card_selection() sends a list not a list of lists, this fixes that
    if not isinstance(raw_card_lines[0], list):
        raw_card_lines = [raw_card_lines]
    # finds the max line length and creates a header
    max_line = 0
    for card_lines in raw_card_lines:
        for line in card_lines:
            line_length = len(line)
            if line_length > max_line:
                max_line = line_length
    
    max_line = ('-' * max_line)

    # inserts header before and after card number line
    text = ""
    for card_lines in raw_card_lines:
        card_lines.insert(1, max_line)
        card_lines.insert(0, max_line)
        text += "\n"
        text += "\n".join(card_lines)

    return text

def print_cards(data):
    """Extracts key information from subscribed cards"""
    card_list = []
    for i, card in enumerate(data, 1):
        if card['subscribed'] == False:
            continue
        lines = []
        lines.append(f"Card {i}")
        lines.append(f"Name: {card['name']}")
        lines.append(f"Url: {card['shortUrl']}")
        lines.append(f"Due: {card['due']}")
        text = "Labels: "
        for label in card['labels']:
            text += f"{label['name']}, "
        #removes comma/space from final label
        text = text[:-2]
        lines.append(text)

        card_list.append(lines)
    
    return format_lines(card_list)

def print_card_selection(selected_card, card_checklist, card_data):
    """Prints selected card description and any checklist items"""
    lines = []
    lines.append(f"Card {selected_card}: {card_data['name']}")
    lines.append(f"Description: {card_data['desc']}")

    # checks if there are checklist items for card, and prints if applicable
    if card_checklist:
        lines.append("Checklist:")
        for list_item in card_checklist:
            if list_item['state'] == 'complete':
                lines.append(f"[X] {list_item['name']}")
                continue
            lines.append(f"[ ] {list_item['name']}")
    
    return format_lines(lines)

def card_select_validation(selection, num_cards):
    """Checks if user card selection is a valid integer"""

    try:
        selection = int(selection)
    except ValueError:
        return False

    return selection > 0 and selection <= num_cards

def new_main():
    """Presents user with actions, makes the appropriet API calls based on input, and prints output"""
    command_bank = ['v','view','m','move','q','quit']


def main():
    """Calls api_request and print_card functions"""
    data = api_request()
    text = print_cards(data)
    print(text)

    # user requests a specific card and the prints the description, checklist items, and maybe more?
    card_selection = input("Which Card would you like more info on? Card: ")
    while card_select_validation(card_selection, len(data)) == False:
        # ends cli if user inputs Q or Quit
        if card_selection.lower() in ['q','quit']:
            print("Buh-Bye...")
            return
        card_selection = input("That is not a valid card... Which Card would you like more info on? Card: ")
    
    card_selection = int(card_selection)
    # because index 0 is card 1
    selected_card_data = data[card_selection-1]
    # requests checklist data from API if checklist ID is present
    checklist_data = api_request_checklist(selected_card_data['idChecklists'])
    text = print_card_selection(card_selection, checklist_data, selected_card_data)
    print(text)

if __name__ == "__main__":
    main()