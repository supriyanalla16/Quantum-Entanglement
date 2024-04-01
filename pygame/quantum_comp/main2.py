import pygame
import sys

# Initialize pygame
pygame.init()

button_width, button_height = 100, 50

# Create a pygame.Rect object that represents the button's boundaries
button_x, button_y = 10, 10
button_rect = pygame.Rect(button_x, button_y, button_width, button_height)

# Create a surface for the button
button_surface = pygame.Surface((button_width, button_height))

# Draw the button's text and border on the surface
pygame.draw.rect(button_surface, "red", (0, 0, button_width, button_height))

# Create a font object
font = pygame.font.Font('freesansbold.ttf', 20)

# Render the text and draw it on the button_surface
text_surface = font.render("Click Me!", True, (255, 255, 255))
text_x = (button_width - text_surface.get_width()) // 2
text_y = (button_height - text_surface.get_height()) // 2
button_surface.blit(text_surface, (text_x, text_y))



# Set up the display
screen_width, screen_height = 1000, 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Button Demo")

# running="True"
# while running:
# Start the main loop
while True:
    
    # screen.fill((255, 255, 255))

    # Draw the button on the screen
    screen.blit(button_surface, (button_x, button_y))


    # Get events from the event queue
    for event in pygame.event.get():
        # Check for the quit event
        if event.type == pygame.QUIT:
            # Quit the game
            # pygame.quit()
            sys.exit()
            # if(event.type==pygame.QUIT):
            # running=False

        # Check for the mouse button down event
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Call the on_mouse_button_down() function
            if button_rect.collidepoint(event.pos):
                print("Button clicked!")

    # Update the display
    pygame.display.update()
