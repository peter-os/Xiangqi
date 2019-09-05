
import pygame
import time

pygame.init()

display_width = 1920
display_height = 1080

black = (0,0,0)
white = (255,255,255)

background_color=(255,248,220)
board_color =(245,222,179)

gameDisplay = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('Xiangqi')
clock = pygame.time.Clock()

advisorR = pygame.image.load('Images/AdvisorR.png')
advisorB = pygame.image.load('Images/AdvisorB.png')
cannonR = pygame.image.load('Images/CannonR.png')
cannonB = pygame.image.load('Images/CannonB.png')
chariotR = pygame.image.load('Images/ChariotR.png')
chariotB = pygame.image.load('Images/ChariotB.png')
elephantR = pygame.image.load('Images/ElephantR.png')
elephantB = pygame.image.load('Images/ElephantB.png')
generalR = pygame.image.load('Images/GeneralR.png')
generalB = pygame.image.load('Images/GeneralB.png')
horseR = pygame.image.load('Images/HorseR.png')
horseB = pygame.image.load('Images/HorseB.png')
soldierR = pygame.image.load('Images/SoldierR.png')
soldierB = pygame.image.load('Images/SoldierB.png')

x_dis = display_width/3
y_dis = display_height/12 - 90

#possible coordinates starting from top left to right
x_coords = []
y_coords = []
current_pieces = ['0'] * 90

for i in range(0,90):
    if i % 9 == 0:
        y_dis += 90
        x_dis = display_width/3
    x_coords.append(x_dis)
    y_coords.append(y_dis)
    x_dis += 80
    
def draw_board():
    gameDisplay.fill(white)
    
    pygame.draw.rect(gameDisplay, board_color, (640,90,640,810))
    
    for i in range(0,9):
        pygame.draw.line(gameDisplay, black, (x_coords[i], y_coords[i]), (x_coords[36 + i],y_coords[36 + i]), 2)
        pygame.draw.line(gameDisplay, black, (x_coords[45 + i], y_coords[45 + i]), (x_coords[81 + i],y_coords[81 + i]), 2)
    
    index = 0
    for i in range(0,10):
        pygame.draw.line(gameDisplay, black, (x_coords[index], y_coords[index]), (x_coords[index+8],y_coords[index+8]), 2)
        index += 9
    
    #Border Outline
    pygame.draw.line(gameDisplay, black, (x_coords[0], y_coords[0]), (x_coords[81],y_coords[81]) , 3)
    pygame.draw.line(gameDisplay, black, (x_coords[8], y_coords[8]), (x_coords[89],y_coords[89]) , 3)
    pygame.draw.line(gameDisplay, black, (x_coords[0], y_coords[0]), (x_coords[8],y_coords[8]) , 3)
    pygame.draw.line(gameDisplay, black, (x_coords[81], y_coords[81]), (x_coords[89],y_coords[89]) , 3)

    #Diagonal Outline
    pygame.draw.line(gameDisplay, black, (x_coords[3], y_coords[3]), (x_coords[23],y_coords[23]) , 3)
    pygame.draw.line(gameDisplay, black, (x_coords[5], y_coords[5]), (x_coords[21],y_coords[21]) , 3)
    pygame.draw.line(gameDisplay, black, (x_coords[66], y_coords[66]), (x_coords[86],y_coords[86]) , 3)
    pygame.draw.line(gameDisplay, black, (x_coords[68], y_coords[68]), (x_coords[84],y_coords[84]) , 3)

