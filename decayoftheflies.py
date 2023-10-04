# skeleton code for project 2 
# vis 142 fall 2022 
# This can take 20 minutes to hours to run. 
# imports, don't change these but you can add imports you need import pygame 
from pygame.locals import * 
from sys import exit 
import random 
import time 
# record the start time 
start_time = time.time() 
##################################################################### # We will be producing 4K video from an image sequence 
# Important: you might want to work at lower resolution that fits, # your screens! Such as 1920 x 1080. 
# And then change these back to 4096 × 2160 for production. # On the other hand, you will have to deal with scaling issues if you do. ##################################################################### # width = 1024 
# height = 540 
width = 4096 
height = 2160 
##################################################################### # Name and title, update to your name and title 
##################################################################### name = "Simona Evtimova" 
title = "Bug Alert" 
##################################################################### # IMPORTANT - you will get your start sequence number from your TA # If you use the default number 1000000 below, your work will not # be part of the class reel, as in every student must have different # start sequence numbers. 
##################################################################### start_sequence_num = 5021000 # CHANGE HERE 
# Do not change these variables 
# normal pygame stuff
clock = pygame.time.Clock() 
pygame.init() 
screen = pygame.display.set_mode((width, height)) 
pygame.display.set_caption('generate 4K animation pngs') 
frame_num = start_sequence_num 
titles_font = pygame.font.SysFont(None, int(width/12)) # if name or title run off screen, try setting the literal to 16 instead of 12 
name_f = titles_font.render(name, True, (255,255,255)) 
title_f = titles_font.render(title, True, (255,255,255)) 
# print resolution warning 
if (width != 4096 and height != 2160): 
    print("Warning: dimensions not 4K, be sure width and height are set to 4096 and 2160.") 
# this function makes one second of black frames 
def make_black(): 
    global frame_num 
    screen.fill((0,0,0)) 
    pygame.display.update() 
    for i in range(0, 60): 
        pygame.image.save(screen, "./simonaEvtimova/" + str(frame_num) + ".png") 
        frame_num = frame_num + 1 
        clock.tick(60) 
