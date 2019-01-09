import pygame
import time
import random

pygame.init()

display_width = 600
display_height = 800

pause = False
black = (0, 0, 0)
white = (255, 255, 255)
red = (150, 0, 0)
bright_red = (255, 0, 0)
green = (0,150,0)
bright_green = (0,255,0)

# TODO: IMPORT ALL SOUNDS FOR IN GAME SOUNDS

block_color = (53,115,255)

car_width = 83
car_height = 52

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Flappy Truck')
clock = pygame.time.Clock()

carImg = pygame.image.load('flappy_truck_draw_pixel.png')

def things_dodged(count):
    font = pygame.font.Font('freesansbold.ttf', 75)
    text = font.render(str(count), True, red)
    gameDisplay.blit(text,(display_width/2,200))

def pipe_draw(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, 0, thingw, thingy])
    pygame.draw.rect(gameDisplay, color,
                     [thingx,
                      thingy + thingh,
                      thingw,
                      display_height - (thingy + thingh)])

# TODO: WRITE ALL SOUND HANDLING FUNCTIONS

def car(x, y):
    gameDisplay.blit(carImg, (x, y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',75)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

def button(msg, x, y, w, h, ic, ac, action=None):
    """
    button function for general button functionality on demand
    msg-button text;x-button x origin;y-button y origin;w-button width
    h-button height; ic-inactive button color;ac-active button color
    """
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x,y,w,h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x,y,w,h))

    smallText = pygame.font.Font('freesansbold.ttf', 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w/ 2)), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)

def unpause():
    global pause
    pause = False




# TODO: WRITE SOUND HANDLING CODE FOR ALL GAME LOOP TYPES AND ADD TO GAME LOOPS/LOOP FUNCTIONS
def paused():




    global pause

    while pause:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = False
                    unpause()

        gameDisplay.fill(white)



        largeText = pygame.font.SysFont('freesansbold.ttf',75)
        TextSurf, TextRect = text_objects("Paused", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)

        pipe_gap_starty = 200
        pipe_startx = display_width / 2
        pipe_width = 100
        pipe_gap_height = 400

        pipe_draw(pipe_startx, pipe_gap_starty, pipe_width, pipe_gap_height, black)

        button('Go Bro',100,display_height - 150,100,50,green,bright_green,unpause)
        button('No Bro',display_width - 150 - 100,display_height - 150,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)

def crash():
    largeText = pygame.font.SysFont('freesansbold.ttf',75)
    TextSurf, TextRect = text_objects('You Crashed', largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    while True:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        #gameDisplay.fill(white)

        button("Go bro",150,display_height - 150,100,50,green,bright_green,game_loop)

        button("No bro",display_width-150 - 100,display_height - 150,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)

def quitgame():
    pygame.quit()
    quit()





def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',75)
        TextSurf, TextRect = text_objects("Flappy Truck", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        mouse = pygame.mouse.get_pos()

        #print(mouse)

        button("Go bro",150,450,100,50,green,bright_green,game_loop)

        button("No bro",display_width-150-100,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)


def game_loop():

    x = (display_width * 0.5)
    y = (display_height * 0.5)

    y_pix_vel = 0
    y_pix_accel = 0.5

    pipe_startx = display_width + 50
    pipe_x_speed = -2
    pipe_width = 100
    pipe_gap_height = 250
    pipe_gap_starty = random.randrange(50,
                        display_width - 50 - pipe_gap_height)

    thingCount = 1

    dodged = 0

    gameExit = False

    passed_pipe = False
    
    while not gameExit:



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    global pause
                    pause = True
                    paused()

            if event.type == pygame.MOUSEBUTTONDOWN:
                """
                if y_pix_vel <= 0:
                    y_pix_vel = 0
                else:
                """
                if y_pix_vel <= -25:
                    y_pix_vel = -25
                if y_pix_vel >= 0:
                    y_pix_vel = -9
                else:
                    y_pix_vel += -4.5






        """
        Add y pixel velocity to y position
        Add y pixel acceleration to y pixel velocity
        """
        y += y_pix_vel
        if y_pix_vel >= 15:
            y_pix_vel = 15
        else:
            y_pix_vel += y_pix_accel

        """
        Put up blank screen
        """
        gameDisplay.fill(white)



        """
        Draw pipe with current pipe parameters
        """
        # things(thingx, thingy, thingw, thingh, color)
        pipe_draw(pipe_startx, pipe_gap_starty, pipe_width, pipe_gap_height, black)

        """
        Draw car in current x y pos
        """
        car(x, y)

        """
        Crash the car if it reaches ground or hits the top of game screen
        """

        if y > display_height - car_height or y < 0:
            crash()

        """
        When pipe goes off left edge of screen:
            Recycle pipe position, randomize pipe opening, add dodged count
            add to pipe left speed
        """
        if pipe_startx < 0 - pipe_width:
            pipe_startx = display_width + 50
            pipe_gap_starty = random.randrange(50, display_height - (50 + pipe_gap_height))
            pipe_x_speed += -.5
            passed_pipe = False

        if pipe_startx < x and passed_pipe == False:
            dodged += 1
            passed_pipe = True

        """
        pipe crash checking conditions, first if for y pos, nested if for x pos
        """
        if y < pipe_gap_starty or y + car_height > pipe_gap_starty + pipe_gap_height:
            print('y crossover')

            if x < pipe_startx + pipe_width and x+car_width > pipe_startx:
                print('x crossover')
                crash()



        # shift pipe left by pipe x speed
        pipe_startx += pipe_x_speed

        # display dodged count
        things_dodged(dodged)

        pygame.display.update()
        clock.tick(60)

"""
fonts = pygame.font.get_fonts()
print(fonts)
"""
game_intro()
game_loop()
quitgame()

