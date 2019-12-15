# Ansel Sanchez - acs7fge
# Nikhil Sharma - ns7kgn

# Game: Catch the Falling Objects - Super Kawaii Catching Game
# Player has to catch objects that fall from the sky while being timed
# Game will end if player catches too many hazard items until health is zero
# Game will also end if player misses three falling items (not hazard ones)

# Checkpoint 1:

# Required Features:
# User input: player will use left and right arrow keys to move from left and right on screen
# graphics/images: there will be an image for the player and graphics of object falling
# Start screen: start screen will have our IDs and names as well as the start button to play and instructions
# Game window: game window will be 800x600

# Optional Features:
# Enemies: There will be falling hazards that will reduce player's health. The enemies can reduce helath by either 5, 10, or 25 health points
# collectibles: There will be falling objects that the player can collect that would increase their score. One can collect items that are worth 5, 10, and 25 points
# Timer: As the player keeps on playing, there will be a timer that keeps track of how long one is playing
# Health bar: There will be a health bar that will keep track of the player's health and when a hazard is collected by the player the health will be reduced. If health gets to zero, game will end

import pygame
import gamebox
import random

start = False

instruction_start = False

count = 0

current_health = 100

score = 0

time = 0

camera = gamebox.Camera(800, 600)

player = gamebox.from_image(400, 500, "player10.png")

title = gamebox.from_image(400, 100, "aids3.png")


start_button = gamebox.from_image(400, 200, "helo.png")

instructions = gamebox.from_image(400, 400, "newInstruct.png")

background = gamebox.from_image(400, 300, "help.jpg")

game_back = gamebox.from_image(400, 300, "download.png")
sides = [gamebox.from_color(0, 0, "black", 20, 1200), gamebox.from_color(800, 600, "black", 20, 1200),
         gamebox.from_color(0, 600, "black", 1600, 20)]



collect = [

    # item 1 increases score by 5
    gamebox.from_image(random.randint(20, 750), -10, "newwaifu1.png"),

    # item 2 increases score by 10
    gamebox.from_image(random.randint(20, 750), -50, "newwaifu2.png"),

    # item 3 increases score by 25
    gamebox.from_image(random.randint(20, 750), -75, "newwaifu3.png")

]

hazards = [

    # hazard 1 = reduces health by 5
    gamebox.from_image(random.randint(20, 750), -20, "newstar1.png"),

    # hazard 2  = reduces health by 10
    gamebox.from_image(random.randint(20, 750), -75, "newstar2.png"),

    # hazard 3 = reduces health by 25
    gamebox.from_image(random.randint(20, 750), -100, "newstar3.png")
]


def tick(keys):
    """

    :param keys:
    :return:
    """
    global start
    global instruction_start
    global count
    global current_health
    global score
    global time

    # start menu
    if not start:
        camera.clear("White")
        camera.draw(background)
        camera.draw(title)
        camera.draw(start_button)
        camera.draw(instructions)

        # game start - user presses space bar
        if pygame.K_SPACE in keys:
            start = True

    # Game
    else:
        camera.clear("white")

        #draws sides behind background and adds collision detection for player when it gets to left or right
        for item in sides:
            if player.touches(item):
                player.move_to_stop_overlapping(item)
            camera.draw(item)

        camera.draw(game_back)
        player.y = 525
        camera.draw(player)

        #player movement
        if pygame.K_RIGHT in keys:
            player.x += 7
        if pygame.K_LEFT in keys:
            player.x -= 7



        #falling collectables
        for thing in range(len(collect)):
            camera.draw(collect[thing])
            collect[thing].y += random.randint(1, 10)
            if collect[0].touches(player):
                score += 5
                collect[0].y = random.randint(-500, -1)
                collect[0].x = random.randint(20, 750)
                if collect[0].touches(collect[1]):
                    collect[0].move_both_to_stop_overlapping(collect[1])
                elif collect[0].touches(collect[2]):
                    collect[0].move_both_to_stop_overlapping(collect[2])
            elif collect[1].touches(player):
                score += 10
                collect[1].y = random.randint(-500, -1)
                collect[1].x = random.randint(20, 750)
                if collect[1].touches(collect[0]):
                    collect[1].move_both_to_stop_overlapping(collect[0])
                elif collect[1].touches(collect[2]):
                    collect[1].move_both_to_stop_overlapping(collect[2])
            elif collect[2].touches(player):
                score += 25
                collect[2].y = random.randint(-500, -1)
                collect[2].x = random.randint(20, 750)
                if collect[2].touches(collect[1]):
                    collect[2].move_both_to_stop_overlapping(collect[1])
                elif collect[2].touches(collect[0]):
                    collect[2].move_both_to_stop_overlapping(collect[0])

            if collect[thing].top_touches(sides[2]):
                collect[thing].y = random.randint(-500, -1)
                collect[thing].x = random.randint(20, 750)
                count +=1
            if count == 3:
                camera.draw(gamebox.from_text(400, 300, "GAME OVER", 70, "red"))
                gamebox.pause()
            camera.draw(gamebox.from_text(600, 50, "Score: " + str(score), 50, "red"))

        #falling hazards and health collisions stuff
        for hazard in range(len(hazards)):
            camera.draw(hazards[hazard])
            hazards[hazard].y +=5
            if hazards[0].touches(player):
                current_health -= 5
                hazards[0].y = random.randint(-500, -1)
                hazards[0].x = random.randint(20, 750)
                if hazards[0].touches(hazards[1]):
                    hazards[0].move_both_to_stop_overlapping(hazards[1])
                elif hazards[0].touches(hazards[2]):
                    hazards[0].move_both_to_stop_overlapping(hazards[2])
            elif hazards[1].touches(player):
                current_health -= 10
                hazards[1].y = random.randint(-500, -1)
                hazards[1].x = random.randint(20, 750)
                if hazards[1].touches(hazards[0]):
                    hazards[1].move_both_to_stop_overlapping(hazards[0])
                elif hazards[1].touches(hazards[2]):
                    hazards[1].move_both_to_stop_overlapping(hazards[2])
            elif hazards[2].touches(player):
                current_health -= 25
                hazards[2].y = random.randint(-500, -1)
                hazards[2].x = random.randint(20, 750)
                if hazards[2].touches(hazards[1]):
                    hazards[2].move_both_to_stop_overlapping(hazards[1])
                elif hazards[2].touches(hazards[0]):
                    hazards[2].move_both_to_stop_overlapping(hazards[0])

            if hazards[hazard].touches(sides[2]):
                hazards[hazard].y = random.randint(-500, -1)
                hazards[hazard].x = random.randint(20, 750)

            if current_health <= 0:
                current_health = 0
                camera.draw(gamebox.from_text(400, 300, "DEAD", 70, "red"))



                gamebox.pause()
            health = gamebox.from_text(400, 52, "Health: " + str(current_health), 50, "black")
            health_bar = gamebox.from_color(400, 50, "red", current_health * 2, 30)
            camera.draw(health_bar)
            camera.draw(health)

        #timer
        time += 1
        frac = str(int((time % ticks_per_second) / ticks_per_second * 10))
        seconds = str(int((time / ticks_per_second) % 60)).zfill(2)
        minutes = str(int((time / ticks_per_second) / 60))

        timer = gamebox.from_text(200, 50, minutes + ":" + seconds, 50, "red")
        camera.draw(timer)

    camera.display()


ticks_per_second = 60

gamebox.timer_loop(ticks_per_second, tick)
