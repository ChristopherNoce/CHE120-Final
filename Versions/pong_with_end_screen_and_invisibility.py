
# Kevin Yang K.Y, Christopher Noce C.N, Kevin Huang K.H
import pygame  # C.N - imports the pygame module. The features on pygame are what make this game playable/possible. Just regular python does not have these capabilities.
import random
import pygame_menu
from pygame_menu import themes

pygame.init()  # C.N - this initializes the pygame modules, including font, sounds, and display.

# Font that is used to render the text
font20 = pygame.font.Font('freesansbold.ttf',
                          20)  # C.N - this sets the font and style that will be used for the text in the gam
font15 = pygame.font.Font('freesansbold.ttf',
                          15)
font25 = pygame.font.Font('freesansbold.ttf',
                          25)

# RGB values of standard colors
BLACK = (0, 0, 0)  # CN RBG value for black
WHITE = (255, 255, 255)  # CN RGB vakue for white
GREEN = (0, 255, 0)  # CN RGB value that creates the green in game

# Basic parameters of the screen
WIDTH, HEIGHT = 900, 600  # CN dimensions of the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # CN Creates the game window using the dimensions listed abvoe
pygame.display.set_caption("Pong")  # CN title of window = "Pong"

clock = pygame.time.Clock()  # CN creates clock object to control the frame rate
FPS = 30  # CN sets the frames per second (FPS) - 30 frames per second means there are 30 still images (frames) displayed in a single second of animation. Higher fps = smoother and more fluid animations.


# Striker class


class Striker:  # CN defines striker class to represent a game paddel
    # Take the initial position, dimensions, speed and color of the object
    def __init__(self, posx, posy, width, height, speed, color):  # CN initializes the properties
        self.posx = posx  # CN x-coordinate of striker
        self.posy = posy  # CN y coordinate of striker
        self.width = width  # CN width of striker
        self.height = height  # CN height of striker
        self.speed = speed  # CN Speed of striker
        self.color = color  # CN colour of striker
        # Rect that is used to control the position and collision of the object
        self.geekRect = pygame.Rect(posx, posy, width,
                                    height)  # CN Rect object (store and manipulate rectangular area) to define position and collision area
        # Object that is blit on the screen
        self.geek = pygame.draw.rect(screen, self.color, self.geekRect)  # CN drwaing the striker on the screen

    # Used to display the object on the screen
    def display(self):  # CN method to display the striker
        self.geek = pygame.draw.rect(screen, self.color, self.geekRect)  # CN drawing the strikers rectangle

    def update(self, yFac):  # CN method to update striker's position based on user-inputted movement
        self.posy = self.posy + self.speed * yFac  # CN adjusts y coordinate based on speed and direction

        # Restricting the striker to be below the top surface of the screen
        if self.posy <= 0:  # CN sets boundary
            self.posy = 0  # ensures that they cannot move past the top edge
        # Restricting the striker to be above the bottom surface of the screen
        elif self.posy + self.height >= HEIGHT:  # CN sets boundary
            self.posy = HEIGHT - self.height  # CN ensures striker does not pass the bottom

        # Updating the rect with the new values
        self.geekRect = (self.posx, self.posy, self.width, self.height)  # CN updates the rectangle with new position

    def displayScore(self, text, score, x, y, color):  # CN method to display the score on the screen
        text = font20.render(text + str(score), True, color)  # CN sets score text colour
        textRect = text.get_rect()  # CN rectangle will go around the text and enclose it
        textRect.center = (x, y)  # CN setting position of the text rectangle
        screen.blit(text, textRect)  # CN displays text on screen

    def getRect(self):  # CN method to retrieve the striker's current rectangle for collision detection
        return self.geekRect  # CN returns the rect object


# Ball class


