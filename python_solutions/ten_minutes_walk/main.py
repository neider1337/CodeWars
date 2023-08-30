def is_valid_walk(walk):
    horizontal = 0
    vertical = 0
    if len(walk) > 10 or len(walk) < 10:
        return False
    if len(walk) == 10:
        for a in walk:
            if a in ['n', 's']:
                if a == 'n':
                    vertical += 1
                if a == 's':
                    vertical -= 1
            if a in ['w', 'e']:
                if a == 'w':
                    horizontal += 1
                if a == 'e':
                    horizontal -= 1
        if horizontal == 0 and vertical == 0:
            return True
        if horizontal != 0 or vertical != 0:
            return False
    pass
