#Kevin Yang K.Y, Christopher Noce C.N, Kevin Huang K.H
import pygame #C.N - imports the pygame module. The features on pygame are what make this game playable/possible. Just regular python does not have these capabilities.

pygame.init() #C.N - this initializes the pygame modules, including font, sounds, and display. 

# Font that is used to render the text
font20 = pygame.font.Font('freesansbold.ttf', 20) #C.N - this sets the font and style that will be used for the text in the game

# RGB values of standard colors
BLACK = (0, 0, 0) #CN RBG value for black
WHITE = (255, 255, 255) #CN RGB vakue for white 
GREEN = (0, 255, 0) #CN RGB value that creates the green in game

# Basic parameters of the screen
WIDTH, HEIGHT = 900, 600 #CN dimensions of the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT)) #CN Creates the game window using the dimensions listed abvoe
pygame.display.set_caption("Pong") #CN title of window = "Pong"

clock = pygame.time.Clock() #CN creates clock object to control the frame rate
FPS = 30 #CN sets the frames per second (FPS) - 30 frames per second means there are 30 still images (frames) displayed in a single second of animation. Higher fps = smoother and more fluid animations.

# Striker class


class Striker:
		# Take the initial position, dimensions, speed and color of the object
	def __init__(self, posx, posy, width, height, speed, color):
		self.posx = posx
		self.posy = posy
		self.width = width
		self.height = height
		self.speed = speed
		self.color = color
		# Rect that is used to control the position and collision of the object
		self.geekRect = pygame.Rect(posx, posy, width, height)
		# Object that is blit on the screen
		self.geek = pygame.draw.rect(screen, self.color, self.geekRect)

	# Used to display the object on the screen
	def display(self):
		self.geek = pygame.draw.rect(screen, self.color, self.geekRect)

	def update(self, yFac):
		self.posy = self.posy + self.speed*yFac

		# Restricting the striker to be below the top surface of the screen
		if self.posy <= 0:
			self.posy = 0
		# Restricting the striker to be above the bottom surface of the screen
		elif self.posy + self.height >= HEIGHT:
			self.posy = HEIGHT-self.height

		# Updating the rect with the new values
		self.geekRect = (self.posx, self.posy, self.width, self.height)

	def displayScore(self, text, score, x, y, color):
		text = font20.render(text+str(score), True, color)
		textRect = text.get_rect()
		textRect.center = (x, y)

		screen.blit(text, textRect)

	def getRect(self):
		return self.geekRect

# Ball class


