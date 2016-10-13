import pygame

BLACK = (0, 0, 0)

pygame.font.init()
font = pygame.font.SysFont('FreeMono', 50, True, False)
text_good = font.render("GOOD", True, BLACK)
text_super = font.render("SUPER !", True, BLACK)
text_perfect = font.render("PERFECT !!!", True, BLACK)
text_poor = font.render("POOR", True, BLACK)

perfect_spot = 5
super_spot = 12
good_spot = 25


def get_text(distance):
    if distance < perfect_spot:
        text = text_perfect
    elif distance < super_spot:
        text = text_super
    elif distance < good_spot:
        text = text_good
    else:
        text = text_poor
    return text
