import turtle
import math
import random
mw = turtle.Screen()
mw.bgcolor("#424904")
mw.title("Wizards maze by Rafa94")
mw.setup(700, 700)

#Register shapes
mw.register_shape("C:/Users/Rafael Perez/PycharmProjects/Wiz game/venv/w2.gif")
mw.register_shape("C:/Users/Rafael Perez/PycharmProjects/Wiz game/venv/treasure.gif")
mw.register_shape("C:/Users/Rafael Perez/PycharmProjects/Wiz game/venv/wall3.gif")
mw.register_shape("C:/Users/Rafael Perez/PycharmProjects/Wiz game/venv/dragon.gif")
mw.register_shape("C:/Users/Rafael Perez/PycharmProjects/Wiz game/venv/d2.gif")
mw.register_shape("C:/Users/Rafael Perez/PycharmProjects/Wiz game/venv/d3.gif")
mw.register_shape("C:/Users/Rafael Perez/PycharmProjects/Wiz game/venv/d4.gif")

#Create pen
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

#Create player
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color("black")
        self.penup()
        self.speed(0)
        self.shape("C:/Users/Rafael Perez/PycharmProjects/Wiz game/venv/w2.gif")
        self.gold = 0 #We are putting gold in our "class player" equaling 0 to represent our player starting with 0 points/gold
    # Directions where our Player can go
    def go_up(self):
        #Calculate the spot to move to
        move_to_x = self.xcor()
        move_to_y = self.ycor() + 24

        #Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_down(self):
        # Calculate the spot to move to
        move_to_x = self.xcor()
        move_to_y = self.ycor() - 24

        # Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_left(self):
        # Calculate the spot to move to
        move_to_x = self.xcor()- 24
        move_to_y = self.ycor()

        # Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_right(self):
        # Calculate the spot to move to
        move_to_x = self.xcor() +24
        move_to_y = self.ycor()

        # Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def is_collision(self, other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2) )

        if distance < 5:
            return True
        else:
            return False

class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("C:/Users/Rafael Perez/PycharmProjects/Wiz game/venv/treasure.gif")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold = 100# each time we get gold it is worth a 100 points
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()

class Enemy(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("C:/Users/Rafael Perez/PycharmProjects/Wiz game/venv/dragon.gif")
        self.penup()
        self.speed(0)
        self.gold = 25  # each time we get gold it is worth a 25 points
        self.goto(x, y)
        self.direction = random.choice(["up", "down", "left", "right"])#Enemy can move randomly move either "up", "down", "left" or "right"

    def move(self):
        if self.direction == "up":
            dx = 0
            dy = 24
            #Basically saying if it goes up it will go 24 pixis up same goes for the rest
        elif self.direction == "down":
            dx = 0
            dy = -24
        elif self.direction == "left":
            dx = -24
            dy = 0
        elif self.direction == "right":
            dx = 24
            dy = 0
        else:
            dx = 0
            dy = 0

        # Check if player is close
        # if so, go in that direction
        if self.is_close(player):
            if player.xcor() < self.xcor():
                self.direction = "left"
            elif player.xcor() > self.xcor():
                self.direction = "right"
            elif player.ycor() < self.ycor():
                self.direction = "down"
            elif player.ycor() > self.ycor():
                self.direction = "up"

        #Calculate the spot to move to
        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy

        #Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        else:
            #Choose diffrent direction, basically saying else if there is a wall in there way choose a diffrent direction to go to
            self.direction = random.choice(["up", "down", "left", "right"])

        #set timer to move next time
        turtle.ontimer(self.move, t=random.randint(100, 300))
        #Whta is ontimer? calls a function to set a time of 100 and 300 milliseconds randomly

    def is_close(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2) )

        if distance < 75:
            return True
        else:
            return False

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


