import random
def roll_two_d6() -> tuple[int, int]:
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    return dice1, dice2

def is_bust(score: int) -> bool:
    if score > 100:
        return True
    else: return False

def is_exact_100(score: int) -> bool:
    if score == 100:
        return True
    else: return False
def closer_to_target(a: int, b: int, target: int = 100) -> int | None:
    p1 = target - a
    p2 = target - b
    if p1 > p2:
        return 2
    elif p2 > p1:
        return 1
    else:
        return
    

def sum_roll(dice: tuple, sum_before: int) -> int:
    sum_dice = dice[0] + dice[1]
    return sum_before + sum_dice

def turn_decision(input_fn):
    if input_fn == "r" or input_fn == "p":
        return True
    else:
        return False
    