def initial_board():
    set_piece(advisorB, x_coords[3] - 33, y_coords[3] - 32, 3, 'AB')
    set_piece(advisorB, x_coords[5] - 33, y_coords[5] - 32, 5, 'AB')
    set_piece(cannonB, x_coords[19] - 33, y_coords[19] - 32, 19, 'CB')
    set_piece(cannonB, x_coords[25] - 33, y_coords[25] - 32, 25, 'CB')
    set_piece(chariotB, x_coords[0] - 33, y_coords[0] - 32, 0, 'OB')
    set_piece(chariotB, x_coords[8] - 33, y_coords[8] - 32, 8, 'OB')
    set_piece(generalB, x_coords[4] - 33, y_coords[4] - 32, 4, 'GB')
    set_piece(elephantB, x_coords[2] - 33, y_coords[8] - 32, 2, 'EB')
    set_piece(elephantB, x_coords[6] - 33, y_coords[8] - 32, 6, 'EB')    
    set_piece(horseB, x_coords[1] - 33, y_coords[8] - 32, 1, 'HB')
    set_piece(horseB, x_coords[7] - 33, y_coords[8] - 32, 7, 'HB')
    set_piece(soldierB, x_coords[27] - 33, y_coords[27] - 32, 27, 'SB')
    set_piece(soldierB, x_coords[29] - 33, y_coords[29] - 32, 29, 'SB')
    set_piece(soldierB, x_coords[31] - 33, y_coords[31] - 32, 31, 'SB')
    set_piece(soldierB, x_coords[33] - 33, y_coords[33] - 32, 33, 'SB')
    set_piece(soldierB, x_coords[35] - 33, y_coords[35] - 32, 35, 'SB')

    set_piece(advisorR, x_coords[84] - 33, y_coords[84] - 32, 84, 'AR')
    set_piece(advisorR, x_coords[86] - 33, y_coords[86] - 32, 86, 'AR')
    set_piece(cannonR, x_coords[64] - 33, y_coords[64] - 32, 64, 'CR')
    set_piece(cannonR, x_coords[70] - 33, y_coords[70] - 32, 70, 'CR')
    set_piece(chariotR, x_coords[81] - 33, y_coords[81] - 32, 81, 'OR')
    set_piece(chariotR, x_coords[89] - 33, y_coords[89] - 32, 89, 'OR')
    set_piece(generalR, x_coords[85] - 33, y_coords[85] - 32, 85, 'GR')
    set_piece(elephantR, x_coords[87] - 33, y_coords[87] - 32, 87, 'ER')
    set_piece(elephantR, x_coords[83] - 33, y_coords[83] - 32, 83, 'ER')    
    set_piece(horseR, x_coords[82] - 33, y_coords[82] - 32, 82, 'HR')
    set_piece(horseR, x_coords[88] - 33, y_coords[88] - 32, 88, 'HR')
    set_piece(soldierR, x_coords[54] - 33, y_coords[54] - 32, 54, 'SR')
    set_piece(soldierR, x_coords[56] - 33, y_coords[56] - 32, 56, 'SR')
    set_piece(soldierR, x_coords[58] - 33, y_coords[58] - 32, 58, 'SR')
    set_piece(soldierR, x_coords[60] - 33, y_coords[60] - 32, 60, 'SR')
    set_piece(soldierR, x_coords[62] - 33, y_coords[62] - 32, 62, 'SR')
         
def set_piece(current_piece, x, y, location, pieceType):
    gameDisplay.blit(current_piece, (x,y))
    current_pieces[location] = pieceType

def display_piece():
    for i in range (len(current_pieces)):
        if current_pieces[i] != '0':
            if current_pieces[i] == 'AB':
                set_piece(advisorB, x_coords[i] - 33, y_coords[i] - 32, i, 'AB')
            if current_pieces[i] == 'CB':
                set_piece(cannonB, x_coords[i] - 33, y_coords[i] - 32, i, 'CB')
            if current_pieces[i] == 'OB':
                set_piece(chariotB, x_coords[i] - 33, y_coords[i] - 32, i, 'OB')
            if current_pieces[i] == 'GB':
                set_piece(generalB, x_coords[i] - 33, y_coords[i] - 32, i, 'GB')
            if current_pieces[i] == 'EB':
                set_piece(elephantB, x_coords[i] - 33, y_coords[i] - 32, i, 'EB')
            if current_pieces[i] == 'HB':
                set_piece(horseB, x_coords[i] - 33, y_coords[i] - 32, i, 'HB')
            if current_pieces[i] == 'SB':
                set_piece(soldierB, x_coords[i] - 33, y_coords[i] - 32, i, 'SB')
                
            if current_pieces[i] == 'AR':
                set_piece(advisorR, x_coords[i] - 33, y_coords[i] - 32, i, 'AR')
            if current_pieces[i] == 'CR':
                set_piece(cannonR, x_coords[i] - 33, y_coords[i] - 32, i, 'CR')
            if current_pieces[i] == 'OR':
                set_piece(chariotR, x_coords[i] - 33, y_coords[i] - 32, i, 'OR')
            if current_pieces[i] == 'GR':
                set_piece(generalR, x_coords[i] - 33, y_coords[i] - 32, i, 'GR')
            if current_pieces[i] == 'ER':
                set_piece(elephantR, x_coords[i] - 33, y_coords[i] - 32, i, 'ER')
            if current_pieces[i] == 'HR':
                set_piece(horseR, x_coords[i] - 33, y_coords[i] - 32, i, 'HR')
            if current_pieces[i] == 'SR':
                set_piece(soldierR, x_coords[i] - 33, y_coords[i] - 32, i, 'SR')

