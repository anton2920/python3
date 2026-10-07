import pygame

WIDTH = 50
HEIGHT = 50
FIELD_WIDTH = 15
FIELD_HEIGHT = 15
SCREEN_WIDTH = FIELD_WIDTH * WIDTH
SCREEN_HEIGHT = FIELD_HEIGHT * HEIGHT

F = "white"
W = "black"
B = "green"
G = "yellow"

Running = True

PLAYING = 1
GAMEOVER = 2


def CreateTestField():
    field = []
    for y in range(FIELD_HEIGHT):
        row = []
        for x in range(FIELD_WIDTH):
            row.append(F)
        field.append(row)
    for i in range(2, 5):
        field[i][i] = B
    return field


def CreateEmptyField():
    field = [[F, F, F, F, F, F, F, F, F, F, F, F, F, F, F],
             [F, F, F, F, F, F, F, F, F, F, F, F, F, F, F],
             [F, F, F, F, F, F, F, F, F, F, F, F, F, F, F],
             [F, F, F, F, F, F, F, F, F, F, F, F, F, F, F],
             [F, F, F, F, F, F, F, F, F, F, F, F, F, F, F],
             [F, F, F, F, F, F, F, F, F, F, F, F, F, F, F],
             [F, F, F, F, F, F, F, F, F, F, F, F, F, F, F],
             [F, F, F, F, F, F, F, F, F, F, F, F, F, F, F],
             [F, F, F, F, F, F, F, F, F, F, F, F, F, F, F],
             [F, F, F, F, F, F, F, F, F, F, F, F, F, F, F],
             [F, F, F, F, F, F, F, F, F, F, F, F, F, F, F],
             [F, F, F, F, F, F, F, F, F, F, F, F, F, F, F],
             [F, F, F, F, F, F, F, F, F, F, F, F, F, F, F],
             [F, F, F, F, F, F, F, F, F, F, F, F, F, F, F],
             [F, F, F, F, F, F, F, F, F, F, F, F, F, F, F]]
    assert ((len(field) == FIELD_HEIGHT) and (len(field[0]) == FIELD_WIDTH))
    return field


def CreateLevel1Field():
    field = [[F, F, F, F, W, W, W, W, W, F, F, F, F, F, F],
             [F, W, W, W, W, F, F, F, W, F, F, F, F, F, F],
             [F, W, F, F, W, 1, F, F, W, W, W, W, F, F, F],
             [F, W, F, 1, 1, F, F, F, F, F, F, W, F, F, F],
             [F, W, 0, F, F, W, 1, F, 1, W, F, W, F, F, F],
             [F, W, W, W, F, W, F, F, F, W, F, W, F, F, F],
             [F, F, W, F, F, W, W, W, W, W, F, W, F, F, F],
             [F, F, W, F, F, G, G, G, G, G, F, W, F, F, F],
             [F, F, W, W, W, W, W, W, W, W, W, W, F, F, F],
             [F, F, F, F, F, F, F, F, F, F, F, F, F, F, F],
             [F, F, F, F, F, F, F, F, F, F, F, F, F, F, F],
             [F, F, F, F, F, F, F, F, F, F, F, F, F, F, F],
             [F, F, F, F, F, F, F, F, F, F, F, F, F, F, F],
             [F, F, F, F, F, F, F, F, F, F, F, F, F, F, F],
             [F, F, F, F, F, F, F, F, F, F, F, F, F, F, F]]
    assert ((len(field) == FIELD_HEIGHT) and (len(field[0]) == FIELD_WIDTH))
    return field


def GetPlayerPosition(field):
    for y, row in enumerate(field):
        for x, tile in enumerate(row):
            if tile == 0:
                field[y][x] = F
                return [x, y]


def GetBoxesPositions(field):
    boxes = []
    for y, row in enumerate(field):
        for x, tile in enumerate(row):
            if tile == 1:
                field[y][x] = F
                boxes.append([x, y])
    return boxes


def GetMovement(events):
    movement = [0, 0]
    for event in events:
        if event.type == pygame.QUIT:
            global Running
            Running = False
        elif event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                movement[0] = -1
            elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                movement[0] = 1
            elif keys[pygame.K_w] or keys[pygame.K_UP]:
                movement[1] = -1
            elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
                movement[1] = 1
            break
    return tuple(movement)


def CanMove(entity, movement, field, boxes):
    if movement == (0, 0):
        return False

    isPlayer = type(entity) is list
    moved = (entity[0] + movement[0], entity[1] + movement[1])
    if (moved[0] < 0) or (moved[0] + 1 > FIELD_WIDTH):
        return False
    if (moved[1] < 0) or (moved[1] + 1 > FIELD_HEIGHT):
        return False

    for y, row in enumerate(field):
        for x, tile in enumerate(row):
            if tile == W:
                if (moved[0] == x) and (moved[1] == y):
                    return False

    for box in boxes:
        x, y = box[0], box[1]
        if (moved[0] == x) and (moved[1] == y):
            if isPlayer:
                return CanMove((x, y), movement, field, boxes)
            else:
                return False

    return True


def Move(entity, movement, boxes):
    entity[0] += movement[0]
    entity[1] += movement[1]
    for box in boxes:
        if (entity[0] == box[0]) and (entity[1] == box[1]):
            box[0] += movement[0]
            box[1] += movement[1]


def Render(screen, player, field, boxes):
    for y, row in enumerate(field):
        for x, tile in enumerate(row):
            pygame.draw.rect(screen, tile, (x * WIDTH, y * HEIGHT, WIDTH, HEIGHT))
    for box in boxes:
        clr = "green"
        x, y = box[0], box[1]
        if field[y][x] == G:
            clr = "purple"
        pygame.draw.rect(screen, clr, (x * WIDTH, y * HEIGHT, WIDTH, HEIGHT))
    pygame.draw.rect(screen, "red", (player[0] * WIDTH, player[1] * HEIGHT, WIDTH, HEIGHT))


def GameOver(field, boxes):
    gCount = 0
    for y, row in enumerate(field):
        for x, tile in enumerate(row):
            if tile == G:
                gCount += 1

    bOnGCount = 0
    for box in boxes:
        x, y = box[0], box[1]
        if field[y][x] == G:
            bOnGCount += 1

    return gCount == bOnGCount


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    state = PLAYING
    restart = True

    global Running
    while Running:
        events = pygame.event.get()
        if state == PLAYING:
            for event in events:
                if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_r):
                    restart = True

            if restart:
                field = CreateLevel1Field()
                player = GetPlayerPosition(field)
                boxes = GetBoxesPositions(field)
                restart = False

            movement = GetMovement(events)
            if CanMove(player, movement, field, boxes):
                Move(player, movement, boxes)

            Render(screen, player, field, boxes)

            if GameOver(field, boxes):
                state = GAMEOVER
        else:
            print("YOU WON!")
            Running = False

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

main()
