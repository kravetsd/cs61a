# coding: utf-8
from dice import four_sided, six_sided, make_test_dice
from ucb import main, trace, log_current_line, interact
def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 0.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN Question 1
    
    sum = 0
    for outcome in range(num_rolls):
        a = dice()
        if a == 1:
            print('sorry it outcomes {}'.format(a))
            return 0
        else: sum = sum + a
    return sum
    # END Question 1
def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free Bacon).

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function of no args that returns an integer outcome.
    """
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
     # BEGIN Question 2
    strscore = str(opponent_score)
    if num_rolls == 0:
        try:
            return int(strscore[0])+int(strscore[1])
        except: return opponent_score
    else:
        return roll_dice(num_rolls,dice)
       
    # END Question 2
def select_dice(score, opponent_score):
    """Select six-sided dice unless the sum of SCORE and OPPONENT_SCORE is a
    multiple of 7, in which case select four-sided dice (Hog wild).
    """
    # BEGIN Question 3
    if (score*opponent_score)%7 ==0:
        return four_sided
    else:
        return six_sided
    # END Question 3
def get_str_dig(dig,swap=True):
    if dig <10 :
        return str(dig)
    elif swap == True:
        return str(dig % 10), str(dig//10)
    else :
        return str(dig // 10), str(dig % 10)
    
def is_swap(score0, score1):
    """Returns whether the last two digits of SCORE0 and SCORE1 are reversed
    versions of each other, such as 19 and 91.
    """
    # BEGIN Question 4
    if get_str_dig(score0) == get_str_dig(score1,swap=False):
        return True
    else:
        return False
    # END Question 4
    
