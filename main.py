import sys, pygame, math

# Inicializando los componenetes de pygame
pygame.init()

# Definiendo canvas
size = width, height = 1080, 720

#Coordenadas de la bola y su variable
x, y = 0, 0

#ball = (x, y)

font = pygame.font.Font(None, 30)
font_lives = pygame.font.Font(None, 30)
font_state = pygame.font.Font(None, 50)
score = 0
high_score = 0

#Radio de la bola
radio = 10

#Posición del paddle
paddle_x, paddle_y = 500, 650
paddle_width, paddle_height = 100, 20

paddle = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)

#Posición de la pelota
ball_x, ball_y = 540, 630
ball_position = pygame.Rect(ball_x, ball_y, 20, 20)
ball_position.center = (ball_x, ball_y)

# Definiendo color de canvas
black = 0, 0, 0
white = 255, 255, 255
blue = 0, 0, 255

# Bloques
brick_width, brick_height = 30, 30
rows, cols, padding = 30, 3, 5
offset_top, offset_left = 30, 17
row_colors = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255)]

total_lives = 3

bricks = []
ball_speed = [4, 5]

paddle_speed = 8

screen = pygame.display.set_mode(size)
pygame.display.set_caption("BREAKOUT")

game_won = False
current_level = 1
ball_in_play = False
game_over = False
running = True
clock = pygame.time.Clock()

LEVEL_CONFIG = {
    1: {"rows": 3, "cols": 7, "paddle_width": 200, "speed": 4, "base": 8},
    2: {"rows": 5, "cols": 9, "paddle_width": 180, "speed": 5, "base": 11},
    3: {"rows": 7, "cols": 11, "paddle_width": 150, "speed": 6, "base": 14},
    4: {"rows": 9, "cols": 13, "paddle_width": 140, "speed": 7, "base": 17},
    5: {"rows": 1, "cols": 1, "paddle_width": 100, "speed": 8, "base": 20},
}

def bounce_angle(ball_speed, normal):
    vx, vy = ball_speed
    nx, ny = normal

    longitud = math.sqrt(nx**2 + ny**2)

    nx /= longitud
    ny /= longitud

    product = vx * nx + vy * ny

    ball_speed[0] = vx - 2 * product * nx
    ball_speed[1] = vy - 2 * product * ny

def paddle_bounce(ball_position, paddle, ball_speed):
    # 1. Donde pego la pelota
    hit_x = ball_position.centerx

    # 2. Convertirlo a p (-1 izquierda, 0 centro, 1 derecha)
    p = (hit_x - paddle.centerx) / (paddle.width / 2)

    # 3. Mantener la velocidad actual
    speed = math.sqrt(ball_speed[0]**2 + ball_speed[1]**2)

    # 4. Modificamos Vx
    ball_speed[0] = ball_speed[0] + 3 * p

    # 5. Evitar que Vx sea muy grande
    max_vx = speed * 0.9
    ball_speed[0] = max(-max_vx, min(ball_speed[0], max_vx))

    # 6. Calculamos Vy
    ball_speed[1] = -math.sqrt(speed**2 - ball_speed[0]**2)

def start_level(level):
    config = LEVEL_CONFIG[level]

    paddle.width = config["paddle_width"]
    paddle.centerx = width // 2

    create_blocks(config["rows"], config["cols"])

    reset_round()
    ball_origin()

def draw_score(surface, score_value):
    score_text = font.render(f"Score: {score_value}", True, white)
    surface.blit(score_text, (0, 0))

def draw_lives(surface, lives):
    lives_text = font_lives.render(f"Lives: {lives}", True, white)
    surface.blit(lives_text, (200, 0))