def check_piece(x, y):
    for i in range (len(current_pieces)):
        if current_pieces[i] != '0':
            if x < x_coords[i] + 30 and x > x_coords[i] - 30:
                if y < y_coords[i] + 30 and y > y_coords[i] - 30:
                    return True
                
def check_valid_move(x,y):
    for i in range (len(current_pieces)):
        if x < x_coords[i] + 30 and x > x_coords[i] - 30:
            if y < y_coords[i] + 30 and y > y_coords[i] - 30:                   
                return True
 
def move(pieceType, new_i, old_i, x, y):
    if not check_same_team(current_pieces[new_i], current_pieces[old_i]):
        if pieceType == 'AB':
            if x > x_coords[3] - 30 and x < x_coords[5] + 30 and y < y_coords[18] + 30 and y > y_coords[0] - 30:
                if new_i == old_i + 10 or new_i == old_i + 8 or new_i == old_i - 10 or new_i == old_i - 8:
                    return True
        if pieceType == 'AR':
            if x > x_coords[3] - 30 and x < x_coords[5] + 30 and y < y_coords[81] + 30 and y > y_coords[63] - 30:
                if new_i == old_i + 10 or new_i == old_i + 8 or new_i == old_i - 10 or new_i == old_i - 8:
                    return True

        if pieceType == 'CB' or pieceType == 'CR':
            counter = 0
            if x > x_coords[old_i] - 30 and x < x_coords[old_i] + 30 and y < y_coords[81] + 30 and y > y_coords[0] - 30:
                if old_i < new_i:
                    while old_i < new_i:
                        old_i += 9
                        if current_pieces[old_i] != '0':
                            counter += 1
                    if counter == 0 or counter == 2 and current_pieces[old_i] != '0':
                        return True
                    return False
                if old_i > new_i:
                    while old_i > new_i:
                        old_i -= 9
                        if current_pieces[old_i] != '0':
                            counter += 1
                    if counter == 0 or counter == 2 and current_pieces[old_i] != '0':
                        return True
                    return False

                
            if x > x_coords[0] - 30 and x < x_coords[8] + 30 and y < y_coords[old_i] + 30 and y > y_coords[old_i] - 30:
                if old_i < new_i:
                    while old_i < new_i:
                        old_i += 1
                        if current_pieces[old_i] != '0':
                            counter += 1
                    if counter == 0 or counter == 2 and current_pieces[old_i] != '0':
                        return True
                    return False
                if old_i > new_i:
                    while old_i > new_i:
                        old_i -= 1
                        if current_pieces[old_i] != '0':
                            counter += 1
                    if counter == 0 or counter == 2 and current_pieces[old_i] != '0':
                        return True
                    return False

        if pieceType == 'OB' or pieceType == 'OR':
            if x > x_coords[old_i] - 30 and x < x_coords[old_i] + 30 and y < y_coords[81] + 30 and y > y_coords[0] - 30:
                if old_i < new_i:
                    while old_i < new_i:
                        old_i += 9
                        if current_pieces[old_i] != '0' and old_i != new_i:
                            return False
                    return True
                if old_i > new_i:
                    while old_i > new_i:
                        old_i -= 9
                        if current_pieces[old_i] != '0' and old_i != new_i:
                             return False
                    return True

            if x > x_coords[0] - 30 and x < x_coords[8] + 30 and y < y_coords[old_i] + 30 and y > y_coords[old_i] - 30:
                if old_i < new_i:
                    while old_i < new_i:
                        old_i += 1
                        if current_pieces[old_i] != '0' and old_i != new_i:
                            return False
                    return True
                if old_i > new_i:
                    while old_i > new_i:
                        old_i -= 1
                        if current_pieces[old_i] != '0' and old_i != new_i:
                             return False
                    return True

        if pieceType == 'EB':
            if y < y_coords[36] + 30:
                if new_i == old_i + 20:
                    if current_pieces[new_i - 10] == '0':
                        return True
                if new_i == old_i - 20:
                    if current_pieces[new_i + 10] == '0':
                        return True
                if new_i == old_i  + 16:
                    if current_pieces[new_i - 8] == '0':
                        return True
                if new_i == old_i - 16:
                    if current_pieces[new_i + 8] == '0':
                        return True
                
        if pieceType == 'ER':
            if y > y_coords[45] - 30:
                if new_i == old_i + 20:
                    if current_pieces[new_i - 10] == '0':
                        return True
                if new_i == old_i - 20:
                    if current_pieces[new_i + 10] == '0':
                        return True
                if new_i == old_i  + 16:
                    if current_pieces[new_i - 8] == '0':
                        return True
                if new_i == old_i - 16:
                    if current_pieces[new_i + 8] == '0':
                        return True

        if pieceType == 'GB':
            if x > x_coords[3] - 30 and x < x_coords[5] + 30 and y < y_coords[18] + 30 and y > y_coords[0] - 30:
                if new_i == old_i + 1 or new_i == old_i - 1 or new_i == old_i + 9 or new_i == old_i - 9:
                    while y_coords[new_i] < y_coords[81]:
                        new_i+=9
                        if current_pieces[new_i] == 'GR':
                            return False
                        if current_pieces[new_i] != '0':
                            return True
                    return True
                
        if pieceType == 'GR':
            if x > x_coords[3] - 30 and x < x_coords[5] + 30 and y < y_coords[81] + 30 and y > y_coords[63] - 30:
                if new_i == old_i + 1 or new_i == old_i - 1 or new_i == old_i + 9 or new_i == old_i - 9:
                    while y_coords[new_i] > y_coords[0]:
                        new_i-=9
                        print (current_pieces[i])
                        if current_pieces[new_i] == 'GB':
                            return False
                        if current_pieces[new_i] != '0':
                            return True
                    return True

        if pieceType == 'HB' or pieceType == 'HR':
            if new_i == old_i + 19 or new_i == old_i + 17:
                if current_pieces[old_i + 9] == '0':
                    return True
            if new_i == old_i - 19 or new_i == old_i - 17:
                if current_pieces[old_i - 9] == '0':
                    return True
            if new_i == old_i + 7 or new_i == old_i - 11:
                 if current_pieces[old_i - 1] == '0':
                    return True           
            if new_i == old_i - 7 or new_i == old_i + 11:
                if current_pieces[old_i + 1] == '0':
                    return True
            return False

        if pieceType == 'SB':
            if y < y_coords[45] + 30:
                if new_i == old_i + 9:
                    return True
            if y > y_coords[45] - 30:
                if new_i == old_i + 9 or y < y_coords[old_i] + 30 and y > y_coords[old_i] - 30 and new_i == old_i + 1 or new_i == old_i - 1:
                    return True
        if pieceType == 'SR':
            if y > y_coords[36] - 30:
                if new_i == old_i - 9:
                    return True
            if y < y_coords[36] + 30:
                if new_i == old_i - 9 or y < y_coords[old_i] + 30 and y > y_coords[old_i] - 30 and new_i == old_i + 1 or new_i == old_i - 1:
                    return True

