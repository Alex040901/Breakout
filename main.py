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

#Posición del paddle
dx1, dx2 = 500, 650
width2, height2 = 100, 20

# Definiendo velocidad del objeto
speed = 5

# Definiendo color de canvas
black = 0, 0, 0
white = 255, 255, 255
blue = 0, 0, 255

screen = pygame.display.set_mode(size)
pygame.display.set_caption("BREAKOUT")

running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        dx1 -= speed
        dx2 = 650
    if keys[pygame.K_RIGHT]:
        dx1 += speed
        dx2 = 650

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False  

    
    screen.fill(black)
    pygame.draw.circle(screen, white, ball, radio)
    pygame.draw.rect(screen, blue, (dx1, dx2, width2, height2))
    pygame.display.flip()
pygame.quit()
sys.exit()
