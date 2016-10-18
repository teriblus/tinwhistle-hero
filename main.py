import pygame
import score
import sound
import color


def get_circle_positions(song, fps, pxPerFrame, goalLinePosition):
    duration = song.get_duration()
    pxPerMillisecond = (fps * pxPerFrame) / 1000.0
    positions = []
    for i in range(0, duration, 20):
        note = song.get_note(i)
        if note:
            positions.append([note, -int((i * pxPerMillisecond) - goalLinePosition)])
    return positions


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

song = sound.Song('/home/lecorgnt/Bureau/perso/tinwhistlehero/andro.mp3')
circlePositions = get_circle_positions(song, FPS, SPEED, GOAL_LINE)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            print_text = True
            text_clock.tick()
            text_delay = 0
            text = score.get_text(abs(GOAL_LINE - circlePositions[-1][1]))
            circlePositions.pop(-1)

    for i in range(0, len(circlePositions)):
        circlePositions[i][1] = (circlePositions[i][1] + SPEED)

    if print_text:
        text_delay += text_clock.tick()
        if text_delay > 500:
            print_text = False

    screen.fill(color.WHITE)
    for circlePosition in circlePositions:
        pygame.draw.circle(screen, color.RED, [circlePosition[1], 50 + 50 * circlePosition[0]], 10)
    pygame.draw.line(screen, color.BLACK, [GOAL_LINE, 0], [GOAL_LINE, size[0]], 5)

    if print_text:
        screen.blit(text, [250, 250])

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
