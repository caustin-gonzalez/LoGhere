import random


# Clamp a value within minimum and maximum numbers
def clamp(value, min_value, max_value):
    if value < min_value:
        return min_value
    elif value > max_value:
        return max_value
    else:
        return value


# Move the current value towards a target value
def move_towards(current_value, target_value, amount):
    if current_value < target_value:
        return min(current_value + amount, target_value)
    else:
        return max(current_value - amount, target_value)


# Unknown purpose at this stage
def gaussian():
    s = 0
    c = 0
    while c < 16:
        c = c + 1
        s = s + random.randint()
    return (s - 8) / 4