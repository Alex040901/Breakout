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

ball_x, ball_y = 100, 100

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

ball_speed = [5, 5]

screen = pygame.display.set_mode(size)
pygame.display.set_caption("BREAKOUT")

running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)

    keys = pygame.key.get_pressed()
    paddle_speed = 5
    ball_position = ball_position.move(ball_speed)

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
