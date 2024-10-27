import random

def generate_number_grid(size=10, min_value=0, max_value=9):
    return [[random.randint(min_value, max_value) for _ in range(size)] for _ in range(size)]
