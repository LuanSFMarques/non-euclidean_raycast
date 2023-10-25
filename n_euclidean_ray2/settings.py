import math

# Major Settings
RESOLUTION =  WIDTH, HEIGHT = 1620, 540  # Resolution
HEIGHT_2 = HEIGHT*2
HALF_WIDTH = (WIDTH//3) // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 60    


PLAYER_POS_1 = HEIGHT//2, HEIGHT//2                    # Position in mini-map
PLAYER_ANGLE_1 = 0                        # Initial Angle
PLAYER_SPEED_1 = 0.2                    # Constant Player Speed
PLAYER_RSPEED_1 = 0.004                   # Constant Rotation Speed

PLAYER_POS_2 = 1.5, 5                     # Position in mini-map
PLAYER_ANGLE_2 = 0                        # Initial Angle
PLAYER_SPEED_2 = 0.004                    # Constant Player Speed
PLAYER_RSPEED_2 = 0.004                   # Constant Rotation Speed

MAP_PIECES_NUM = 10                     # Number of pieces per map
PIECES_SIZE = (WIDTH/3)/MAP_PIECES_NUM

# Ray casting
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = (WIDTH//3) // 2
HALF_NUM_RAYS = NUM_RAYS // 2
DELTA_ANGLE = FOV / NUM_RAYS
MAX_DEPTH = 20

# COLORS
C_TILE1 = (161,151,191)
C_TILE2 = (215,202,255)
C_TILE_DETEC = (0, 210, 0)
C_TILE_BORDER = (10, 10, 10)
C_PLAYER = None
C_RAY = None

SCREEN_DIST = HALF_WIDTH / math.tan(HALF_FOV)
SCALE = (WIDTH//3) // NUM_RAYS