class Ball: #K.H A new class "Ball" is being defined.
	def __init__(self, posx, posy, radius, speed, color): #K.H "__init__" is a method that initializes certain characteristics for the game ball within Pong.
		self.posx = posx #K.H Assigns the value of posx (position along x-axis) to self.posx which is the x-position characteristic of the ball object. 
		self.posy = posy #K.H Assigns the value of posy (position along y-axis) to self.posy which is the y-position characteristic of the ball object. 
		self.radius = radius #K.H Assigns the value of radius (radius of the ball) to self.radius which is the radius characteristic of the ball object.
		self.speed = speed #K.H Assigns the value of speed (speed of the ball) to self.speed which is the speed characteristic of the ball object.
		self.color = color #K.H Assigns the value of color (colour of the ball) to self.color which is the colour characteristic of the ball object. 
		self.xFac = 1 #K.H Assigns the arbitrary value of 1 to self.xFac which is the ball's movement along the x-axis, left or right.
		self.yFac = -1 #K.H Assigns the arbitrary value of -1 to self.yFac which is the ball's movement along the y-axis, up or down.
		self.ball = pygame.draw.circle(
			screen, self.color, (self.posx, self.posy), self.radius) #K.H Uses a pygame method to draw the ball on the screen, with a specified colour and radius, and also the ball's initial position along the y-axis and x-axis.
		self.firstTime = 1 #K.H Assigns the value of 1 to self.firstTime, which is a way of tracking if the ball hit one of the left/right sides of the screen for the first time, which can be seen below.

	def display(self): #K.H A function "display" is created to display the game ball. 
		self.ball = pygame.draw.circle(
			screen, self.color, (self.posx, self.posy), self.radius) #K.H Uses a pygame method to draw the ball on the screen, with a specified colour and radius, and also the ball's initial position along the y-axis and x-axis.

	def update(self): #K.H A function "update" is created which seems to update the x and y position of the ball. 
		self.posx += self.speed*self.xFac #K.H The position of the ball on the x-axis is updated to be relative to the speed of the ball multiplied by the arbitrary factor of the ball along the x-axis.
		self.posy += self.speed*self.yFac #K.H The position of the ball on the y-axis is updated to be relative to the speed of the ball multiplied by the arbitrary factor of the ball along the y-axis.

		# If the ball hits the top or bottom surfaces, 
		# then the sign of yFac is changed and 
		# it results in a reflection
		if self.posy <= 0 or self.posy >= HEIGHT: #K.H Conditional statement seeing if the y-position of the ball is less than or equal to zero (hits the bottom of the screen) or if the y-position is greater than or equal to the height (hits the top of the screen).
			self.yFac *= -1 #K.H If the conditional statement is satisfied, the arbitrary factor in the y-direction is multiplied by -1 and effectively flipped so the ball goes in the opposite direction.

		if self.posx <= 0 and self.firstTime: #K.H Conditional statement seeing if the x-position of the ball is less than or equal to zero (hits the left side of the screen) and if it is the first time that the ball has done so (any value other than 0 is associated with the boolean True).
			self.firstTime = 0 #K.H If the conditional statement is satisfied, self.firstTime is assigned the value of 0, which is associated with the boolean False.
			return 1 #K.H If the conditional statement is satisfied, the value of 1 is also returned for this function.
		elif self.posx >= WIDTH and self.firstTime: #K.H Conditional statement seeing if the x-position of the ball is greater than or equal to the width (hits the right side of the screen) and if it is the first time that the ball has done so (any value other than 0 is associated with the boolean True).
			self.firstTime = 0 #K.H If the conditional statement is satisfied, self.firstTime is assigned the value of 0, which is associated with the boolean False.
			return -1 #K.H If the conditional statement is satisfied, the value of -1 is also returned for this function.
		else: #K.H Conditional statement that only runs if none of the three conditional statements above are satisfied.
			return 0 #K.H If the else statement is run, then this line returns the value of 0 to the function.

	def reset(self): #K.H A function "reset" is created which seems to reset the ball, presumably every time when a player scores.
		self.posx = WIDTH//2 #K.H The x-position of the ball is reset into the middle of the screen (since the width of the screen divided by 2 is half the screen from left to right).
		self.posy = HEIGHT//2 #K.H The y-position of the ball is reset into the middle of the screen (since the height of the screen divided by 2 is half the screen from up to down).
		self.xFac *= -1 #K.H The arbitrary factor in the x-direction is multiplied by the value of -1, meaning that the ball's direction in the x-direction will go the opposite way than before it was reset.
		self.firstTime = 1 #K.H self.firstTime is assigned the value of 1 again, effectively setting its boolean value to True and resetting it its value before the ball hit the end sides of the screen.

	# Used to reflect the ball along the X-axis
	def hit(self): #K.H A function "hit" is created which seems to show what happens when the ball is hit by a player's paddle.
		self.xFac *= -1 #K.H The arbitrary factor in the x-direction is multiplied by the value of -1, which flips the x-direction that the ball is moving in.

	def getRect(self): #K.H A function "getRect" is created.
		return self.ball #K.H self.ball is returned whenever this function is called.

# Game Manager


def main():
	running = True #K.Y: Initializing the running variable so that the while loop runs

	# Defining the objects
    #K.Y: x, y, width, height, speed, colour
	geek1 = Striker(20, 0, 10, 100, 10, GREEN) 
	geek2 = Striker(WIDTH-30, 0, 10, 100, 10, GREEN)
    #K.Y: x, y, radius, speed, colour
	ball = Ball(WIDTH//2, HEIGHT//2, 7, 7, WHITE)

    #K.Y: List of the players?
	listOfGeeks = [geek1, geek2]

	# Initial parameters of the players
	geek1Score, geek2Score = 0, 0
	geek1YFac, geek2YFac = 0, 0

	while running:
		screen.fill(BLACK) #K.Y: sets game background colour

		# Event handling
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False #K.Y: Exits the while loop/game ?when game window is closed?
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					geek2YFac = -1
				if event.key == pygame.K_DOWN:
					geek2YFac = 1
				if event.key == pygame.K_w:
					geek1YFac = -1
				if event.key == pygame.K_s:
					geek1YFac = 1
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					geek2YFac = 0
				if event.key == pygame.K_w or event.key == pygame.K_s:
					geek1YFac = 0

		# Collision detection
		for geek in listOfGeeks:
			if pygame.Rect.colliderect(ball.getRect(), geek.getRect()):
				ball.hit()

		# Updating the objects
		geek1.update(geek1YFac)
		geek2.update(geek2YFac)
		point = ball.update()

		# -1 -> Geek_1 has scored
		# +1 -> Geek_2 has scored
		# 0 -> None of them scored
		if point == -1:
			geek1Score += 1
		elif point == 1:
			geek2Score += 1

		# Someone has scored
		# a point and the ball is out of bounds.
		# So, we reset it's position
		if point:
            #K.Y: Calls upon the reset method in the ball class to set ball position to center of screen
			ball.reset() 

		# Displaying the objects on the screen
		geek1.display() 
		geek2.display()
		ball.display()

		# Displaying the scores of the players
		geek1.displayScore("Geek_1 : ", 
						geek1Score, 100, 20, WHITE)
		geek2.displayScore("Geek_2 : ", 
						geek2Score, WIDTH-100, 20, WHITE)

		pygame.display.update()
		clock.tick(FPS)	


if __name__ == "__main__":
	main()
	pygame.quit()
