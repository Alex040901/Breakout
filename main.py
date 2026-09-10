import sys, pygame, random

# Inicializando los componenetes de pygame
pygame.init()

# Definiendo canvas
size = width, height = 1080, 720

#Coordenadas de la bola y su variable
x, y = 0, 0

#ball = (x, y)

font = pygame.font.Font(None, 30)
font_state = pygame.font.Font(None, 60)
font_sub = pygame.font.Font(None, 60)
score = 0
high_score = 0

#Radio de la bola
radio = 10

ball_x, ball_y = 540, 630

#Posición del paddle
paddle_x, paddle_y = 500, 650
paddle_width, paddle_height = 100, 20

paddle = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)

#Posición de la bola
ball_position = pygame.Rect(ball_x, ball_y, 20, 20)
ball_position.center = (ball_x, ball_y)

# Definiendo color de canvas
black = 0, 0, 0
white = 255, 255, 255
blue = 0, 0, 255

# Bloques
brick_width, brick_height = 30, 30
rows, cols, padding = 1, 3, 5
offset_top, offset_left = 30, 900
row_colors = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255)]

total_lives = 3
print("Total de vidas", total_lives)

bricks = []
ball_speed = [5, -5]
paddle_speed = 8

screen = pygame.display.set_mode(size)
pygame.display.set_caption("BREAKOUT")

ball_in_play = False
game_over = False
running = True
clock = pygame.time.Clock()

def draw_score(surface, score_value):
    score_text = font.render(f"Score: {score_value}", True, white)
    surface.blit(score_text, (0, 0))

#def draw_score(surface, score_value, high_score_value):
    #score_text = font.render(f"Score: {score_value} | Record: {high_score_value}", True, white)
    #surface.blit(score_text, (offset_top, offset_left))

def reset_round():
    global ball_speed, ball_in_play
    ball_in_play = False
    ball_speed = [3, -3]
    paddle.x = paddle_x
    paddle.y = paddle_y  

def reset_game():
    global total_lives, game_over, score
    total_lives = 3
    score = 0
    game_over = False
    reset_round()
    create_blocks()

def create_blocks():
    bricks.clear()
    
    for r in range (rows):
        y = offset_top + r * (brick_height + padding)
        color = row_colors[r % len(row_colors)]

        for c in range (cols):
            x = offset_left + c * (brick_width + padding) 
            bloque = pygame.Rect(x, y, brick_width, brick_height)

            bricks.append((bloque, color))    

def draw_blocks():
    for bloque, color in bricks:
        pygame.draw.rect(screen, color, bloque)

while running:
    clock.tick(60)

    keys = pygame.key.get_pressed()
    ball_position = ball_position.move(ball_speed)

    if ball_in_play == False:
        ball_position.centerx = paddle.centerx
        ball_position.bottom = paddle.top

    if ball_in_play == True:
        ball_position.x += ball_speed[0]
        ball_position.y += ball_speed[1]

    if game_over == True:
        reset_game()

    if keys[pygame.K_UP]:
        ball_in_play = True

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
    if ball_position.top < 0 or ball_position.bottom > height:
        ball_speed[1] = -ball_speed[1]

    if ball_position.bottom > height:
        print("-1UP")
        total_lives -= 1
        print("Vidas ", total_lives)
        if total_lives > 0:
            reset_round()
        if total_lives == 0:
            print("REINICIO......")
            reset_game()


    if paddle.colliderect(ball_position) and ball_speed[1] > 0:
        print("Collision detected")
        ball_speed[1] = -abs(ball_speed[1])
        ball_position.bottom = paddle.top

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False          
    
    screen.fill(black)
    pygame.draw.circle(screen, white, ball_position.center, radio)
    pygame.draw.rect(screen, (255, 0, 0), ball_position, 2)

    for bloques, color in bricks:
        pygame.draw.rect(screen, color, bloques)

        for item in bricks[:]:
            bloques, color = item
            if ball_position.colliderect(bloques):
                print("COLISIÓN CON BLOQUE")
                score += 3
                bricks.remove(item)
                ball_speed[1] = -ball_speed[1]
                break

    if len(bricks) == 0:
        print("HAZ PASADO DE NIVEL")
        reset_game()

    pygame.draw.rect(screen, blue, paddle)
    draw_score(screen, score)
    pygame.display.flip()
pygame.quit()
sys.exit()
