import pygame#import pygame library
import random
pygame.init()#initializes pygame
pygame.display.set_caption("War card game")#sets title for game

screen = pygame.display.set_mode((700,500))#screen size
clock = pygame.time.Clock()#sets up a clock to keep game going at a pace 

doExit = False#Variable to quit game loop
turn = False

class card:
    def __init__(self,suit,number):
        self.suit = suit
        self.number = number#
    def draw(self,x,y):
        pygame.draw.rect(screen, (255, 255, 255), (x, y, 100, 180))
        pygame.draw.rect(screen,(0,0,0),(x,y,100,180),3)
        font = pygame.font.Font('freesansbold.ttf', 24)
        text = font.render(str(self.number), 1, (0, 0, 0))
        text2 = font.render(str(self.suit), 1, (250, 0, 0))
        screen.blit(text,(x+30, y+30))
        screen.blit(text2,(x+10, y+60))
Deck = list()
for j in range (4):
    for i in range (13):
        Deck.append(card(j,i))
random.shuffle(Deck)

p1hand = list()
p2hand = list()
p1Discard = list()
p2Discard = list()

for i in range(26):
    p1hand.append(Deck[i])
for j in range (26,52):
    p2hand.append(Deck[j])
c1 = card(200,200)
c2 = card(200,300)
c3 = card(300,300)
while not doExit:#game loop--------------------------------------------------
    clock.tick(60)#how fast the game is going per minute
    event = pygame.event.wait()
    
    if event.type == pygame.QUIT:
        doExit = True
    if event.type == pygame.MOUSEBUTTONDOWN:
        turn = True
    if event.type == pygame.MOUSEBUTTONUP:
        turn = False
    if event.type == pygame.MOUSEMOTION:
        mousePos = event.pos
        
     #game logic-----------------------------------------------------
    if len(p1hand)<=0 or len(p2hand)<=0:
        if len(p1Discard)>len(p2Discard):
            print("player 1 wins haha")
        else:
            print ("player 2 wins")
        doExit = True
        
        
        
    if turn and len(p1hand)>0 and len(p2hand)>0:
        
        if p1hand[len(p1hand)-1].number>p2hand[len(p2hand)-1].number:
            print ("ha loser! player 1 wins")
            p1Discard.append(p1hand[len(p1hand)-1])
            p2Discard.append(p2hand[len(p2hand)-1])
            p1hand.pop(len(p1hand)-1)
            p2hand.pop(len(p2hand)-1)
        else:
            print ("player 2 wins")
            p2Discard.append(p1hand[len(p1hand)-1])
            p1Discard.append(p2hand[len(p2hand)-1])
            p1hand.pop(len(p1hand)-1)
            p2hand.pop(len(p2hand)-1)
            
        
        
    #render section----------------------------------------------------
    screen.fill((0,150,0))#wipes the screen

    for i in range(0,len(p1hand)):
        p1hand[i].draw(100+i*5,50)
        
    for i in range (0,len(p2hand)):
        p2hand[i].draw(100+i*5,250)
        
    for i in range(0,len(p1Discard)):
        p1Discard[i].draw(400+2*i,50)
        
    for i in range(0,len(p2Discard)):
        p2Discard[i].draw(400+2*i,250)
        
    #c1.draw(200,200)
    #c2.draw(300,100)
    #c3.draw(400,250)
    
    pygame.display.flip()#Draws everything to the screen
pygame.quit()#end of the game loop
