# Importing libraries that we'll be using
import pygame
import sys
import random

# Initializing pygame
pygame.init()
from pygame import mixer

mixer.init()
mixer.music.load("character_sprites/Campifire Song3.mp3")
mixer.music.set_volume(0.7)
mixer.music.play()

# These set us up to be able to use text and timers later
font = pygame.font.SysFont(None, 36)
clock = pygame.time.Clock()
campCollide = False
egggone = False
egg_hitbox = pygame.Rect(770, 20, 100, 100)
applegone = False
apple_hitbox = pygame.Rect(700, 330, 100, 100)
juicegone = False
juice_hitbox = pygame.Rect(925, 60, 100, 100)
melongone = False
melon_hitbox = pygame.Rect(500, 30, 100, 100)
# Defining the window we will display our game on (in terms of pixels)
SCREEN_WIDTH = 1505
SCREEN_HEIGHT = 645
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Abandoned.game')
platform = pygame.Rect(0, 0, 1, 1)
#GLOBAL VARIABLES
platform_width = 128
platform_height = 10
platform_list = []
#Here's where we import the pixel art for our leafy platforms.
#You can also import any image from your computer by instead typing in
#your computer's path to that file, e.g. (f"/path/to/file_name.png)
platform_img = pygame.image.load("character_sprites/New Piskel.png")
num_platforms = 8

#We can use pygame.Rect to make a invisible rectangular object
#to detect things like collisions
#It follows the format: pygame.Rect(<topleft_x>,<topleft_y>,<width>,<height>)

monkey_x = int(SCREEN_WIDTH / 2)
monkey_y = SCREEN_HEIGHT - 100
velocity_y = 0
monkey_size = 50
monkey = pygame.Rect(monkey_x, monkey_y, monkey_size, monkey_size)
#monkey_img = pygame.image.load(f"character_sprites/Character.png")
logs_img = pygame.image.load(f"background/logs.png")
sanityy = 0
sanityy_left = 70
frames = 0
framess = 0
frames_left = 100000000  #How many frames are left before game over

score = 0
top_score = 0
#The banana will be our player's goal

#Some RGB values we might want to use
DARK_GREEN = (0, 150, 0)
background = pygame.image.load("background/Background3.png")
WHITE = (255, 255, 255)

trees = pygame.Rect(0, 0, 400, 645)
CampfireL = pygame.Rect(640, 83, 1, 215)
CampfireR = pygame.Rect(860, 83, 1, 215)
CampfireTop = pygame.Rect(640, 83, 270, 1)
CampfireBottom = pygame.Rect(640, 297, 200, 1)

Treemidleft = pygame.Rect(180, 80, 1, 350)
Treeroofleft = pygame.Rect(180, 80, 180, 1)
Treetedgeleft = pygame.Rect(360, 1, 1, 60)
Treefloorleft = pygame.Rect(180, 430, 260, 1)
Treebedgeleft = pygame.Rect(440, 430, 1, 500)

Treemidright = pygame.Rect(1250, 80, 1, 50)
Treeroofright = pygame.Rect(1090, 80, 160, 1)
Treetedgeright = pygame.Rect(1090, 1, 1, 50)
Treeroof2right = pygame.Rect(1250, 80, 500, 1)

Treefloorright = pygame.Rect(1200, 400, 360, 1)
Treebedgeright = pygame.Rect(1200, 400, 1, 500)
Treemid2right = pygame.Rect(1300, 250, 1, 200)
Treefloor2right = pygame.Rect(1300, 250, 500, 1)

#campfire = pygame.image.load("background/Campfire.png")
campfire = pygame.image.load("background/Campfire.png")
tree_img = pygame.image.load("background/TreeSprite3.png")


def draw_setting():
    """Draws background, platforms, floor, and banana onto our screen"""

    # For each new frame, we want to redraw our background over the previous frame
    #screen.blit(starting_screen, (0, 0))
    screen.blit(background, (0, 0))

    screen.blit(tree_img, (0, 0))
    screen.blit(logs_img, (540, 150))
    screen.blit(campfire, (640, 190))
    # screen.blit(campfire, (580, 170))
    # screen.blit is how you draw one surface (like images) onto another (like our window)
    screen.blit(platform_img, platform)

    # Drawing banana

    #if len(platform_list) == num_platforms:


# Drawing score
score_txt = font.render(f"Score: {score}", True, (255, 255, 255))
screen.blit(score_txt, (10, 10))