def draw_state(surface):
    if game_over:
        texto = font_state.render("Game Over", True, white)
        text_rect = texto.get_rect()
        text_rect.center = (width // 2, height // 2)
        surface.blit(texto, text_rect)

    if game_over or game_won:
        restart_text = font_state.render("Presiona ENTER para reiniciar", True, white)
        restart_rect = restart_text.get_rect()
        restart_rect.center = (width // 2, height // 3)
        surface.blit(restart_text, restart_rect)

    if game_won:
        won_text = font_state.render("Game Win!", True, white)
        won_rect = won_text.get_rect()
        won_rect.center = (width // 2, height // 2)
        surface.blit(won_text, won_rect) 

def reset_round():
    global ball_speed, ball_in_play, paddle_speed
    ball_in_play = False
    speed = LEVEL_CONFIG[current_level]["speed"]
    ball_speed = [speed, -speed]
    paddle.centerx = width // 2
    base_speed = LEVEL_CONFIG[current_level]["base"]
    paddle_speed = base_speed
    #paddle.x = paddle_x
    #paddle.y = paddle_y  

def reset_game():
    global total_lives, game_over, score, current_level, game_won
    current_level = 1
    total_lives = 3
    score = 0
    game_over = False
    game_won = False
    start_level(1)
    #reset_round()

def ball_origin():
    global ball_in_play
    ball_in_play = False
    paddle.x = paddle_x
    paddle.y = paddle_y
    ball_position.centerx = paddle.centerx
    ball_position.bottom = paddle.top

def create_blocks(rows_count, cols_count):
    global bricks
    bricks.clear()

    total_grid_width = (cols * brick_width) + ((cols - 1) * padding)

    offset_left = (screen.get_width() - total_grid_width) // 2
    
    for r in range (rows_count):
        y = offset_top + r * (brick_height + padding)
        color = row_colors[r % len(row_colors)]

        for c in range (cols_count):
            x = offset_left + c * (brick_width + padding) 
            bloque = pygame.Rect(x, y, brick_width, brick_height)

            bricks.append((bloque, color))    

def draw_blocks():
    for bloque, color in bricks:
        pygame.draw.rect(screen, color, bloque)

start_level(1)
while running:
    clock.tick(60)

    keys = pygame.key.get_pressed()

    if ball_in_play == False:
        ball_position.centerx = paddle.centerx
        ball_position.bottom = paddle.top

    if ball_in_play:
        previous_position = ball_position.copy()

        ball_position.x += ball_speed[0]
        ball_position.y += ball_speed[1]

    if keys[pygame.K_UP]:
        ball_in_play = True

    if not game_over and not game_won:

        if keys[pygame.K_LEFT]:
            paddle.x -= paddle_speed
        
        if keys[pygame.K_RIGHT]:
            paddle.x += paddle_speed

    if paddle.left < 0:
        paddle.left = 0
    if paddle.right > width:
        paddle.right = width

    if ball_position.left < 0 or ball_position.right > width:
        ball_speed[0] = -ball_speed[0]
    if ball_position.top < 0:
        ball_speed[1] = -ball_speed[1]

    if not game_over and not game_won:
        if ball_position.bottom > height:
            total_lives -= 1
            if total_lives > 0:
                reset_round()
            else:
                game_over = True        

    if paddle.colliderect(ball_position) and ball_speed[1] > 0:
        #ball_speed[1] = -abs(ball_speed[1])
        ball_position.bottom = paddle.top
        paddle_bounce(ball_position, paddle, ball_speed)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and (game_over or game_won):
                reset_game()

    
    screen.fill(black)
    pygame.draw.circle(screen, white, ball_position.center, radio)
    #pygame.draw.rect(screen, (255, 0, 0), ball_position, 2)

    for bloques, color in bricks:
        pygame.draw.rect(screen, color, bloques)

    for item in bricks[:]:
        bloques, color = item
        colision_valida = False
        if ball_position.colliderect(bloques):
            score += 3
            bricks.remove(item)
            if previous_position.bottom <= bloques.top and \
                ball_position.bottom >= bloques.top and \
                ball_position.right >= bloques.left and \
                ball_position.left <= bloques.right and \
                ball_speed[1] > 0:
                colision_valida = True
                normal = (0, -1)
                bounce_angle(ball_speed, normal)
            elif previous_position.right <= bloques.left and \
                ball_position.right >= bloques.left and \
                ball_position.bottom >= bloques.top and \
                ball_position.top <= bloques.bottom and \
                ball_speed[0] > 0:
                normal = (-1, 0)
                bounce_angle(ball_speed, normal)
            elif previous_position.left >= bloques.right and \
                ball_position.left <= bloques.right and \
                ball_position.bottom >= bloques.top and \
                ball_position.top <= bloques.bottom and \
                ball_speed[0] < 0:
                normal = (1, 0)
                bounce_angle(ball_speed, normal)
            elif previous_position.top >= bloques.bottom and \
                ball_position.top <= bloques.bottom and \
                ball_position.right >= bloques.left and \
                ball_position.left <= bloques.right and \
                ball_speed[1] < 0:
                normal = (0, 1)
                bounce_angle(ball_speed, normal)
            break

    if not game_over:
        if len(bricks) == 0:
            current_level += 1
            if current_level in LEVEL_CONFIG:
                start_level(current_level)
            else:
                game_won = True                

    if game_over:
        draw_state(screen)
    if game_won:
        draw_state(screen)
    pygame.draw.rect(screen, blue, paddle)
    draw_score(screen, score)
    draw_lives(screen, total_lives)
    pygame.display.flip()
pygame.quit()
sys.exit()
