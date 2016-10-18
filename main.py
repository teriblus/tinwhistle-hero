import pygame
import score

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("tin whistle hero")

GOAL_LINE = 500  # px
SPEED = 4  # px/frame
FPS = 60  # frame/sec

clock = pygame.time.Clock()

done = False
print_text = False
text_clock = pygame.time.Clock()
text_delay = 0
text = None
circlePositions = [0,50,100,200,300]
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            print_text = True
            text_clock.tick()
            text_delay = 0
            text = score.get_text(abs(500 - circlePositions[-1]))
            circlePositions.pop(-1)

    for i in range(0,len(circlePositions)):
        circlePositions[i] = (circlePositions[i] + SPEED) % 700

    if print_text:
        text_delay += text_clock.tick()
        if text_delay > 500:
            print_text = False

    screen.fill(WHITE)
    for circlePosition in circlePositions:
        pygame.draw.circle(screen, RED, [circlePosition, 50], 10)
    pygame.draw.line(screen, BLACK, [GOAL_LINE, 0], [GOAL_LINE, 700], 5)

    if print_text:
        screen.blit(text, [250, 250])

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