def update_monkey():
    """Control monkey's movement and image, and detect collisions with platforms and banana"""
    #Globals allow us to edit variable that exist outside of this function
    global monkey_x, monkey_y, velocity_y, monkey, monkey_img, platform_list, score, campCollide, sanityy_left, egggone, applegone, juicegone, melongone

    #Here's how you detect keystrokes:
    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_a]:
        current_sprite = f"character_sprites/character_left.png"
        monkey_x -= 5
        monkey_img = pygame.image.load(current_sprite)
        screen.blit(monkey_img, (monkey_x, monkey_y))
    elif key_pressed[pygame.K_d]:
        current_sprite = f"character_sprites/character_right.png"
        monkey_x += 5
        monkey_img = pygame.image.load(current_sprite)
        screen.blit(monkey_img, (monkey_x, monkey_y))
    elif key_pressed[pygame.K_w]:
        current_sprite = f"character_sprites/character_back.png"
        monkey_y -= 5
        monkey_img = pygame.image.load(current_sprite)
        screen.blit(monkey_img, (monkey_x, monkey_y))
    elif key_pressed[pygame.K_s]:
        current_sprite = f"character_sprites/Character.png"
        monkey_y += 5
        monkey_img = pygame.image.load(current_sprite)
        screen.blit(monkey_img, (monkey_x, monkey_y))
    else:
        current_sprite = f"character_sprites/Character.png"
        monkey_img = pygame.image.load(current_sprite)
        screen.blit(monkey_img, (monkey_x, monkey_y))

    #Update monkey's x and y coordinates
    monkey = pygame.Rect(monkey_x, monkey_y, monkey_size, monkey_size)

    if monkey.colliderect(CampfireL):
        monkey_x -= 5
        campCollide = True
    elif monkey.colliderect(CampfireR):
        monkey_x += 5
    elif monkey.colliderect(CampfireTop):
        monkey_y -= 5
    elif monkey.colliderect(CampfireBottom):
        monkey_y += 5
        # monkey_x = Campfire[1] - monkey_size
    if monkey.colliderect(Treemidleft):
        monkey_x += 5
    elif monkey.colliderect(Treeroofleft):
        monkey_y += 5
    elif monkey.colliderect(Treetedgeleft):
        monkey_x += 5
    elif monkey.colliderect(Treefloorleft):
        monkey_y -= 5
    elif monkey.colliderect(Treebedgeleft):
        monkey_x += 5

    if monkey.colliderect(Treemidright):
        monkey_x -= 5
    elif monkey.colliderect(Treeroofright):
        monkey_y += 5
    elif monkey.colliderect(Treetedgeright):
        monkey_x -= 5
    elif monkey.colliderect(Treebedgeright):
        monkey_x -= 5
    elif monkey.colliderect(Treefloorright):
        monkey_y -= 5
    elif monkey.colliderect(Treemid2right):
        monkey_x -= 5
    elif monkey.colliderect(Treeroof2right):
        monkey_y += 5
    elif monkey.colliderect(Treefloor2right):
        monkey_y -= 5

    if monkey.colliderect(egg_hitbox):
        if egggone == False:
            sanityy_left += 5
            egggone = True

    if egggone == False:
        currentegg_sprite = f"food sprites/egg.png"
        egg_img = pygame.image.load(currentegg_sprite)
        screen.blit(egg_img, (820, 100))

    elif egggone == True:
        currentegg_sprite = f"hungry_monkey_sprites/New Piskel.png"
        egg_img = pygame.image.load(currentegg_sprite)
        screen.blit(egg_img, (820, 100))

    if monkey.colliderect(apple_hitbox):
        if applegone == False:
            sanityy_left += 5
            applegone = True
    if applegone == False:
        currentapple_sprite = f"food sprites/apple.png"
        apple_img = pygame.image.load(currentapple_sprite)
        screen.blit(apple_img, (700, 400))

    elif applegone == True:
        currentapple_sprite = f"hungry_monkey_sprites/New Piskel.png"
        apple_img = pygame.image.load(currentapple_sprite)
        screen.blit(apple_img, (700, 400))
    if monkey.colliderect(juice_hitbox):
        if juicegone == False:
            sanityy_left += 5
            juicegone = True
    if juicegone == False:
        currentjuice_sprite = f"food sprites/juice.png"
        juice_img = pygame.image.load(currentjuice_sprite)
        screen.blit(juice_img, (930, 90))

    elif juicegone == True:
        currentjuice_sprite = f"hungry_monkey_sprites/New Piskel.png"
        juice_img = pygame.image.load(currentjuice_sprite)
        screen.blit(juice_img, (930, 90))
    if monkey.colliderect(melon_hitbox):
        if melongone == False:
            sanityy_left += 10
            melongone = True
    if melongone == False:
        currentmelon_sprite = f"food sprites/melon.png"
        melon_img = pygame.image.load(currentmelon_sprite)
        screen.blit(melon_img, (500, 90))

    elif melongone == True:
        currentmelon_sprite = f"hungry_monkey_sprites/New Piskel.png"
        melon_img = pygame.image.load(currentmelon_sprite)
        screen.blit(melon_img, (500, 90))

    generate_platforms()
    # Animate the monkey sprite


