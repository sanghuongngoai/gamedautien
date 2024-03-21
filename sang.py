import pygame
pygame.init()
screen = pygame.display.set_mode((1280,700))
running = True

bg = pygame.image.load(r'anhr\background.jpg')
tl = pygame.image.load(r'anhr\triangel.png')
hm = pygame.image.load(r'anhr\human.png')

y_n = 2.5
jump = False
bg_x = 0
x_n =2
bg_x,bg_y = 0,0
tl_x,tl_y = 1000,500
hm_x,hm_y = 100,540
gp = True

def vc():
	if hm_hcn.colliderect(tl_hcn):		
		return False
	return True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				if gp:
					if hm_y == 540:
						jump = True
			if event.key == pygame.K_SPACE:
				if gp == False:
					gp = True
	if gp:
		bg_hcn = screen.blit(bg,(bg_x,bg_y))
		bg_x -= x_n
		bg2_hcn = screen.blit(bg,(bg_x+1280,bg_y))
		if bg_x == -1280:
			bg_x = 0
		
		
		tl_hcn = screen.blit(tl,(tl_x,tl_y))
		tl_x -= x_n
		if tl_x == -130:
			tl_x = 1000
		hm_hcn = screen.blit(hm,(hm_x,hm_y))
		if hm_y >= 300: 
			if jump:
				hm_y -= y_n
		else:
			jump = False
		if hm_y < 540:
			if jump == False:
				hm_y += y_n
		gp = vc()
	if gp == False:
		bg_x,bg_y = 0,0
		tl_x,tl_y = 1000,500
		hm_x,hm_y = 100,540
	
		bg_hcn = screen.blit(bg,(bg_x,bg_y))
		tl_hcn = screen.blit(tl,(tl_x,tl_y))
		hm_hcn = screen.blit(hm,(hm_x,hm_y))
	
	pygame.display.update()