############################################################# # this object is just for example purposes - Don't use this class # unless of course to change it to be different from my circle foo # using objects will make project 2 generally easier however 
class Fly: 
    bugColor = (0, 0, 0) 
    ## 
    headSize = 0 
    bodySize = 0 
    buttWidth = 0 
    buttHeight = 0 
    leftWingWidth = 0 
    leftWingHeight = 0 
    rightWingWidth = 0 
    rightWingHeight = 0
    ## 
    headLocationX = 0 
    headLocationY = 0 
    bodyLocationX = 0 
    bodyLocationY = 0 
    buttLocationX = 0 
    buttLocationY = 0 
    leftWingLocationX = 0 
    leftWingLocationY = 0 
    rightWingLocationX = 0 
    rightWingLocationY = 0 
    ## 
    screenWidth = width 
    screenHeight = height 
    ## 
    randomInteger = 0 
    randomPicker = 0 
    ## 
    bug1_left_wing = 0 
    bug1_right_wing = 0 
    ## 
    def __init__(self): 
        self.headLocationX = width/2 
        self.headLocationY = height/2.75 
        ## 
        ## bug one location 
        self.headLocationX = self.headLocationX 
        self.headLocationY = self.headLocationY 
        self.headSize = (4 * 45) 
        self.bodyLocationX = self.headLocationX 
        self.bodyLocationY = self.headLocationY + (4 * 60) 
        self.bodySize = (4 * 150) 
        self.buttLocationX = self.bodyLocationX - (4 * 30)
        self.buttLocationY = self.bodyLocationY - (4 * 30) 
        self.buttWidth = (4 * 60)
        self.buttHeight = (4 * 150) 
        self.leftWingLocationX = self.bodyLocationX 
        self.leftWingLocationY = self.bodyLocationY 
        self.leftWingWidth = (4 * 75) 
        self.leftWingHeight = (4 * 150) 
        self.rightWingLocationX = self.bodyLocationX - (4 * 75) 
        self.rightWingLocationY = self.bodyLocationY 
        self.rightWingWidth = (4 * 75) 
        self.rightWingHeight = (4 * 150) 
        ## 
    def draw(self): 
        self.bugColor = (random.randint(0,255), random.randint(0,255), random.randint(0,255)) 
        self.randomPicker = random.randint(0, 1) 
        if (self.randomPicker == 1): 
            self.leftWingLocationX = self.bodyLocationX - (4 * 160) 
            self.leftWingLocationY = self.bodyLocationY - (4 * 20) 
            self.leftWingWidth = (4 * 150) 
            self.leftWingHeight = (4 * 75) 
            self.rightWingLocationX = self.bodyLocationX + (4 * 10) 
            self.rightWingLocationY = self.bodyLocationY - (4 * 20) 
            self.rightWingWidth = (4 * 150) 
            self.rightWingHeight = (4 * 75) 
        else: 
            self.leftWingLocationX = self.bodyLocationX 
            self.leftWingLocationY = self.bodyLocationY 
            self.leftWingWidth = (4 * 75) 
            self.leftWingHeight = (4 * 150) 
            self.rightWingLocationX = self.bodyLocationX - (4 * 75) 
            self.rightWingLocationY = self.bodyLocationY 
            self.rightWingWidth = (4 * 75) 
            self.rightWingHeight = (4 * 150)
        self.headSize = self.headSize 
        self.bodySize = self.headSize 
        self.buttSize = self.headSize 
             ## 
        self.bug1_head = pygame.draw.circle(screen, self.bugColor, (self.headLocationX, self.headLocationY), self.headSize, 0) 
        self.bug1_body = pygame.draw.circle(screen, self.bugColor, (self.bodyLocationX, self.bodyLocationY), self.bodySize, 0) 
        self.bug1_butt = pygame.draw.ellipse(screen, self.bugColor, 
        (self.buttLocationX, self.buttLocationY, self.buttWidth, self.buttHeight), 0) 
        self.bug1_left_wing = pygame.draw.ellipse(screen, self.bugColor, 
        (self.leftWingLocationX, self.leftWingLocationY, self.leftWingWidth, self.leftWingHeight), 0) 
        self.bug1_right_wing = pygame.draw.ellipse(screen, self.bugColor, (self.rightWingLocationX, self.rightWingLocationY, self.rightWingWidth, self.rightWingHeight), 0) 
        self.bug2_head = pygame.draw.circle(screen, self.bugColor, (self.headLocationX + (width/3), self.headLocationY), self.headSize, 0) 
        self.bug2_body = pygame.draw.circle(screen, self.bugColor, (self.bodyLocationX + (width/3), self.bodyLocationY), self.bodySize, 0) 
        self.bug2_butt = pygame.draw.ellipse(screen, self.bugColor, (self.buttLocationX + (width/3), self.buttLocationY, self.buttWidth, self.buttHeight), 0) 
        self.bug2_left_wing = pygame.draw.ellipse(screen, self.bugColor, 
        (self.leftWingLocationX + (width/3), self.leftWingLocationY, self.leftWingWidth, self.leftWingHeight), 0) 
        self.bug2_right_wing = pygame.draw.ellipse(screen, self.bugColor, (self.rightWingLocationX + (width/3), self.rightWingLocationY, self.rightWingWidth, self.rightWingHeight), 0) 
        self.bug3_head = pygame.draw.circle(screen, self.bugColor, (self.headLocationX - (width/3), self.headLocationY), self.headSize, 0) 
        self.bug3_body = pygame.draw.circle(screen, self.bugColor, (self.bodyLocationX - (width/3), self.bodyLocationY), self.bodySize, 0) 
        self.bug3_butt = pygame.draw.ellipse(screen, self.bugColor, (self.buttLocationX - (width/3), self.buttLocationY, self.buttWidth, self.buttHeight), 0) 
        self.bug3_left_wing = pygame.draw.ellipse(screen, self.bugColor, 
        (self.leftWingLocationX - (width/3), self.leftWingLocationY, self.leftWingWidth, self.leftWingHeight), 0)
        self.bug3_right_wing = pygame.draw.ellipse(screen, self.bugColor, (self.rightWingLocationX - (width/3), self.rightWingLocationY, self.rightWingWidth, self.rightWingHeight), 0) 
################################ end object 
# this is the credits loop, which puts the title of your work 
# and your name on the screen 
make_black() # one second black 
# produce title sequence 
screen.fill((0,0,0)) 
screen.blit(name_f, (int(width/8), int(width/8))) 
screen.blit(title_f, (int(width/8), int(width/4))) 
for i in range(0, 3*60): 
    pygame.display.update() 
    pygame.image.save(screen, "./simonaEvtimova/" + str(frame_num) + ".png") 
    frame_num = frame_num + 1 
    clock.tick(60) 
make_black() # one second black 
# make a list of active things 
active_circle_things = [] 
for i in range (0, height + width): 
    active_circle_things.append(Fly()) 
# here is the main animation loop 
for i in range(0, 20*60): # 20*60 frames is 20 seconds 
######################################################### 
# in the skeleton, your animation goes from here ######## 
######################################################### 
    screen.fill((0,0,0)) 
    for thing in active_circle_things: 
        thing.draw() 
######################################################### 
# to here ############################################### 
######################################################### 
# The next line can be commented out to speed up testing frame rate # by not writing the file. But for output to final frames, 
# you will need to ucomment it. 
    pygame.image.save(screen, "./simonaEvtimova/" + str(frame_num) + ".png") 
    frame_num = frame_num + 1
    pygame.display.update() 
    clock.tick(60) 
# print out stats 
print("seconds:", int(time.time() - start_time)) 
print("~minutes: ", int((time.time() - start_time)/60)) 
# we just quit here 
pygame.display.quit() 
pygame.quit() 
exit() 

# you can make your files into a movie with ffmpeg: 
# ffmpeg -r 60 -start_number 1000000 -s 4096x2160 -i %d.png -vcodec libx264 -crf 5 -pix_fmt yuv420p final.mp4 
# with a few changes such as to start number, but this is just extra info here