class Ball:  # K.H A new class "Ball" is being defined.
    def __init__(self, posx, posy, radius, speed,
                 color):  # K.H "__init__" is a method that initializes certain characteristics for the game ball within Pong.
        self.posx = posx  # K.H Assigns the value of posx (position along x-axis) to self.posx which is the x-position characteristic of the ball object.
        self.posy = posy  # K.H Assigns the value of posy (position along y-axis) to self.posy which is the y-position characteristic of the ball object.
        self.radius = radius  # K.H Assigns the value of radius (radius of the ball) to self.radius which is the radius characteristic of the ball object.
        self.speed = speed  # K.H Assigns the value of speed (speed of the ball) to self.speed which is the speed characteristic of the ball object.
        self.color = color  # K.H Assigns the value of color (colour of the ball) to self.color which is the colour characteristic of the ball object.
        self.xFac = 1  # K.H Assigns the arbitrary value of 1 to self.xFac which is the ball's movement along the x-axis, left or right.
        self.yFac = -1  # K.H Assigns the arbitrary value of -1 to self.yFac which is the ball's movement along the y-axis, up or down.
        self.ball = pygame.draw.circle(
            screen, self.color, (self.posx, self.posy),
            self.radius)  # K.H Uses a pygame method to draw the ball on the screen, with a specified colour and radius, and also the ball's initial position along the y-axis and x-axis.
        self.firstTime = 1  # K.H Assigns the value of 1 to self.firstTime, which is a way of tracking if the ball hit one of the left/right sides of the screen for the first time, which can be seen below.

    def display(self):  # K.H A function "display" is created to display the game ball.
        self.ball = pygame.draw.circle(
            screen, self.color, (self.posx, self.posy),
            self.radius)  # K.H Uses a pygame method to draw the ball on the screen, with a specified colour and radius, and also the ball's initial position along the y-axis and x-axis.

    def update(self):  # K.H A function "update" is created which seems to update the x and y position of the ball.
        self.posx += self.speed * self.xFac  # K.H The position of the ball on the x-axis is updated to be relative to the speed of the ball multiplied by the arbitrary factor of the ball along the x-axis.
        self.posy += self.speed * self.yFac  # K.H The position of the ball on the y-axis is updated to be relative to the speed of the ball multiplied by the arbitrary factor of the ball along the y-axis.
        if (self.posx >= WIDTH // 2 and self.xFac > 0) or (self.posx <= WIDTH // 2 and self.xFac < 0):
            self.color = WHITE

        # If the ball hits the top or bottom surfaces,
        # then the sign of yFac is changed and
        # it results in a reflection
        if self.posy <= 0 or self.posy >= HEIGHT:  # K.H Conditional statement seeing if the y-position of the ball is less than or equal to zero (hits the bottom of the screen) or if the y-position is greater than or equal to the height (hits the top of the screen).
            self.yFac *= -1  # K.H If the conditional statement is satisfied, the arbitrary factor in the y-direction is multiplied by -1 and effectively flipped so the ball goes in the opposite direction.

        if self.posx <= 0 and self.firstTime:  # K.H Conditional statement seeing if the x-position of the ball is less than or equal to zero (hits the left side of the screen) and if it is the first time that the ball has done so (any value other than 0 is associated with the boolean True).
            self.firstTime = 0  # K.H If the conditional statement is satisfied, self.firstTime is assigned the value of 0, which is associated with the boolean False.
            return 1  # K.H If the conditional statement is satisfied, the value of 1 is also returned for this function.
        elif self.posx >= WIDTH and self.firstTime:  # K.H Conditional statement seeing if the x-position of the ball is greater than or equal to the width (hits the right side of the screen) and if it is the first time that the ball has done so (any value other than 0 is associated with the boolean True).
            self.firstTime = 0  # K.H If the conditional statement is satisfied, self.firstTime is assigned the value of 0, which is associated with the boolean False.
            return -1  # K.H If the conditional statement is satisfied, the value of -1 is also returned for this function.
        else:  # K.H Conditional statement that only runs if none of the three conditional statements above are satisfied.
            return 0  # K.H If the else statement is run, then this line returns the value of 0 to the function.

    def reset(
            self):  # K.H A function "reset" is created which seems to reset the ball, presumably every time when a player scores.
        self.posx = WIDTH // 2  # K.H The x-position of the ball is reset into the middle of the screen (since the width of the screen divided by 2 is half the screen from left to right).
        self.posy = HEIGHT // 2  # K.H The y-position of the ball is reset into the middle of the screen (since the height of the screen divided by 2 is half the screen from up to down).
        self.xFac = random.randrange(-1, 2, 2)  # K.H The arbitrary factor in the x-direction is multiplied by the value of -1, meaning that the ball's direction in the x-direction will go the opposite way than before it was reset.
        self.firstTime = 1  # K.H self.firstTime is assigned the value of 1 again, effectively setting its boolean value to True and resetting it its value before the ball hit the end sides of the screen.
        self.color = WHITE

    # Used to reflect the ball along the X-axis
    def hit(self):  # K.H A function "hit" is created which seems to show what happens when the ball is hit by a player's paddle.
        self.randFac = random.randint(1, 3)
        self.invisibility = random.randint(1, 4)
        if self.xFac > 0:
            self.xFac = -self.randFac
            
            if self.invisibility == 1:
                self.color = BLACK
                
        elif self.xFac < 0:
            self.xFac = self.randFac
    
            if self.invisibility == 1:
                self.color = BLACK
       # K.H The arbitrary factor in the x-direction is multiplied by the value of -1, which flips the x-direction that the ball is moving in.

    def getRect(self):  # K.H A function "getRect" is created.
        return self.ball  # K.H self.ball is returned whenever this function is called.


class Games():
    def game():
        running = True  # K.Y: Initializing the running variable to True so that the while loop below runs
        
        background = pygame.image.load('pong_background_resized.png')  # CN loading background image
        background_music = pygame.mixer.Sound('background_music.mp3')

    # Defining the objects
    # K.Y: x, y, width, height, speed, colour
        geek1 = Striker(20, 0, 10, 100, 10, GREEN)
        geek2 = Striker(WIDTH - 30, 0, 10, 100, 10, GREEN)
    # K.Y: x, y, radius, speed, colour
        ball = Ball(WIDTH // 2, HEIGHT // 2, 7, 7, WHITE)

    # K.Y: List of the players
        listOfGeeks = [geek1, geek2]

    # Initial parameters of the players
        geek1Score, geek2Score = 0, 0
        geek1YFac, geek2YFac = 0, 0  # K.Y: YFac is explained in the following comments

        while running:  # K.Y: While the game is running/tab is open
            screen.blit(background, (0, 0))  # CN renders the background image
            background_music.play() #plays music

            # Event handling
        # K.Y: pygame.event.get() creates a list of events (mouse movements, keyboard inputs, etc)
        # K.Y: YFac is used to update the position of the strikers
        # K.Y: Top of the screen is y = 0, bottom is y = 600
        # K.Y: Position is updated by adding speed*YFac to the current position
        # K.Y: Negative YFac moves the striker up, positive YFac moves the striker down
            for event in pygame.event.get():  # K.Y: checks each event in the list
                if event.type == pygame.QUIT:
                    running = False  # K.Y: Exits the while loop/game when game window is closed
                if event.type == pygame.KEYDOWN:  # K.Y: When the key is pressed down
                # K.Y: the following 2 if statements set geek2YFac to -1 (up arrow) or 1 (down arrow)
                    if event.key == pygame.K_UP:
                        geek2YFac = -1
                    if event.key == pygame.K_DOWN:
                        geek2YFac = 1
                # K.Y: the following 2 if statements set geek1YFac to -1 (w key) or 1 (s key)
                    if event.key == pygame.K_w:
                        geek1YFac = -1
                    if event.key == pygame.K_s:
                        geek1YFac = 1
                if event.type == pygame.KEYUP:  # K.Y: When the respective keys are released the YFac of geek1/2 is set to 0 meaning the striker's position will not change
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:  # K.Y: If up arrow or down arrow is released
                        geek2YFac = 0
                    if event.key == pygame.K_w or event.key == pygame.K_s:  # K.Y: If 'w' or 's' key is released
                        geek1YFac = 0

        # Collision detection
        # K.Y: Gets the position of each geek and the ball, and checks if they have collided
        # K.Y: If they have collided, calls the ball.hit() function which reverses the left/right direction of the ball
            for geek in listOfGeeks:
                if pygame.Rect.colliderect(ball.getRect(), geek.getRect()):
                    ball.hit()

        # Updating the objects
        # K.Y: with the YFacs described above
            geek1.update(geek1YFac)
            geek2.update(geek2YFac)
            point = ball.update()  # K.Y: ball.update() returns 1 or -1 if the ball x position is at or beyond the end of the window (0,900), 0 otherwise

        # -1 -> Geek_1 has scored
        # +1 -> Geek_2 has scored
        # 0 -> None of them scored
            if point == -1:
                geek1Score += 1
            elif point == 1:
                geek2Score += 1
                
            if geek1Score == 10:
                background_music.stop()
                Games.end_screen1()
            elif geek2Score == 10:
                background_music.stop()
                Games.end_screen2()


        # Someone has scored
        # a point and the ball is out of bounds.
        # So, we reset it's position
            if point:
            # K.Y: Calls upon the reset method in the ball class to set ball position to center of screen
                ball.reset()
            
        # Displaying the objects on the screen
            geek1.display()
            geek2.display()
            ball.display()

        # Displaying the scores of the players
            geek1.displayScore("Geek_1 : ",
                            geek1Score, 100, 20, WHITE)
            geek2.displayScore("Geek_2 : ",
                            geek2Score, WIDTH - 100, 20, WHITE)

            pygame.display.update()

            clock.tick(FPS)  # K.Y: Rate at which the while loop runs
    # K.Y: Since FPS is defined as 30 at the top of the program, the loop will run 30 times per second
    
    def end_screen1(): #Player 1 wins
        freeze_screen = True
        x_size = 200
        y_size = 200

        win_screen = pygame.image.load('win_screen.png')
        resized_win = pygame.transform.scale(win_screen, (x_size, y_size))
        lose_screen = pygame.image.load('lose_screen.png')
        resized_lose = pygame.transform.scale(lose_screen, (x_size, y_size))
        play_again = font25.render("Play again? (Y/N)", WHITE, WHITE)
        rectangle_for_centering_question = play_again.get_rect()
        rectangle_for_centering_question.center = (WIDTH // 2, HEIGHT // 2)

        while freeze_screen:
   
            screen.blit(play_again, rectangle_for_centering_question)
            screen.blit(resized_win, (WIDTH // 4 - 0.5*x_size, HEIGHT // 2 - 0.5*y_size))
            screen.blit(resized_lose, (WIDTH // 4 * 3 - 0.5*x_size, HEIGHT // 2 - 0.5*y_size))
            for event in pygame.event.get():  # K.Y: checks each event in the list
                if event.type == pygame.QUIT:
                    freeze_screen = False 
                    main() # K.Y: Exits the while loop/game when game window is closed
                if event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_n:
                        freeze_screen = False
                        main()
                    elif event.key == pygame.K_y:
                        freeze_screen = False
                        Games.game()
            pygame.display.update()

            clock.tick(FPS)
                    
    def end_screen2(): #Player 2 wins
        freeze_screen = True
        x_size = 200
        y_size = 200

        win_screen = pygame.image.load('win_screen.png')
        resized_win = pygame.transform.scale(win_screen, (x_size, y_size))
        lose_screen = pygame.image.load('lose_screen.png')
        resized_lose = pygame.transform.scale(lose_screen, (x_size, y_size))
        play_again = font25.render("Play again? (Y/N)", WHITE, WHITE)
        rectangle_for_centering_question = play_again.get_rect()
        rectangle_for_centering_question.center = (WIDTH // 2, HEIGHT // 2)

        while freeze_screen:

            screen.blit(play_again, rectangle_for_centering_question)
            screen.blit(resized_win, (WIDTH // 4 * 3 - 0.5*x_size, HEIGHT // 2 - 0.5*y_size))
            screen.blit(resized_lose, (WIDTH // 4 - 100, HEIGHT // 2 -100))
            for event in pygame.event.get():  # K.Y: checks each event in the list
                if event.type == pygame.QUIT:
                    freeze_screen = False 
                    main() # K.Y: Exits the while loop/game when game window is closed
                if event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_n:
                        freeze_screen = False
                        main()
                    elif event.key == pygame.K_y:
                        freeze_screen = False
                        Games.game()
            pygame.display.update()

            clock.tick(FPS)


    def game1():
        running = True

    # Defining the objects
        geek1 = Striker(20, 0, 10, 250, 10, WHITE)
        geek2 = Striker(WIDTH - 30, 0, 10, 100, 10, WHITE)
        ball = Ball(WIDTH // 2, HEIGHT // 2, 7, 7, WHITE)

        listOfGeeks = [geek1, geek2]

    # Initial parameters of the players
        geek1Score, geek2Score = 0, 0
        geek1YFac, geek2YFac = 0, 0

        while running:
            screen.fill(BLACK)

        # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
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
                ball.reset()

            # Displaying the objects on the screen
            geek1.display()
            geek2.display()
            ball.display()

            # Displaying the scores of the players
            geek1.displayScore("Geek_1 : ",
                               geek1Score, 100, 20, WHITE)
            geek2.displayScore("Geek_2 : ",
                               geek2Score, WIDTH - 100, 20, WHITE)

            pygame.display.update()

            clock.tick(FPS)

        # K.Y: Game manager
        
class Rules():
    def rules():
        running = True
        rules_list = ["Welcome to Pong!", "1. First player to 10 wins.", "2. The ball will randomly speed up or slow down after each hit.", \
                      "3. Once in a while, the ball will become invisible until the center line after a hit.", \
                          "4. Player 1 uses 'W' and 'S' keys to control their paddle, and Player 2 uses the up/down arrow keys.", \
                              "5. Press 'Q' to exit this screen and start playing!"]
        
        while running:
            screen.fill(BLACK)
            
            spacing = -(HEIGHT//2)//(0.5*len(rules_list))
            for rule in rules_list:
                text = font15.render(rule, WHITE, WHITE)
                rectangle_for_centering_text = text.get_rect()
                rectangle_for_centering_text.center = (WIDTH // 2, HEIGHT // 2 + spacing)
                screen.blit(text, rectangle_for_centering_text)
                spacing += 50
                
            for event in pygame.event.get():  # K.Y: checks each event in the list
                if event.type == pygame.QUIT:
                    running = False  # K.Y: Exits the while loop/game when game window is closed
                if event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_q:
                        running = False
            pygame.display.update()

            clock.tick(FPS)


name1 = ['username','username']
def getNames1(name):
    name1[0] = name

def getNames2(name):
    name1[1] = name

def main():
    mainmenu = pygame_menu.Menu('Welcome', WIDTH, HEIGHT, theme=themes.THEME_DARK)

    mainmenu.add.text_input('Name 1: ', default=name1[0], maxchar=20, onchange = getNames1)
    mainmenu.add.text_input('Name 2: ', default=name1[1], maxchar=20, onchange = getNames2)

    # K.Y: Add comments later
    mainmenu.add.button('Mode 1', Games.game)
    mainmenu.add.button('Mode 2', Games.game1)
    mainmenu.add.button('Quit', pygame_menu.events.EXIT)
    mainmenu.add.button("Rules", Rules.rules)

    mainmenu.mainloop(screen)


if __name__ == "__main__":
    main()
    pygame.quit()
