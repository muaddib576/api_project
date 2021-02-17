"""Various tests for the trello cli project"""

from trello_cli.trello_project import card_select_validation

def test_card_select_validation_nums():
    assert card_select_validation(1,3) == True, 'Should return True'
    assert card_select_validation(0,3) == True, 'Should return True'
    assert card_select_validation(0,1) == True, 'Should return True'
    assert card_select_validation(0,0) == False, 'Should return False'
    assert card_select_validation(1,0) == False, 'Should return False'
    assert card_select_validation(4,3) == False, 'Should return False'
    assert card_select_validation(-1,3) == False, 'Should return False'
def test_card_select_validation_str():
    assert card_select_validation('derp',3) == False, 'Should return False'
def test_card_select_validation_bool():
    assert card_select_validation(True,2) == False, 'Should return False'
    assert card_select_validation(False,2) == False, 'Should return False'


