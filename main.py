import sys, pygame

# Inicializando los componenetes de pygame
pygame.init()

# Definiendo canvas
size = width, height = 1080, 720

#Coordenadas de la bola y su variable
x, y = 100, 100
ball = (x, y)
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

total_lives = 3
print("Total de vidas", total_lives)

# Definiendo color de canvas
black = 0, 0, 0
white = 255, 255, 255
blue = 0, 0, 255

ball_speed = [3, -3]
paddle_speed = 5

screen = pygame.display.set_mode(size)
pygame.display.set_caption("BREAKOUT")

game_over = False
ball_in_play = False
running = True
clock = pygame.time.Clock()

def reset_round():
    global ball_speed, ball_in_play
    ball_in_play = False
    ball_speed = [3, -3]
    paddle.x = paddle_x
    paddle.y = paddle_y  

def reset_game():
    global total_lives, game_over
    total_lives = 3
    reset_round()
    game_over = False

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

    pygame.draw.rect(screen, blue, paddle)
    pygame.display.flip()
pygame.quit()
sys.exit()
