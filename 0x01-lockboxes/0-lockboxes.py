#!/usr/bin/python3
"""Lock Boxes"""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be unlocked.

    Args:
        boxes (list of list of int): A list where each element

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    unlocked = set()
    queue = [0]
    unlocked.add(0)
    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if key < len(boxes) and key not in unlocked:
                unlocked.add(key)
                queue.append(key)
    return len(unlocked) == len(boxes)