def get_move_index(x,y):
    for i in range (len(current_pieces)):
        if x < x_coords[i] + 30 and x > x_coords[i] - 30:
            if y < y_coords[i] + 30 and y > y_coords[i] - 30:                 
                return i

def selected_piece(x, y):
    for i in range (len(current_pieces)):
        if current_pieces[i] != '0':
            if x < x_coords[i] + 30 and x > x_coords[i] - 30:
                if y < y_coords[i] + 30 and y > y_coords[i] - 30:                 
                    return current_pieces[i], i

def check_same_team(moving_piece, existing_piece):
    if existing_piece != '0':
        if moving_piece == 'AB'or moving_piece == 'CB' or moving_piece == 'OB' or moving_piece == 'GB' or moving_piece == 'EB' or moving_piece == 'HB' or moving_piece == 'SB':
            if existing_piece == 'AB'or existing_piece == 'CB' or existing_piece == 'OB' or existing_piece == 'GB' or existing_piece == 'EB' or existing_piece == 'HB' or existing_piece == 'SB':
                return True
        if moving_piece == 'AR'or moving_piece == 'CR' or moving_piece == 'OR' or moving_piece == 'GR' or moving_piece == 'ER' or moving_piece == 'HR' or moving_piece == 'SR':
            if existing_piece == 'AR'or existing_piece == 'CR' or existing_piece == 'OR' or existing_piece == 'GR' or existing_piece == 'ER' or existing_piece == 'HR' or existing_piece == 'SR':
                return True
            
