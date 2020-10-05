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
    def bitesItSelf():
        for id, coordinate in enumerate(PlayerSnake.bodyCoordinates):
            if (
                (id < len(PlayerSnake.bodyCoordinates) - 1) and
                (coordinate[0] == PlayerSnake.headX) and
                (coordinate[1] == PlayerSnake.headY)
            ):
                print('noooooo')
                return True
        return False
    def bitesEdge(GameSettings):
        if not GameSettings.isInArea(PlayerSnake.headX, PlayerSnake.headY):
            print('nooo')