def getShape(name, generation):
    if name == 'shape1':
        return shape1(generation)
    elif name == 'simkinGliderGun':
        return simkinGliderGun(generation)
    elif name == 'beeHive':
        return beeHive(generation)
    elif name == 'stairs':
        return stairs(generation)

def shape1(generation):
    width = len(generation)
    height = len(generation[0])
    middleX = int(width / 2)
    middleY = int(height / 2)
    generation[middleX][middleY] = 1
    generation[middleX][middleY + 1] = 1
    generation[middleX + 1][middleY -1] = 1
    generation[middleX + 1][middleY] = 1
    generation[middleX + 2][middleY] = 1
    return generation

def simkinGliderGun(generation):
    width = len(generation)
    height = len(generation[0])
    middleX = int(width / 2)
    middleY = int(height / 2)
    gapX = 10
    # block 1
    generation[middleY - 2][middleX - 6 - gapX] = 1
    generation[middleY - 2][middleX - 5 - gapX] = 1
    generation[middleY - 1][middleX - 6 - gapX] = 1
    generation[middleY - 1][middleX - 5 - gapX] = 1
    # simkin glilder gun
    generation[middleY][middleX + 4 - gapX] = 1
    generation[middleY - 1][middleX + 4 - gapX] = 1
    generation[middleY - 2][middleX + 4 - gapX] = 1
    generation[middleY - 3][middleX + 5 - gapX] = 1
    generation[middleY - 4][middleX + 6 - gapX] = 1
    generation[middleY - 4][middleX + 7 - gapX] = 1
    generation[middleY - 3][middleX + 9 - gapX] = 1
    generation[middleY - 2][middleX + 10 - gapX] = 1
    generation[middleY - 1][middleX + 10 - gapX] = 1
    generation[middleY - 0][middleX + 10 - gapX] = 1
    generation[middleY - 1][middleX + 11 - gapX] = 1
    generation[middleY + 1][middleX + 9 - gapX] = 1
    generation[middleY + 2][middleX + 7 - gapX] = 1
    generation[middleY + 2][middleX + 6 - gapX] = 1
    generation[middleY + 1][middleX + 5 - gapX] = 1
    generation[middleY - 1][middleX + 8 - gapX] = 1
    # canon
    generation[middleY - 2][middleX + 14 - gapX] = 1
    generation[middleY - 2][middleX + 15 - gapX] = 1
    generation[middleY - 3][middleX + 14 - gapX] = 1
    generation[middleY - 3][middleX + 15 - gapX] = 1
    generation[middleY - 4][middleX + 14 - gapX] = 1
    generation[middleY - 4][middleX + 15 - gapX] = 1
    generation[middleY - 5][middleX + 16 - gapX] = 1
    generation[middleY - 5][middleX + 18 - gapX] = 1
    generation[middleY - 6][middleX + 18 - gapX] = 1
    generation[middleY - 1][middleX + 16 - gapX] = 1
    generation[middleY - 1][middleX + 18 - gapX] = 1
    generation[middleY - 0][middleX + 18 - gapX] = 1
    # block2
    generation[middleY - 3][middleX + 28 - gapX] = 1
    generation[middleY - 3][middleX + 29 - gapX] = 1
    generation[middleY - 4][middleX + 28 - gapX] = 1
    generation[middleY - 4][middleX + 29 - gapX] = 1

    return generation

def beeHive(generation):
    width = len(generation)
    height = len(generation[0])
    middleX = int(width / 2)
    middleY = int(height / 2)
    generation[middleY][middleX] = 1
    generation[middleY + 1][middleX + 1] = 1
    generation[middleY + 1][middleX + 2] = 1
    generation[middleY][middleX + 3] = 1
    generation[middleY - 1][middleX + 2] = 1
    generation[middleY - 1][middleX + 1] = 1
    return generation

def stairs(generation):
    width = len(generation)
    height = len(generation[0])
    middleX = int(width / 2)
    middleY = int(height / 2)
    generation[middleY][middleX] = 1
    generation[middleY][middleX + 1] = 1
    generation[middleY - 1][middleX - 1] = 1
    generation[middleY - 1][middleX] = 1
    generation[middleY - 2][middleX - 2] = 1
    generation[middleY - 2][middleX - 1] = 1
    return generation