def assign_piece(symbol):
    if symbol == 'AB':
        return advisorB
    if symbol == 'CB':
        return cannonB
    if symbol == 'OB':
        return chariotB
    if symbol == 'GB':
        return generalB
    if symbol == 'EB':
        return elephantB
    if symbol == 'HB':
        return horseB
    if symbol == 'SB':
        return soldierB
    
    if symbol == 'AR':
        return advisorR
    if symbol == 'CR':
        return cannonR
    if symbol == 'OR':
        return chariotR
    if symbol == 'GR':
        return generalR
    if symbol == 'ER':
        return elephantR
    if symbol == 'HR':
        return horseR
    if symbol == 'SR':
        return soldierR

    return '0'

def set_new_piece(current_piece, location, pieceType):
    current_pieces[location] = pieceType
    draw_board()
    display_piece()
    gameDisplay.blit(current_piece, (x_coords[location] - 33, y_coords[location]- 32))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_end(text):
    textFont = pygame.font.Font('freesansbold.ttf',200)
    textSurf, textRect = text_objects(text, textFont)
    textRect.center = ((display_width/2),(display_height/3))
    gameDisplay.blit(textSurf, textRect)
    pygame.display.flip()
    game_body()

def game_body():
    
    gameEnd = False
    selected = 0
#Red goes first
    player_turn = 'R'
    
    while not gameEnd:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
#LMB to select a piece
            elif selected == 1 and event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    new_index = check_valid_move(mousex, mousey)
                    if check_valid_move(mousex, mousey):
                        new_index = get_move_index(mousex, mousey)
                        if move(strPiece, new_index, index, mousex, mousey):
                            current_pieces[index] = '0'
                            if current_pieces[new_index] == 'GB':
                                message_end("RED WINS!")
                                gameEnd = True                               
                            if current_pieces[new_index] == 'GR':
                                message_end("BLACK WINS!")
                                gameEnd = True
                            set_new_piece(dragPiece, new_index, strPiece)
                            selected = 0
                            if player_turn == 'R':
                                player_turn = 'B'
                            else:
                                player_turn = 'R'
#RMB to cancel selected piece
                if event.button == 3:
                    selected = 0
                    draw_board()
                    display_piece()                   
                    
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mousex, mousey = pygame.mouse.get_pos()
                    print(mousex,mousey)
                    if check_piece(mousex, mousey):
                        strPiece, index = selected_piece(mousex, mousey)
                        if strPiece[1] == player_turn:
                            dragPiece = assign_piece(strPiece)
                            selected = 1;
                    
            elif selected == 1:
                draw_board()
                mousex, mousey = pygame.mouse.get_pos()
                gameDisplay.blit(dragPiece, (mousex - 33,mousey- 32))
                display_piece()
                clock.tick(30)

            
        pygame.display.update()
        clock.tick(60)
    
draw_board()
initial_board()
game_body()


pygame.quit()
quit()


