import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Oblique Highlighted Button")

# Colors
button_color = (100, 100, 100)
highlight_color = (200, 0, 0)

# Button dimensions
button_width, button_height = 200, 100
button_x, button_y = (width - button_width) // 2, (height - button_height) // 2

# User-specified angle and extent for the highlighted part
highlight_angle = math.radians(float(20))
highlight_extent = float(10)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get the mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Check if the mouse is over the highlighted part of the button
    highlighted = (
        (button_x <= mouse_x <= button_x + button_width) and
        (button_y <= mouse_y <= button_y + button_height) and
        (mouse_x - button_x) * math.sin(-highlight_angle) + (mouse_y - button_y) * math.cos(-highlight_angle) <= highlight_extent
    )

    # Draw the button as a polygon
    screen.fill((255, 255, 255))
    pygame.draw.polygon(screen, button_color, [
        (button_x, button_y),
        (button_x + button_width, button_y),
        (
            button_x + button_width - highlight_extent * math.sin(highlight_angle),
            button_y + highlight_extent * math.cos(highlight_angle)
        ),
        (button_x - highlight_extent * math.sin(highlight_angle), button_y + highlight_extent * math.cos(highlight_angle))
    ])

    # Draw the highlighted part with a different color
    if highlighted:
        pygame.draw.polygon(screen, highlight_color, [
            (button_x, button_y),
            (button_x + button_width, button_y),
            (
                button_x + button_width - highlight_extent * math.sin(highlight_angle),
                button_y + highlight_extent * math.cos(highlight_angle)
            ),
            (button_x - highlight_extent * math.sin(highlight_angle), button_y + highlight_extent * math.cos(highlight_angle))
        ])

    # Update the display
    pygame.display.flip()
