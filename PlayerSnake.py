class PlayerSnake:
    direction='right'
    headX = 10
    headY = 10
    bodyCoordinates = []
    availableFood = 0

    def reset(snakeLength: int):
        PlayerSnake.bodyCoordinates=[]
        PlayerSnake.headX = 10
        PlayerSnake.headY = 10
        i = 0
        while i < snakeLength:
            i += 1
            PlayerSnake.headX += 1
            PlayerSnake.bodyCoordinates.append([PlayerSnake.headX, PlayerSnake.headY])
        PlayerSnake.move()

    def move():
        if (PlayerSnake.direction == 'right'):
            PlayerSnake.headX += 1
        elif (PlayerSnake.direction == 'left'):
            PlayerSnake.headX -= 1
        elif (PlayerSnake.direction == 'down'):
            PlayerSnake.headY += 1
        else:
            PlayerSnake.headY -= 1
        PlayerSnake.bodyCoordinates.append([PlayerSnake.headX, PlayerSnake.headY])
        if (PlayerSnake.availableFood >= 1):
            PlayerSnake.availableFood -= 1
        else:
            PlayerSnake.bodyCoordinates.pop(0)
