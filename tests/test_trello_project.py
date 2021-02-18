"""Various tests for the trello cli project"""

from trello_cli.trello_project import card_select_validation, print_cards

def test_card_select_validation_nums():
    assert card_select_validation(1,3) == True, 'Should return True'
    assert card_select_validation(3,3) == True, 'Should return True'
    assert card_select_validation(0,1) == False, 'Should return False'
    assert card_select_validation(0,0) == False, 'Should return False'
    assert card_select_validation(0,3) == False, 'Should return False'
    assert card_select_validation(1,0) == False, 'Should return False'
    assert card_select_validation(4,3) == False, 'Should return False'
    assert card_select_validation(-1,3) == False, 'Should return False'
def test_card_select_validation_str():
    assert card_select_validation('derp',3) == False, 'Should return False'
def test_card_select_validation_bool():
    assert card_select_validation(True,2) == False, 'Should return False'
    assert card_select_validation(False,2) == False, 'Should return False'


def test_print_cards():
    text = """-----------------------------
Card 1
-----------------------------
Name: Test Name A
Url: test.com
Due: monday ya dummy
Labels: real things, not fake
-----------------------------
Card 2
-----------------------------
Name: -5
Url: 4.5
Due: True
Labels: False, 1
"""

    data = [
        {
    "name": 'Test Name A',
    "shortUrl" : 'test.com',
    "due" : 'monday ya dummy',
    "labels" : [
        {
            "name" : 'real things'
        },
        {
            "name" : 'not fake'
        }
    ],
    "subscribed" : True
    },
    {
    "name": -5,
    "shortUrl" : 4.5,
    "due" : True,
    "labels" : [
        {
            "name" : False,
        },
        {
            "name" : 1,
        }
    ],
    "subscribed" : True
    }
    ]

    assert print_cards(data) == text, "Should return formatted cards"