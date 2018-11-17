import pygame
import sys
		
def run_game():
	
	pygame.init()
	screen = pygame.display.set_mode((1000,700))
	bg_color = (200,55,55)
	
	while True:		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
 
    screen.fill(bg_color)
 
    pygame.display.flip()
	
run_game()
