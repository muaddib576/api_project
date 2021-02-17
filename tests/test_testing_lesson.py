# """Testing functions for the testing lesson"""

# from trello_cli.testing_lesson import endgame, letter_grade

# def test_endgame_true():
#     assert endgame(True) == 'Congratulations, you won!', "Should retrun 'Congratulations, you won!'"
# def test_endgame_false():
#     assert endgame(False) == 'You lost. Better luck next time!', "Should return 'You lost. Better luck next time!'"
# def test_endgame_zero():
#     assert endgame(0) == 'You lost. Better luck next time!', "Should return 'You lost. Better luck next time!'"
# def test_endgame_str():
#     assert endgame("blah") == 'You lost. Better luck next time!', "Should return invalid win outcome?"

# def test_grade_valid_scores():
#     assert letter_grade(95) == 'A', "95 should return 'A'"
#     assert letter_grade(85) == 'B', "85 should return 'B'"
#     assert letter_grade(75) == 'C', "75 should return 'C'"
#     assert letter_grade(65) == 'D', "65 should return 'D'"
#     assert letter_grade(55) == 'F', "55 should return 'F'"
# def test_grade_invalid_inputs():
#     assert letter_grade(110) == False, "110 should return False"
#     assert letter_grade(-5) == False, "-5 should return False"
#     assert letter_grade("Blah") == False, "Str should return False"
#     assert letter_grade() == False, "Blank should return False"

