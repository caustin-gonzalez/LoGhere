
# Clamp a value within minimum and maximum numbers


def clamp(value, min_value, max_value):
    if value < min_value:
        return min_value
    elif value > max_value:
        return max_value
    else:
        return value


def move_towards(current_value, target_value, amount):
    if current_value < target_value:
        return min(current_value + amount, target_value)
    else:
        return max(current_value - amount, target_value)