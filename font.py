import pygame

class Font:
	def __init__(self):
		self.fonts = self.load_fonts()

	def load_fonts(self):
		chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '?', '.', ' ', '-', '!', ',', '\'']
		fonts = {}
		for i in chars:
			if i == '?':
				fonts[i] = pygame.image.load(f'Assets/fonts/q_mark.png')
				fonts[i] = pygame.transform.scale(fonts[i], (fonts[i].get_width()*4, fonts[i].get_height()*4))
			elif i == ' ':
				fonts[i] = pygame.Surface((30, 30))
			else:
				fonts[i] = pygame.image.load(f'Assets/fonts/{i}.png')
				fonts[i] = pygame.transform.scale(fonts[i], (fonts[i].get_width()*4, fonts[i].get_height()*4))

			fonts[i].set_colorkey((0, 0, 0))

		return fonts

	def render(self, text, disp, pos):
		text = text.upper()
		last_end_pos = pos[0]
		for l in text:
			disp.blit(self.fonts[l], (last_end_pos, pos[1]))
			last_end_pos += self.fonts[l].get_width()
