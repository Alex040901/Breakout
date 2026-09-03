import sys, pygame

# Inicializando los componenetes de pygame
pygame.init()

# Definiendo canvas
size = width, height = 1080, 720
x, y = 100, 100
radio = 10
bullet = (x, y)
left, top, width, height = (500, 650, 100, 20)
canvas = (left, top, width, height)

# Definiendo velocidad del objeto
speed = [2, 2]

# Definiendo color de canvas
black = 0, 0, 0
white = 255, 255, 255

screen = pygame.display.set_mode(size)

running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    



    screen.fill(black)
    pygame.draw.circle(screen, white, bullet, radio)
    pygame.draw.rect(screen, white, canvas)
    pygame.display.flip()
pygame.quit()
sys.exit()
