def endgame(is_winner):
    """Return a string to tell the player if they won or lost."""
    if is_winner:
        return "Congratulations, you won!"
    else:
        return "You lost. Better luck next time!"

def letter_grade(score):
    """Return the letter grade for a particular number score"""
    ranges = {
        (90, 100): "A",
        (80, 89): "B",
        (70, 79): "C",
        (60, 69): "D",
        (0, 59): "F",
    }

    for score_range, letter in ranges.items():
        min_score, max_score = score_range
        if score >= min_score and score <= max_score:
            return letter
    
    return False

if __name__ == "__main__":
    main()

# trello_cli/testing_lesson.py (this file)
# tests/test_testing_lesson.py (new file)