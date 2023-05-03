# File created by: Diego Lopez

# screen
WIDTH = 800
HEIGHT = 600

#sprites
PLAYER_ACC = 2
PLAYER_FRICTION = -0.3
PLAYER_JUMP = 20
PLAYER_GRAV = 0.8
MOB_ACC = 2
MOB_FRICTION = -0.3

#color
BLACK = (0,0,0)
GREY = (20,20,20)
WHITE = (255,255,255)
BLUE = (50,50,255)
RED = (255,50,50)
DARK_RED = (150,40,40)


FPS = 60
RUNNING = True
SCORE = 0
PAUSED = False

# Starting platforms
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40, (GREY), "ice"),
                 (200, HEIGHT * 3 / 4, 100, 20, (BLACK), "bouncey"),
                 (125, HEIGHT - 350, 100, 5, (200,100,50), "disappearing"),
                 (500, HEIGHT - 350, 100, 5, (200,100,50), "disappearing"),
                 (350, 200, 100, 20, (GREY), "normal"),
                 (600, 50, 50, 20, (GREY), "normal")]