class Enemy2(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("C:/Users/Rafael Perez/PycharmProjects/Wiz game/venv/d2.gif")
        self.penup()
        self.speed(0)
        self.gold = 25  # each time we get gold it is worth a 25 points
        self.goto(x, y)
        self.direction = random.choice(["up", "down", "left", "right"])#Enemy can move randomly move either "up", "down", "left" or "right"

    def move(self):
        if self.direction == "up":
            dx = 0
            dy = 24
            #Basically saying if it goes up it will go 24 pixis up same goes for the rest
        elif self.direction == "down":
            dx = 0
            dy = -24
        elif self.direction == "left":
            dx = -24
            dy = 0
        elif self.direction == "right":
            dx = 24
            dy = 0
        else:
            dx = 0
            dy = 0

        #Calculate the spot to move to
        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy

        #Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        else:
            #Choose diffrent direction, basically saying else if there is a wall in there way choose a diffrent direction to go to
            self.direction = random.choice(["up", "down", "left", "right"])

        #set timer to move next time
        turtle.ontimer(self.move, t=random.randint(100, 300))
        #Whta is ontimer? calls a function to set a time of 100 and 300 milliseconds randomly


    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


class Enemy3(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("C:/Users/Rafael Perez/PycharmProjects/Wiz game/venv/d3.gif")
        self.penup()
        self.speed(0)
        self.gold = 25  # each time we get gold it is worth a 25 points
        self.goto(x, y)
        self.direction = random.choice(["up", "down", "left", "right"])#Enemy can move randomly move either "up", "down", "left" or "right"

    def move(self):
        if self.direction == "up":
            dx = 0
            dy = 24
            #Basically saying if it goes up it will go 24 pixis up same goes for the rest
        elif self.direction == "down":
            dx = 0
            dy = -24
        elif self.direction == "left":
            dx = -24
            dy = 0
        elif self.direction == "right":
            dx = 24
            dy = 0
        else:
            dx = 0
            dy = 0

        # Check if player is close
        # if so, go in that direction
        if self.is_close(player):
            if player.xcor() < self.xcor():
                self.direction = "left"
            elif player.xcor() > self.xcor():
                self.direction = "right"
            elif player.ycor() < self.ycor():
                self.direction = "down"
            elif player.ycor() > self.ycor():
                self.direction = "up"

        #Calculate the spot to move to
        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy

        #Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        else:
            #Choose diffrent direction, basically saying else if there is a wall in there way choose a diffrent direction to go to
            self.direction = random.choice(["up", "down", "left", "right"])

        #set timer to move next time
        turtle.ontimer(self.move, t=random.randint(100, 300))
        #Whta is ontimer? calls a function to set a time of 100 and 300 milliseconds randomly

    def is_close(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2) )

        if distance < 75:
            return True
        else:
            return False

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


class Enemy4(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("C:/Users/Rafael Perez/PycharmProjects/Wiz game/venv/d4.gif")
        self.penup()
        self.speed(0)
        self.gold = 25  # each time we get gold it is worth a 25 points
        self.goto(x, y)
        self.direction = random.choice(["up", "down", "left", "right"])#Enemy can move randomly move either "up", "down", "left" or "right"

    def move(self):
        if self.direction == "up":
            dx = 0
            dy = 24
            #Basically saying if it goes up it will go 24 pixis up same goes for the rest
        elif self.direction == "down":
            dx = 0
            dy = -24
        elif self.direction == "left":
            dx = -24
            dy = 0
        elif self.direction == "right":
            dx = 24
            dy = 0
        else:
            dx = 0
            dy = 0

        # Check if player is close
        # if so, go in that direction
        if self.is_close(player):
            if player.xcor() < self.xcor():
                self.direction = "left"
            elif player.xcor() > self.xcor():
                self.direction = "right"
            elif player.ycor() < self.ycor():
                self.direction = "down"
            elif player.ycor() > self.ycor():
                self.direction = "up"

        #Calculate the spot to move to
        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy

        #Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        else:
            #Choose diffrent direction, basically saying else if there is a wall in there way choose a diffrent direction to go to
            self.direction = random.choice(["up", "down", "left", "right"])

        #set timer to move next time
        turtle.ontimer(self.move, t=random.randint(100, 300))
        #Whta is ontimer? calls a function to set a time of 100 and 300 milliseconds randomly

    def is_close(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2) )

        if distance < 75:
            return True
        else:
            return False

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()

levels = [""]

level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",# 25 Blocks across
"XP XXXXXXXE          XXXXX",
"X  XXXXXXX  XXXXXX  XXXXX",
"X       XX  XXXXXX  XXXXX",
"X       XX  XXX        BXX",
"XXXXXX  XX  XXX        XX",
"XXXXXX  XX  XXXXXX  XXXXX",
"XXXXXX  XX    XXXX  XXXXX",
"X  XXXA        XXXXT  XXXXX",
"X  XXX  XXXXXXXXXXXXXXXXX",
"X         XXXXXXXXXXXXXXX",
"X                XXXXXXXX",
"XXXXXXXXXXXX     XXXXX  X",
"XXXXXXXXXXXXXXX  XXXXX  X",
"XXX  XXXXXXXXXX         X",
"XXX                    TX",
"XXXE         XXXXXXXXXXXXX",
"XXXXXXXXXX  XXXXXXXXXXXXX",
"XXXXXXXXXX              X",
"XX   XXXXX              X",
"XX   XXXXXXXXXXXXX  XXXXX",
"XX    YXXXXXXXXXXX  XXXXX",
"XXT          XXXX        X",
"XXXXD                    X",
"XXXXXXXXXXXXXXXXXXXXXXXXX"
]# 25 Blocks down
 # We have P representing the player and we the T represnting treasure in our map