#sprite_frame = int((frames / 5) % 4) + 1
#sprite_frames = int ((framess)%4) + 1
sprite_frame = int((framess / 5) % 4) + 1
if len(
        platform_list
) == num_platforms:  # Whenever platforms are all generated, play the animation
    if sprite_frame == 1:
        currentfire_sprite = "background/firesecond.png"
    elif sprite_frame == 2:
        currentfire_sprite = "background/Campfire.png"
    elif sprite_frame == 3:
        currentfire_sprite = "background/firesecond.png"
    else:
        currentfire_sprite = "background/Campfire.png"
    campfire = pygame.image.load(currentfire_sprite)
    screen.blit(campfire, (640, 190))
screen.blit(campfire, (640, 190))
#Draw monkey onto screen
screen.blit(campfire, (640, 190))
#if len(platform_list) == num_platforms:  # Whenever platforms are all generated, play the animation

# Draw monkey onto screen

#if monkey.colliderect(trees):

#Generate new platforms every time the ground is touched (won't generate if there are enough platforms)


def game_over_display():
    """Displays game stats whenever time runs out"""
    global score

    screen.fill(DARK_GREEN)
    game_over_txt = font.render("Game Over", True, WHITE)
    score_txt = font.render(f"Your score was: {score}", True, WHITE)
    top_score_txt = font.render(f"The high score is: {top_score}", True, WHITE)
    restart_txt = font.render("Press R to restart, or Q to quit", True, WHITE)

    #Draw the above text onto the screen
    screen.blit(game_over_txt,
                (SCREEN_WIDTH // 2 - game_over_txt.get_width() // 2,
                 SCREEN_HEIGHT // 2 - 100))
    screen.blit(score_txt, (SCREEN_WIDTH // 2 - score_txt.get_width() // 2,
                            SCREEN_HEIGHT // 2 - 50))
    screen.blit(top_score_txt,
                (SCREEN_WIDTH // 2 - top_score_txt.get_width() // 2,
                 SCREEN_HEIGHT // 2))
    screen.blit(restart_txt, (SCREEN_WIDTH // 2 - restart_txt.get_width() // 2,
                              SCREEN_HEIGHT // 2 + 50))
    pygame.display.update()

    # Wait for restart or quit input
    input_waiting = True
    while input_waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Press R to restart
                    input_waiting = False
                    game_loop()  # Restart the game
                elif event.key == pygame.K_q:  # Press Q to quit
                    pygame.quit()
                    sys.exit()


def advance_timer():
    """Every frame, reduce the time left for the game and display this change"""
    global top_score, frames_left

    frames_left -= 1
    timer_txt = font.render(f"Sanity: {sanityy_left}", True, (255, 255, 255))
    screen.blit(timer_txt, (10, 60))

    #Check if the timer has run out, meaning the game is over
    if frames_left <= 0:
        if score > top_score:
            top_score = score
        game_over_display()


def generate_platforms():
    """Whenever there are fewer platforms than desired num_platforms, generate new random ones"""
    current_platform_count = len(platform_list)
    while current_platform_count < num_platforms:
        platform_x = (
            random.randint(0, SCREEN_WIDTH - platform_width)
        )  #random.randint(a,b) generate a random integer between a and b
        platform_y = (random.randint(
            80 + (current_platform_count *
                  (SCREEN_HEIGHT - 80) // num_platforms),
            (80 + (current_platform_count + 1) *
             (SCREEN_HEIGHT - 80) // num_platforms)))
        #Create new rectangles for these platforms, and store them in platform_list
        platform_list.append(
            pygame.Rect(platform_x, platform_y, platform_width,
                        platform_height))

        current_platform_count += 1


def reset_variables():
    """Every time the game_loop is rerun, reset relevant variables"""
    global sanityy_left, score, platform_list, monkey_x, monkey_y

    sanity_left = 1000
    score = 0
    platform_list = []
    generate_platforms()
    monkey_x = 500
    monkey_y = SCREEN_HEIGHT - 400


sanity_drain = pygame.USEREVENT + 1
pygame.time.set_timer(sanity_drain, 1000)

frame_increase = pygame.USEREVENT + 2
pygame.time.set_timer(frame_increase,
                      1200)  # This should increment framess every 500ms


def game_loop():
    """This function runs our main game loop, yippie!"""
    global framess, sanityy_left, frames

    reset_variables()
    running = True
    while running:
        #Here is an instance of event handling, checking if the user wants to exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == sanity_drain:
                if sanityy_left > 0:
                    sanityy_left -= 1
            elif event.type == frame_increase:
                framess += 1
                #print(f"framess: {framess}"
                #)  # Debug print to see if it's incrementing

        draw_setting()  #Drawing floor, platforms, and banana
        update_monkey(
        )  #Let's allow our monkey to move and collide with things
        advance_timer()  #Progress the game timer and check if it's run out

        # Now that we've made our changes to the frame, let's update the screen to reflect those changes:
        pygame.display.update()
        clock.tick(
            30)  #This functions helps us cap the FPS (Frames per Second)
        frames += 1  #We use this frame variable to animate our monkey


game_loop()
