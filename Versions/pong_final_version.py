
# Kevin Yang K.Y, Christopher Noce C.N, Kevin Huang K.H
import pygame  
import random
import pygame_menu
from pygame_menu import themes
from spyder.utils.color_system import Green

pygame.init()  

# Font that is used to render the text
font20 = pygame.font.Font('freesansbold.ttf',
                          20)  
font15 = pygame.font.Font('freesansbold.ttf',
                          15)
font25 = pygame.font.Font('freesansbold.ttf',
                          25)

# RGB values of standard colors
BLACK = (0, 0, 0)  
WHITE = (255, 255, 255)  
GREEN = (0, 255, 0)  

# Basic parameters of the screen
WIDTH, HEIGHT = 900, 600 
screen = pygame.display.set_mode((WIDTH, HEIGHT))  
pygame.display.set_caption("Pong")  

clock = pygame.time.Clock()  
FPS = 30  


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
        self.geekRect = pygame.Rect(posx, posy, width,
                                    height)  
        # Object that is blit on the screen
        self.geek = pygame.draw.rect(screen, self.color, self.geekRect)  

    # Used to display the object on the screen
    def display(self):  
        self.geek = pygame.draw.rect(screen, self.color, self.geekRect)  

    def update(self, yFac):  
        self.posy = self.posy + self.speed * yFac  

        # Restricting the striker to be below the top surface of the screen
        if self.posy <= 0:  
            self.posy = 0 
        # Restricting the striker to be above the bottom surface of the screen
        elif self.posy + self.height >= HEIGHT:  
            self.posy = HEIGHT - self.height  

        # Updating the rect with the new values
        self.geekRect = (self.posx, self.posy, self.width, self.height)  

    def displayScore(self, text, score, x, y, color):  
        text = font20.render(text + str(score), True, color)  
        textRect = text.get_rect()  
        textRect.center = (x, y)  
        screen.blit(text, textRect)  

    def getRect(self):  
        return self.geekRect  


# Ball class


class Ball:  
    def __init__(self, posx, posy, radius, speed,
                 color):  
        self.posx = posx  
        self.posy = posy  
        self.radius = radius  
        self.speed = speed  
        self.color = color  
        self.xFac = 1  
        self.yFac = -1  
        self.ball = pygame.draw.circle(
            screen, self.color, (self.posx, self.posy),
            self.radius)   
        self.firstTime = 1

    def display(self):  
        self.ball = pygame.draw.circle(
            screen, self.color, (self.posx, self.posy),
            self.radius) 

    def update(self):  
        self.posx += self.speed * self.xFac 
        self.posy += self.speed * self.yFac  
        if (self.posx >= WIDTH // 2 and self.xFac > 0) or (self.posx <= WIDTH // 2 and self.xFac < 0):
            self.color = WHITE

        # If the ball hits the top or bottom surfaces,
        # then the sign of yFac is changed and
        # it results in a reflection
        if self.posy <= 0 or self.posy >= HEIGHT:  
            self.yFac *= -1  

        if self.posx <= 0 and self.firstTime:  
            self.firstTime = 0  
            return 1  
        elif self.posx >= WIDTH and self.firstTime:  
            self.firstTime = 0  
            return -1  
        else:  
            return 0  

    def reset(
            self):  
        self.posx = WIDTH // 2  
        self.posy = HEIGHT // 2  
        self.xFac = random.randrange(-1, 2, 2) 
        self.firstTime = 1  
        self.color = WHITE

    # Used to reflect the ball along the X-axis
    def hit(self):  
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

    def getRect(self):  
        return self.ball  


class Games():
    def game():
        running = True  
        
        background = pygame.image.load('pong_background_resized.png')  
        background_music = pygame.mixer.Sound('background_music.mp3')
        end_music = pygame.mixer.Sound('Celebration Sound Effect.mp3')

    # Defining the objects
        geek1 = Striker(20, 0, 10, 100, 10, GREEN)
        geek2 = Striker(WIDTH - 30, 0, 10, 100, 10, GREEN)

        ball = Ball(WIDTH // 2, HEIGHT // 2, 7, 7, WHITE)

        listOfGeeks = [geek1, geek2]

    # Initial parameters of the players
        geek1Score, geek2Score = 0, 0
        geek1YFac, geek2YFac = 0, 0  

        while running:  
            screen.blit(background, (0, 0))  
            background_music.play() 

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
                
            if geek1Score == 9: #1 point from winning
                geek2.height = 200  # increases the height of geek2's paddle (makes the game easier as they are 1 point from losing
                geek2.geekRect = pygame.Rect(geek2.posx, geek2.posy, geek2.width, geek2.height) # collisions
            elif geek2Score == 9:
                geek1.height = 200  # increases the height of geek1's paddle
                geek1.geekRect = pygame.Rect(geek1.posx, geek1.posy, geek1.width, geek1.height) # collisions
                
            if geek1Score == 10:
                background_music.stop()
                end_music.play()
                Games.end_screen1()
            elif geek2Score == 10:
                background_music.stop()
                end_music.play()
                Games.end_screen2()


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
            for event in pygame.event.get():  #checks each event in the list
                if event.type == pygame.QUIT:
                    freeze_screen = False 
                    main() # Exits the while loop/game when game window is closed
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
            for event in pygame.event.get():  #checks each event in the list
                if event.type == pygame.QUIT:
                    freeze_screen = False 
                    main() #Exits the while loop/game when game window is closed
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
        background = pygame.image.load('pong_background_resized.png')

    # Defining the objects
        geek1 = Striker(20, 0, 10, 250, 10, WHITE)
        geek2 = Striker(WIDTH - 30, 0, 10, 100, 10, WHITE)
        ball = Ball(WIDTH // 2, HEIGHT // 2, 7, 7, WHITE)

        listOfGeeks = [geek1, geek2]

    # Initial parameters of the players
        geek1Score, geek2Score = 0, 0
        geek1YFac, geek2YFac = 0, 0

        while running:
            screen.blit(background, (0,0))

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
                
            for event in pygame.event.get():  # checks each event in the list
                if event.type == pygame.QUIT:
                    running = False  # Exits the while loop/game when game window is closed
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