"""
Creates a welcome screen with user interaction included.
"""


import pygame as p

def main_screen():
    p.init()    # Initialise pygame
    screen = p.display.set_mode((777, 512))
    p.display.set_caption("Chess Game")
    font = p.font.SysFont(None, 40)

    running = True
    player_choice = None
    button_visible = True  # Flag to control button visibility
    show_options = False  # This flag indicates whether to show additional text

    # Button properties
    button_width = 200
    button_height = 50
    button_color = (255, 255, 255)  # White
    button_text = "Play"
    button_font = p.font.SysFont(None, 48)  # Larger font for the button
    
    play_ai_rect = None  # Initialize variable to avoid UnboundLocalError
    play_player_rect = None  # Initialize variable for player choice option
    
    while running:
        
        screen.fill((0, 0, 0))  # Clear the screen with black
        
        # Welcome message
        draw_text("Welcome to Chess Game", font, screen, (255, 255, 255), (screen.get_width() // 2, 100))
        
        if button_visible:
            # Draw the "Play" button
            button_x = (screen.get_width() - button_width) // 2
            button_y = (screen.get_height() // 2) - (button_height // 2)  # Centered vertically
            button_rect = p.Rect(button_x, button_y, button_width, button_height)  # Rectangle for the button
            p.draw.rect(screen, button_color, button_rect)  # Draw the rectangle
            draw_text(button_text, button_font, screen, (0, 0, 0), (button_x + button_width // 2, button_y + 25))  # Button text

        if show_options:  # Only if "Play" has been clicked
            # Draw additional text and store the rectangles
            draw_text("Choose your opponent:", font, screen, (255, 255, 255), (screen.get_width() // 2, 200))
            play_ai_rect = draw_text("1. Play against AI", font, screen, (255, 255, 255), (screen.get_width() // 2, 300))
            play_player_rect = draw_text("2. Play against another player", font, screen, (255, 255, 255), (screen.get_width() // 2, 400))

        for event in p.event.get():
            if event.type == p.QUIT:
                running = False
                player_choice = None
            elif event.type == p.MOUSEBUTTONDOWN:
                if button_rect and button_rect.collidepoint(event.pos):# Clicked on "Play"
                    button_visible = False  # Hide the "Play" button
                    show_options = True  # Show options after clicking "Play"
                
                 # Detect if the click was on the AI or player option
                if show_options:  # Ensure that `play_ai_rect` is valid before checking
                    if play_ai_rect and play_ai_rect.collidepoint(event.pos):  # Clicked on "Play against AI"
                        player_choice = "ai"
                        running = False
                    elif play_player_rect and play_player_rect.collidepoint(event.pos):  # Clicked on "Play against another player"
                        player_choice = "player"
                        running = False

                elif event.type == p.KEYDOWN:
                    if event.key == p.K_1:  # Pressed key '1'
                        player_choice = "ai"
                        running = False
                    elif event.key == p.K_2:    # Pressed key '2'
                        player_choice = "player"
                        running = False
                        
        p.display.flip()

    # p.quit()
    return player_choice

def draw_text(text, font, surface, color, position):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()  # Get the rectangle representing the text
    text_rect.center = position  # Center it at the specified position
    surface.blit(text_obj, text_rect)  # Draw the text on the surface
    return text_rect  # Return the rectangle to check for collisions