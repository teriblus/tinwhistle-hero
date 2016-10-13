import pygame
import score

FPS = 40

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("tin whistle hero")

clock = pygame.time.Clock()

eventIn = 2000

circlePosition = 50
done = False
print_text = False
text_clock = pygame.time.Clock()
text_delay = 0
text = None
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            print_text = True
            text_clock.tick()
            text_delay = 0
            text = score.get_text(abs(500 - circlePosition))

    circlePosition = (circlePosition + 10) % 700

    if print_text:
        text_delay += text_clock.tick()
        if text_delay > 500:
            print_text = False

    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, [circlePosition, 50], 10)
    pygame.draw.line(screen, BLACK, [500, 0], [500, 700], 5)

    if print_text:
        screen.blit(text, [250, 250])

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