#Adding a treasure list
treasures = []#Our empty list of treasure

#Add enemies list
enemies = []

#adding emeies2 list
enemies2 = []

#adding emeies3 list
enemies3 = []

#adding emeies4 list
enemies4 = []


#Add maze to maze list
levels.append(level_1)

def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            #Get the character at each x,y coordinate
            #NOTE the order of y and x in the next line
            character = level[y][x]
            #Calculate the screen x,y coordinates
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            #Check if it is an X (representing a wall)
            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.shape("C:/Users/Rafael Perez/PycharmProjects/Wiz game/venv/wall3.gif")
                pen.stamp()
                #add coordnates to wall list
                walls.append((screen_x, screen_y))
            #Check if it is a P (representing a player)
            if character == "P":
                player.goto(screen_x, screen_y)
            #Check if it is a T (representing treasure)
            if character == "T":
                treasures.append(Treasure(screen_x, screen_y))#Remember with append it adds its arguement as a single element to the end of the list, the length of the list is increased by one
                #Meaning that our points will go up by one

             #Check if it is a E (representing our enemy)
            if character == "E":
                enemies.append(Enemy(screen_x, screen_y))

            #Check if it is a D (representing our enemy2)
            if character == "D":
               enemies2.append(Enemy2(screen_x, screen_y))

            # Check if it is a A (representing our enemy3)
            if character == "A":
               enemies3.append(Enemy3(screen_x, screen_y))

            # Check if it is a A (representing our enemy3)
            if character == "B":
               enemies4.append(Enemy4(screen_x, screen_y))


#Create class instances/Object
pen = Pen()
player = Player()

#create the wall coordinate
walls = []


#Set up the level
setup_maze(levels[1])
#print(walls)#print the walls before the level!
#Keyboard binding
mw.listen()
mw.onkey(player.go_left,"a")#if we press a well go left
mw.onkey(player.go_right,"d")#if we press d well go right
mw.onkey(player.go_up,"w")#if we press w well go up
mw.onkey(player.go_down,"s")#if we press s well go left


mw.tracer()

#Start moving enemies
for enemy in enemies:
    turtle.ontimer(enemy.move, t=250)

#Start moving enemies2
for enemy in enemies2:
    turtle.ontimer(enemy.move, t=250)

#Start moving enemies3
for enemy in enemies3:
    turtle.ontimer(enemy.move, t=250)

#Start moving enemies3
for enemy in enemies4:
    turtle.ontimer(enemy.move, t=250)



#main game loop
while True:
    #Check for player collision with treasure
    #Iterate through treasure list
    for treasure in treasures:
        if player.is_collision(treasure):
            #add treasure gold to the player gold
            player.gold += treasure.gold
            print("Player Gold: {}".format(player.gold))
            #Destroy the tresure
            treasure.destroy()



    #Iterate through enemy list to see if the player collides
    for enemy in enemies:
        if player.is_collision(enemy):
            print("Player is being Attacked!")

    for enemy in enemies2:
        if player.is_collision(enemy):
            print("Player is being Attacked!")

    for enemy in enemies3:
        if player.is_collision(enemy):
            print("Player is being Attacked!")

    #update screen
    mw.update()







