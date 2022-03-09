import pygame
  
def game():
	pygame.init()
	  

	surface = pygame.display.set_mode((400,300))
	  

	color = (255,0,0)  
	pygame.draw.rect(surface, color, pygame.Rect(30, 30, 60, 60))
	pygame.display.flip()
	running = True
	while running:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				running=False
				pygame.quit()
	
game()