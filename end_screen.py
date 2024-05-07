'''
Creates an end screen for user to play again or exit
'''

from main_screen import draw_text
import pygame as p

def end_screen(result):
    p.init()
    screen = p.display.set_mode((777, 512))
    p.display.set_caption("Game Over")
    font = p.font.SysFont(None, 40)
    button_font = p.font.SysFont(None, 48)

    running = True
    play_again = False

    while running:
        screen.fill((0, 0, 0))

        draw_text(f"Game Over: {result}", font, screen, (255, 255, 255), (screen.get_width() // 2, 100))

        button_width = 200
        button_height = 50
        button_color = (255, 255, 255)

        play_again_rect = draw_text("Play Again", button_font, screen, (255, 255, 255), (screen.get_width() // 2, screen.get_height() // 2))
        exit_rect = draw_text("Exit", button_font, screen, (255, 255, 255), (screen.get_width() // 2, screen.get_height() // 2 + 100))

        for event in p.event.get():
            if event.type == p.QUIT:
                running = False
                play_again = False
            elif event.type == p.MOUSEBUTTONDOWN:
                if play_again_rect.collidepoint(event.pos):
                    running = False
                    play_again = True
                elif exit_rect.collidepoint(event.pos):
                    running = False
                    play_again = False

        p.display.flip()

    return play_again