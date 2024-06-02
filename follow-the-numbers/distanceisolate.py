import math
import random

MIN_DISTANCE = 30

def calculate_distance(point1, point2):
    """
    Calculates the Euclidean distance between two points.
    Assumes each point is a tuple (x, y).
    """
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def generate_new_position(previous_positions, X_Max, Y_Max):
    """
    Generates a new position and checks its distance from previous positions.
    Returns a valid position with distance >= 30.
    """
    while True:
        new_x = random.randint(10, X_Max)  # Adjust the range as needed
        new_y = random.randint(10, Y_Max)  # Adjust the range as needed
        new_position = (new_x, new_y)

        valid = True
        for prev_position in previous_positions:
            distance = calculate_distance(new_position, prev_position)
            if distance < MIN_DISTANCE:
                valid = False
                break

        if valid:
            return new_position