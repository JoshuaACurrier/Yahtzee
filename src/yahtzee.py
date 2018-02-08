#yahtzee.py
#A game of yahtzee for 1-4 players
#By: Josh Currier

import pygame
from pygame.locals import *
from random import randrange

#Handles the roll work and ouputs a tuple with a value and graphic
def roll():
    die1 = pygame.image.load("Die1.png").convert_alpha()
    die2 = pygame.image.load("Die2.png").convert_alpha()
    die3 = pygame.image.load("Die3.png").convert_alpha()
    die4 = pygame.image.load("Die4.png").convert_alpha()
    die5 = pygame.image.load("Die5.png").convert_alpha()
    die6 = pygame.image.load("Die6.png").convert_alpha()
    roll_value = randrange(1,7)
    if roll_value == 1:
        dice_graphic = die1
    elif roll_value ==2:
        dice_graphic = die2
    elif roll_value == 3:
        dice_graphic = die3
    elif roll_value == 4:
        dice_graphic = die4
    elif roll_value == 5:
        dice_graphic = die5
    elif roll_value == 6:
        dice_graphic = die6
    dice_result = (roll_value,dice_graphic)
    return dice_result

#This intakes a dice value and returns it's graphic, handy when I don't want to roll.
def diceshow(dice_value):
    die1 = pygame.image.load("Die1.png").convert_alpha()
    die2 = pygame.image.load("Die2.png").convert_alpha()
    die3 = pygame.image.load("Die3.png").convert_alpha()
    die4 = pygame.image.load("Die4.png").convert_alpha()
    die5 = pygame.image.load("Die5.png").convert_alpha()
    die6 = pygame.image.load("Die6.png").convert_alpha()
    if dice_value == 1:
        dice_graphic = die1
    elif dice_value ==2:
        dice_graphic = die2
    elif dice_value == 3:
        dice_graphic = die3
    elif dice_value == 4:
        dice_graphic = die4
    elif dice_value == 5:
        dice_graphic = die5
    elif dice_value == 6:
        dice_graphic = die6
    return dice_graphic

#This will change a dices locked state look
def diceconverter(dice_value,dice_change):
    die1_locked = pygame.image.load("Die1_lock.png").convert_alpha()
    die2_locked = pygame.image.load("Die2_lock.png").convert_alpha()
    die3_locked = pygame.image.load("Die3_lock.png").convert_alpha()
    die4_locked = pygame.image.load("Die4_lock.png").convert_alpha()
    die5_locked = pygame.image.load("Die5_lock.png").convert_alpha()
    die6_locked = pygame.image.load("Die6_lock.png").convert_alpha()
    die1 = pygame.image.load("Die1.png").convert_alpha()
    die2 = pygame.image.load("Die2.png").convert_alpha()
    die3 = pygame.image.load("Die3.png").convert_alpha()
    die4 = pygame.image.load("Die4.png").convert_alpha()
    die5 = pygame.image.load("Die5.png").convert_alpha()
    die6 = pygame.image.load("Die6.png").convert_alpha()
    if dice_value == 1 and dice_change == False:
        dice_lock = die1_locked
    elif dice_value == 2 and dice_change == False:
        dice_lock = die2_locked
    elif dice_value == 3 and dice_change == False:
        dice_lock = die3_locked
    elif dice_value == 4 and dice_change == False:
        dice_lock = die4_locked
    elif dice_value == 5 and dice_change == False:
        dice_lock = die5_locked
    elif dice_value == 6 and dice_change == False:
        dice_lock = die6_locked
    elif dice_value == 1 and dice_change == True:
        dice_lock = die1
    elif dice_value == 2 and dice_change == True:
        dice_lock = die2
    elif dice_value == 3 and dice_change == True:
        dice_lock = die3
    elif dice_value == 4 and dice_change == True:
        dice_lock = die4
    elif dice_value == 5 and dice_change == True:
        dice_lock = die5
    elif dice_value == 6 and dice_change == True:
        dice_lock = die6
    return dice_lock

#Handles the title screen logic and starts the game
def title(screen):
    while True:
        #Allows game to be quit by closing the window
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
            #Gets mouse button location
            if event.type == MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                #Starts the game
                if (mouse_position[0] > 800 and mouse_position[0] < 920) and (mouse_position[1] > 350 and mouse_position[1] < 420):
                    players = player_count(screen)
                    return players
                    #print("Start Works")
                #Opens up high score file
                elif (mouse_position[0] > 800 and mouse_position[0] < 920) and (mouse_position[1] > 450 and mouse_position[1] < 520):
                    hi_score()
                    #Quits the game
                elif (mouse_position[0] > 800 and mouse_position[0] < 920) and (mouse_position[1] > 550 and mouse_position[1] < 620):
                    #print("Quit Works")
                    quit()
        #If user presses escape, leave game
        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            quit()
        #Loads and render game graphics
        logo = pygame.image.load("yahtzee_logo.png").convert_alpha()
        start_button = pygame.image.load("Start.png").convert_alpha()
        quit_button = pygame.image.load("Quit.png").convert_alpha()
        hi_score_button = pygame.image.load("Highscore.png").convert_alpha()
        background_image = pygame.image.load("background.jpg").convert_alpha()
        screen.blit(background_image, (0,0))
        screen.blit(logo,(0,0))
        screen.blit(start_button, (800,350))
        screen.blit(hi_score_button, (800,450))
        screen.blit(quit_button, (800,550))
        #Update screen with blit values
        pygame.display.update()

#Asks how many players and returns the player count         
def player_count(screen):
    finish = 0
    while True:
        #Allows game to be quit by closing the window
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
            if event.type == MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                if (mouse_position[0] > 790 and mouse_position[0] < 1020) and (mouse_position[1] > 240 and mouse_position[1] < 330):
                    #print("Player 1 Works")
                    players = 1
                    finish = 1
                elif (mouse_position[0] > 790 and mouse_position[0] < 1020) and (mouse_position[1] > 340 and mouse_position[1] < 430):
                    #print("player 2 works")
                    players = 2
                    finish = 1
                elif (mouse_position[0] > 790 and mouse_position[0] < 1020) and (mouse_position[1] > 440 and mouse_position[1] < 530):
                    #print("player 3 works")
                    players = 3
                    finish = 1
                elif (mouse_position[0] > 790 and mouse_position[0] < 1020) and (mouse_position[1] > 540 and mouse_position[1] < 630):
                    #print("player 4 works")
                    players = 4
                    finish = 1
        #If user presses escape, leave game
        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            quit()
        #convert and load graphics
        logo = pygame.image.load("yahtzee_logo.png").convert_alpha()
        background_image = pygame.image.load("background.jpg").convert_alpha()
        headline = pygame.image.load("headline_player.png").convert_alpha()
        player1 = pygame.image.load("player1.png").convert_alpha()
        player2 = pygame.image.load("player2.png").convert_alpha()
        player3 = pygame.image.load("player3.png").convert_alpha()
        player4 = pygame.image.load("player4.png").convert_alpha()
        screen.blit(background_image, (0,0))
        screen.blit(logo,(0,0))
        screen.blit(headline, (675,150))
        screen.blit(player1, (800,250))
        screen.blit(player2, (800,350))
        screen.blit(player3, (800,450))
        screen.blit(player4, (800,550))
        #Update screen with blit values
        pygame.display.update()
        #Gets mouse button location
        if finish == 1:
            break
    return players

#Runs the main game logic, specifically checking for turns and running the logic of each turn
def yahtzee(players,player1score, player2score, player3score, player4score,screen):
    turn = 1
    #Load Game Graphics
    white = 255,255,255
    myfont = pygame.font.Font(None,60)
    player1_turn = myfont.render("Player 1's Turn (Click to continue)",True, white)
    player2_turn = myfont.render("Player 2's Turn (Click to continue)",True, white)
    player3_turn = myfont.render("Player 3's Turn (Click to continue)",True, white)
    player4_turn = myfont.render("Player 4's Turn (Click to continue)",True, white)
    free_turn = myfont.render("You get a free turn!",True, white)
    while turn <= 13:
        freeturnflag = True
        free_turn_message = False
        round_count = myfont.render("     Round {} Click to continue".format(turn),True, white)
        placement = (620,310)
        pygame.display.update()
        mouse_loop(round_count,placement,screen)
        #Run Player Turn Logic
        if players > 0:
            while freeturnflag == True:
                if free_turn_message == True:
                    mouse_loop(free_turn,(550,310),screen)
                mouse_loop(player1_turn,(550,310),screen)
                player1score,freeturnflag,free_turn_message = player_turn(player1score,screen,player1score,player2score,player3score,player4score)
                score_viewer(player1score, player2score, player3score, player4score,screen)
            freeturnflag = True
            free_turn_message = False
        if players > 1:
            while freeturnflag == True:
                if free_turn_message == True:
                    mouse_loop(free_turn,(550,310),screen)
                mouse_loop(player2_turn, (550,310),screen)
                player2score,freeturnflag,free_turn_message = player_turn(player2score,screen,player1score,player2score,player3score,player4score)
                score_viewer(player1score, player2score, player3score, player4score,screen)
            freeturnflag = True
            free_turn_message = False
        if players > 2:
            while freeturnflag == True:
                if free_turn_message == True:
                    mouse_loop(free_turn,(550,310),screen)
                mouse_loop(player3_turn,(550,310), screen)
                player3score,freeturnflag,free_turn_message = player_turn(player3score,screen,player1score,player2score,player3score,player4score)
                score_viewer(player1score, player2score, player3score, player4score,screen)
            freeturnflag = True
            free_turn_message = False
        if players > 3:
            while freeturnflag == True:
                if free_turn_message == True:
                    mouse_loop(free_turn,(550,310),screen)
                mouse_loop(player4_turn,(550,310),screen)
                player4score,freeturnflag,free_turn_message = player_turn(player4score,screen,player1score,player2score,player3score,player4score)
                score_viewer(player1score, player2score, player3score, player4score,screen)
            freeturnflag = True
            free_turn_message = False
        turn += 1
    return player1score,player2score,player3score,player4score

#This will allow me to pause the game until the player presses a button on the mouse.
def mouse_loop(graphic,placement,screen):
    x = True
    logo = pygame.image.load("yahtzee_logo.png").convert_alpha()
    background_image = pygame.image.load("background.jpg").convert_alpha()
    screen.blit(background_image, (0,0))
    screen.blit(logo,(0,0))
    screen.blit(graphic, placement)
    pygame.display.update()
    while x == True:   
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                x = False
            if event.type == QUIT:
                quit()
                
#Handles the logic of each individual turn, returns a modified score list
def player_turn(currentscore,screen,player1score,player2score,player3score,player4score):
    flag = True
    dicelock1 = True
    dicelock2 = True
    dicelock3 = True
    dicelock4 = True
    dicelock5 = True
    roll_turn = 0
    diceset = [0,0,0,0,0]
    logo = pygame.image.load("yahtzee_logo.png").convert_alpha()
    background_image = pygame.image.load("background.jpg").convert_alpha()
    roll_image = pygame.image.load("Roll.png").convert_alpha()
    dice_background = pygame.image.load("dice_background.png").convert_alpha()
    #dice_check = pygame.image.load("Die1.png").convert_alpha()
    lock_button = pygame.image.load("Lock.png").convert_alpha()
    #lock_icon = pygame.image.load("lock_img.png").convert_alpha()
    
    
    screen.blit(background_image, (0,0))
    screen.blit(logo,(0,0))
    screen.blit(dice_background, (500,300))
    screen.blit(roll_image, (790,450))
   
    #screen.blit(dice_check, (520, 320))
    #screen.blit(dice_check, (660, 320))
    #screen.blit(dice_check, (800, 320))
    #screen.blit(dice_check, (940, 320))
    #screen.blit(dice_check, (1080, 320))
    pygame.display.update()
    while flag:
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
            if event.type == MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                if (mouse_position[0] > 790 and mouse_position[0] < 915) and (mouse_position[1] > 450 and mouse_position[1] < 525) and roll_turn < 3:
                    if dicelock1 == True:
                        dice1 = roll()
                        diceset[0] = dice1[0]
                        screen.blit(dice1[1],(520,320))
                    if dicelock2 == True:
                        dice2 = roll()
                        diceset[1] = dice2[0]
                        screen.blit(dice2[1],(660,320))
                    if dicelock3 == True:
                        dice3 = roll()
                        diceset[2] = dice3[0]
                        screen.blit(dice3[1],(800,320))
                    if dicelock4 == True:
                        dice4 = roll()
                        diceset[3] = dice4[0]
                        screen.blit(dice4[1],(940,320))
                    if dicelock5 == True:
                        dice5 = roll()
                        diceset[4] = dice5[0]
                        screen.blit(dice5[1],(1080,320))
                    roll_turn += 1
                    if roll_turn == 3:
                        flag = False
                    print(diceset) #Remember that this should be commented out
                elif (mouse_position[0] > 535 and mouse_position[0] < 614) and (mouse_position[1] > 250 and mouse_position[1] < 289) and roll_turn > 0:
                    if dicelock1 == True:
                        dicelock1 = False
                    else:
                        dicelock1 = True
                    dicelockimage1 = diceconverter(diceset[0],dicelock1)
                    screen.blit(dicelockimage1,(520,320))
                elif (mouse_position[0] > 675 and mouse_position[0] < 754) and (mouse_position[1] > 250 and mouse_position[1] < 289) and roll_turn > 0:
                    if dicelock2 == True:
                        dicelock2 = False
                    else:
                        dicelock2 = True
                    dicelockimage2 = diceconverter(diceset[1],dicelock2)
                    screen.blit(dicelockimage2,(660,320))
                elif (mouse_position[0] > 815 and mouse_position[0] < 894) and (mouse_position[1] > 250 and mouse_position[1] < 289) and roll_turn > 0:
                    if dicelock3 == True:
                        dicelock3 = False
                    else:
                        dicelock3 = True
                    dicelockimage3 = diceconverter(diceset[2],dicelock3)
                    screen.blit(dicelockimage3,(800,320))
                elif (mouse_position[0] > 955 and mouse_position[0] < 1034) and (mouse_position[1] > 250 and mouse_position[1] < 289) and roll_turn > 0:
                    if dicelock4 == True:
                        dicelock4 = False
                    else:
                        dicelock4 = True
                    dicelockimage4 = diceconverter(diceset[3],dicelock4)
                    screen.blit(dicelockimage4,(940,320))
                elif (mouse_position[0] > 1095 and mouse_position[0] < 1174) and (mouse_position[1] > 250 and mouse_position[1] < 289) and roll_turn > 0:
                    if dicelock5 == True:
                        dicelock5 = False
                    else:
                        dicelock5 = True
                    dicelockimage5 = diceconverter(diceset[4],dicelock5)
                    screen.blit(dicelockimage5,(1080,320))
        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            quit()
        if roll_turn > 0:
            screen.blit(lock_button, (535,250))
            screen.blit(lock_button, (675,250))
            screen.blit(lock_button, (815,250))
            screen.blit(lock_button, (955,250))
            screen.blit(lock_button, (1095,250))
            #screen.blit(lock_icon, (552,210))
            #screen.blit(lock_icon, (692,210))
            #screen.blit(lock_icon, (832,210))
            #screen.blit(lock_icon, (972,210))
            #screen.blit(lock_icon, (1112,210))    
        pygame.display.update()
    score_choice,free_turn_flag = score(diceset,currentscore)
    if free_turn_flag == True:
        free_turn_message = True
    else:
        free_turn_message = False
    currentscore = player_score(score_choice, diceset,currentscore,screen)
    print(currentscore)
    return currentscore,free_turn_flag,free_turn_message

#This program checks thru the supplied dice value and gives out the possible scoreable categories
def score(diceset,currentscore):
    free_turn_flag = False
    score_choice = []
    counts = [0,0,0,0,0,0,0]
    addup = 0
    for value in diceset:
        counts[value] = counts[value] + 1
    print(counts)
    print(currentscore)
    #check for aces (position 0)
    if counts[1] > 0 and currentscore[0] == "":
        ace_choice = (1,counts[1] * 1,0) #A tuple with position 0 = name, position 1 = score, position 2 = index number
        score_choice.append(ace_choice)
    #check for twos (position 1)
    if counts[2] > 0 and currentscore[1] == "":
        two_choice = (2,counts[2] * 2,1) #A tuple with position 0 = name, position 1 = score, position 2 = index number
        score_choice.append(two_choice)
    #check for Threes (postion 2)
    if counts[3] > 0 and currentscore[2] == "":
        three_choice = (3,counts[3] * 3,2) #A tuple with position 0 = name, position 1 = score, position 2 = index number
        score_choice.append(three_choice)
    #check for Fours (position 3)
    if counts[4] > 0 and currentscore[3] == "":
        four_choice = (4,counts[4] * 4,3) #A tuple with position 0 = name, position 1 = score, position 2 = index number
        score_choice.append(four_choice)
    #check for Fives (pos 4)
    if counts[5] > 0 and currentscore[4] == "":
        five_choice = (5,counts[5] * 5,4) #A tuple with position 0 = name, position 1 = score, position 2 = index number
        score_choice.append(five_choice)
    #check for Sixes (pos 5)
    if counts[6] > 0 and currentscore[5] == "":
        six_choice = (6,counts[6] * 6,5) #A tuple with position 0 = name, position 1 = score, position 2 = index number
        score_choice.append(six_choice)
    #check for 3 of a kind (pos 6)
    if (3 in counts or 4 in counts or 5 in counts) and currentscore[6] == "":
        for dice in diceset:
            addup = addup + dice
        threekind_value = (7,addup,6)
        score_choice.append(threekind_value)
        addup = 0
    #check for 4 of a kind (pos 7)
    if (4 in counts or 5 in counts) and currentscore[7] == "":
        for dice in diceset:
            addup = addup + dice
        fourkind_value = (8,addup,7)
        score_choice.append(fourkind_value)
        addup = 0
    #check for Full House (pos 8)
    if (3 in counts and 2 in counts) and currentscore[8] == "":
        fullhouse_value = (9,25,8)
        score_choice.append(fullhouse_value)
    #check for small Straight (pos 09)
    if not(3 in counts or 4 in counts or 5 in counts) and ((counts[1] >= 1 and counts[2] >= 1 and counts[3] >= 1 and counts[4] >= 1) or (counts[2] >= 1 and counts[3] >= 1 and counts[4] >= 1 and counts[5] >= 1) or (counts[3] >= 1 and counts[4] >= 1 and counts[5] >= 1 and counts[6] >= 1)) and currentscore[9] == "":
        smallstraight_value = (10,30,9)
        score_choice.append(smallstraight_value)
    #check for Large Straight (pos 10)
    if not(2 in counts or 3 in counts or 4 in counts or 5 in counts) and (counts[1] == 0 or counts[6] == 0) and currentscore[10] == "":
        largestraight_value = (11,40,10)
        score_choice.append(largestraight_value)
    #Yahtzee (pos 11)
    if 5 in counts:
        if currentscore[11] == "":
            yahtzee_value = (12,50,11)
            score_choice.append(yahtzee_value)
        elif currentscore[13] == "":
            yahtzeebonus_value = (14,100,13)
            score_choice.append(yahtzeebonus_value)
            free_turn_flag = True
        elif currentscore[13] != "":
            yahtzeebonus_addem = currentscore[13] + 100
            yatzeebonus_value = (14,yahtzeebonus_addem,13)
            score_choice.append(yahtzeebonus_value)
            free_turn_flag = True
    #check for chance (pos 12)
    if currentscore[12] == "":
        for dice in diceset:
            addup = addup + dice
        chance_value = (13,addup,12)
        score_choice.append(chance_value)
        addup = 0
    #print(score_choice)
    return score_choice,free_turn_flag

#renders and returns score graphic choices
def score_graphic(image_value):
    aces_button = pygame.image.load("aces.png").convert_alpha() #Value 1
    twos_button = pygame.image.load("twos.png").convert_alpha() #Value 2
    threes_button = pygame.image.load("threes.png").convert_alpha() #Value 3
    fours_button = pygame.image.load("fours.png").convert_alpha() #Value 4
    fives_button = pygame.image.load("fives.png").convert_alpha() #Value 5
    sixes_button = pygame.image.load("sixes.png").convert_alpha() #Value 6
    three_kind_button = pygame.image.load("three_kind.png").convert_alpha() #Value 7
    four_kind_button = pygame.image.load("four_kind.png").convert_alpha() #Value 8
    full_house_button = pygame.image.load("full_house.png").convert_alpha() #Value 9
    s_straight_button = pygame.image.load("s_straight.png").convert_alpha() #Value 10
    l_straight_button = pygame.image.load("l_straight.png").convert_alpha() #Value 11
    yahtzee_button = pygame.image.load("yahtzee.png").convert_alpha() #Value 12
    chance_button = pygame.image.load("chance.png").convert_alpha() #Value 13
    yahtzee_bonus_button = pygame.image.load("yahtzee_bonus.png").convert_alpha() #Value 14
    if image_value == 1:
        graphic_back = aces_button
        #print("ace works")
    elif image_value == 2:
        graphic_back = twos_button
        #print("two works")
    elif image_value == 3:
        graphic_back = threes_button
        #print("three works")
    elif image_value == 4:
        graphic_back = fours_button
        #print("four works")
    elif image_value == 5:
        graphic_back = fives_button
        #print("five works")
    elif image_value == 6:
        graphic_back = sixes_button
        #print("six works")
    elif image_value == 7:
        graphic_back = three_kind_button
        #print("three of a kind works")
    elif image_value == 8:
        graphic_back = four_kind_button
        #print("four of a kind works")
    elif image_value == 9:
        graphic_back = full_house_button
        #print("full house works")
    elif image_value == 10:
        graphic_back = s_straight_button
        #print("small straight works")
    elif image_value == 11:
        graphic_back = l_straight_button
        #print("large straight works")
    elif image_value == 12:
        graphic_back = yahtzee_button
        #print("yahtzee works")
    elif image_value == 13:
        graphic_back = chance_button
        #print("chance works")
    elif image_value == 14:
        graphic_back = yahtzee_bonus_button
        #print("yahtzee bonus works")
    return graphic_back

#Shows and gets player score choices    
def player_score(score_choice,diceset,currentscore,screen):
    #Load Graphics
    logo = pygame.image.load("yahtzee_logo.png").convert_alpha()
    background_image = pygame.image.load("background.jpg").convert_alpha()
    dice_background = pygame.image.load("dice_background.png").convert_alpha()
    zero_image = pygame.image.load("zero.png").convert_alpha()
    screen.blit(background_image, (0,0))
    screen.blit(logo,(0,0))
    screen.blit(dice_background, (20,500))
    dice1_print = diceshow(diceset[0])
    dice2_print = diceshow(diceset[1])
    dice3_print = diceshow(diceset[2])
    dice4_print = diceshow(diceset[3])
    dice5_print = diceshow(diceset[4])
    screen.blit(dice1_print,(40,520))
    screen.blit(dice2_print,(180,520))
    screen.blit(dice3_print,(320,520))
    screen.blit(dice4_print,(460,520))
    screen.blit(dice5_print,(600,520))
    x = 750
    y = 10
    i = 0
    score_flag = True
    graphic = []
    for choice in score_choice:
        graphic_temp = score_graphic(choice[0])
        graphic.append(graphic_temp)
        i += 1
    for graphic_print in graphic:
        screen.blit(graphic_print,(x,y))
        y = y + 79
    screen.blit(zero_image,(750,642))
    pygame.display.update()
    
    while score_flag == True:
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
            if event.type == MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                if (mouse_position[0] > 750 and mouse_position[0] < 1144) and (mouse_position[1] > 10 and mouse_position[1] < 79) and i > 0:
                    #print("Button Works")
                    magic = (score_choice[0][1],score_choice[0][2])
                    score_flag = False
                if (mouse_position[0] > 750 and mouse_position[0] < 1144) and (mouse_position[1] > 89 and mouse_position[1] < 158) and i > 1:
                    #print("Button Works")
                    magic = (score_choice[1][1],score_choice[1][2])
                    score_flag = False
                if (mouse_position[0] > 750 and mouse_position[0] < 1144) and (mouse_position[1] > 168 and mouse_position[1] < 237) and i > 2:
                    #print("Button Works")
                    magic = (score_choice[2][1],score_choice[2][2])
                    score_flag = False
                if (mouse_position[0] > 750 and mouse_position[0] < 1144) and (mouse_position[1] > 247 and mouse_position[1] < 306) and i > 3:
                    #print("Button Works")
                    magic = (score_choice[3][1],score_choice[3][2])
                    score_flag = False
                if (mouse_position[0] > 750 and mouse_position[0] < 1144) and (mouse_position[1] > 316 and mouse_position[1] < 385) and i > 4:
                    #print("Button Works")
                    magic = (score_choice[4][1],score_choice[4][2])
                    score_flag = False
                if (mouse_position[0] > 750 and mouse_position[0] < 1144) and (mouse_position[1] > 395 and mouse_position[1] < 464) and i > 5:
                    #print("Button Works")
                    magic = (score_choice[5][1],score_choice[5][2])
                    score_flag = False
                if (mouse_position[0] > 750 and mouse_position[0] < 1144) and (mouse_position[1] > 474 and mouse_position[1] < 543) and i > 6:
                    #print("Button Works")
                    magic = (score_choice[6][1],score_choice[6][2])
                    score_flag = False
                if (mouse_position[0] > 750 and mouse_position[0] < 1144) and (mouse_position[1] > 553 and mouse_position[1] < 622) and i > 7:
                    #print("Button Works")
                    magic = (score_choice[7][1],score_choice[7][2])
                    score_flag = False
                if (mouse_position[0] > 750 and mouse_position[0] < 1144) and (mouse_position[1] > 642 and mouse_position[1] < 711):
                    #print("Button Works")
                    magic = zero_score(currentscore,screen)
                    score_flag = False
        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            quit()
    currentscore[magic[1]] = magic[0]
    return currentscore


#Checks and creates buttons for each blank score and lets players assign a zero score.
def zero_score(currentscore,screen):
    zero_list = []
    zero_choice = []
    counter = 0
    ace_flag = False
    two_flag = False
    three_flag = False
    four_flag = False
    five_flag = False
    six_flag = False
    threekind_flag = False
    fourkind_flag = False
    fullhouse_flag = False
    sstr_flag = False
    lstr_flag = False
    yahtzee_flag = False
    chance_flag = False
    score_flag = True
    #Load Graphics
    logo = pygame.image.load("yahtzee_logo.png").convert_alpha()
    background_image = pygame.image.load("background.jpg").convert_alpha()
    zero_ace = pygame.image.load("zero_aces.png").convert_alpha()
    zero_twos = pygame.image.load("zero_twos.png").convert_alpha()
    zero_threes = pygame.image.load("zero_threes.png").convert_alpha()
    zero_fours = pygame.image.load("zero_fours.png").convert_alpha()
    zero_fives = pygame.image.load("zero_fives.png").convert_alpha()
    zero_sixes = pygame.image.load("zero_sixes.png").convert_alpha()
    zero_threekind = pygame.image.load("zero_threekind.png").convert_alpha()
    zero_fourkind = pygame.image.load("zero_fourkind.png").convert_alpha()
    zero_fullhouse = pygame.image.load("zero_fullhouse.png").convert_alpha()
    zero_sstr = pygame.image.load("zero_sstr.png").convert_alpha()
    zero_lstr = pygame.image.load("zero_lstr.png").convert_alpha()
    zero_yahtzee = pygame.image.load("zero_yahtzee.png").convert_alpha()
    zero_chance = pygame.image.load("zero_chance.png").convert_alpha()
    screen.blit(background_image, (0,0))
    screen.blit(logo,(0,0))
    pygame.display.update()
    for score in currentscore:
        if score == "":
            zero_list.append(counter)
            counter += 1
        else:
            counter += 1
    #print("This is the zero List: ",zero_list)
    for item in zero_list:
        if item == 0:
            ace_flag = True
        if item == 1:
            two_flag = True
        if item == 2:
            three_flag = True
        if item == 3:
            four_flag = True
        if item == 4:
            five_flag = True
        if item == 5:
            six_flag = True
        if item == 6:
            threekind_flag = True
        if item == 7:
            fourkind_flag = True
        if item == 8:
            fullhouse_flag = True
        if item == 9:
            sstr_flag = True
        if item == 10:
            lstr_flag = True
        if item == 11:
            yahtzee_flag = True
        if item == 12:
            chance_flag = True
    if ace_flag == True:
        screen.blit(zero_ace,(600,140))
    if two_flag == True:
        screen.blit(zero_twos,(734,140))
    if three_flag == True:
        screen.blit(zero_threes,(868,140))
    if four_flag == True:
        screen.blit(zero_fours,(600,195))
    if five_flag == True:
        screen.blit(zero_fives,(734,195))
    if six_flag == True:
        screen.blit(zero_sixes,(868,195))
    if threekind_flag == True:
        screen.blit(zero_threekind,(600,250))
    if fourkind_flag == True:
        screen.blit(zero_fourkind,(734,250))
    if fullhouse_flag == True:
        screen.blit(zero_fullhouse,(868,250))
    if sstr_flag == True:
        screen.blit(zero_sstr,(600,305))
    if lstr_flag == True:
        screen.blit(zero_lstr,(734,305))
    if yahtzee_flag == True:
        screen.blit(zero_yahtzee,(868,305))
    if chance_flag == True:
        screen.blit(zero_chance,(734,360))
    pygame.display.update()
    while score_flag == True:
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
            if event.type == MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                if (mouse_position[0] > 600 and mouse_position[0] < 1144) and (mouse_position[1] > 140 and mouse_position[1] < 158) and ace_flag == True:
                    #print("Button Works")
                    magic = (0,0)
                    score_flag = False
                if (mouse_position[0] > 734 and mouse_position[0] < 1144) and (mouse_position[1] > 140 and mouse_position[1] < 158) and two_flag == True:
                    #print("Button Works")
                    magic = (0,1)
                    score_flag = False
                if (mouse_position[0] > 868 and mouse_position[0] < 1144) and (mouse_position[1] > 140 and mouse_position[1] < 158) and three_flag == True:
                    #print("Button Works")
                    magic = (0,2)
                    score_flag = False
                if (mouse_position[0] > 600 and mouse_position[0] < 1144) and (mouse_position[1] > 195 and mouse_position[1] < 306) and four_flag == True:
                    #print("Button Works")
                    magic = (0,3)
                    score_flag = False
                if (mouse_position[0] > 734 and mouse_position[0] < 1144) and (mouse_position[1] > 195 and mouse_position[1] < 306) and five_flag == True:
                    #print("Button Works")
                    magic = (0,4)
                    score_flag = False
                if (mouse_position[0] > 868 and mouse_position[0] < 1144) and (mouse_position[1] > 195 and mouse_position[1] < 306) and six_flag == True:
                    #print("Button Works")
                    magic = (0,5)
                    score_flag = False
                if (mouse_position[0] > 600 and mouse_position[0] < 1144) and (mouse_position[1] > 250 and mouse_position[1] < 543) and threekind_flag == True:
                    #print("Button Works")
                    magic = (0,6)
                    score_flag = False
                if (mouse_position[0] > 734 and mouse_position[0] < 1144) and (mouse_position[1] > 250 and mouse_position[1] < 543) and fourkind_flag == True:
                    #print("Button Works")
                    magic = (0,7)
                    score_flag = False
                if (mouse_position[0] > 868 and mouse_position[0] < 1144) and (mouse_position[1] > 250 and mouse_position[1] < 543) and fullhouse_flag == True:
                    #print("Button Works")
                    magic = (0,8)
                    score_flag = False
                if (mouse_position[0] > 600 and mouse_position[0] < 1144) and (mouse_position[1] > 305 and mouse_position[1] < 711) and sstr_flag == True:
                    #print("Button Works")
                    magic = (0,9)
                    score_flag = False
                if (mouse_position[0] > 734 and mouse_position[0] < 1144) and (mouse_position[1] > 305 and mouse_position[1] < 711) and lstr_flag == True:
                    #print("Button Works")
                    magic = (0,10)
                    score_flag = False
                if (mouse_position[0] > 868 and mouse_position[0] < 1144) and (mouse_position[1] > 305 and mouse_position[1] < 711) and yahtzee_flag == True:
                    #print("Button Works")
                    magic = (0,11)
                    score_flag = False
                if (mouse_position[0] > 734 and mouse_position[0] < 1144) and (mouse_position[1] > 360 and mouse_position[1] < 711) and chance_flag == True:
                    #print("Button Works")
                    magic = (0,12)
                    score_flag = False
        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            quit()
    return magic
     
#Shows score card and fills in applicable scores
def score_viewer(player1score, player2score, player3score, player4score,screen):
    logo = pygame.image.load("yahtzee_logo.png").convert_alpha()
    background_image = pygame.image.load("background.jpg").convert_alpha()
    score_card = pygame.image.load("y_score_card.jpg").convert_alpha()
    black = 0,0,0
    myfont = pygame.font.Font(None,20)
    screen.blit(background_image,(0,0))
    screen.blit(logo,(0,0))
    screen.blit(score_card,(290,0))
    #Player 1 Render Score
    p1_ace = myfont.render(str(player1score[0]),True, black)
    p1_two = myfont.render(str(player1score[1]),True, black)
    p1_three = myfont.render(str(player1score[2]),True, black)
    p1_four = myfont.render(str(player1score[3]),True, black)
    p1_five = myfont.render(str(player1score[4]),True, black)
    p1_six = myfont.render(str(player1score[5]),True, black)
    p1_threekind = myfont.render(str(player1score[6]),True, black)
    p1_fourkind = myfont.render(str(player1score[7]),True, black)
    p1_fullhouse = myfont.render(str(player1score[8]),True, black)
    p1_smlstraight = myfont.render(str(player1score[9]),True, black)
    p1_lrgstraight = myfont.render(str(player1score[10]),True, black)
    p1_yahtzee = myfont.render(str(player1score[11]),True, black)
    p1_chance = myfont.render(str(player1score[12]),True, black)
    p1_bonus = myfont.render(str(player1score[13]),True, black)
    #Player 2 render Score
    p2_ace = myfont.render(str(player2score[0]),True, black)
    p2_two = myfont.render(str(player2score[1]),True, black)
    p2_three = myfont.render(str(player2score[2]),True, black)
    p2_four = myfont.render(str(player2score[3]),True, black)
    p2_five = myfont.render(str(player2score[4]),True, black)
    p2_six = myfont.render(str(player2score[5]),True, black)
    p2_threekind = myfont.render(str(player2score[6]),True, black)
    p2_fourkind = myfont.render(str(player2score[7]),True, black)
    p2_fullhouse = myfont.render(str(player2score[8]),True, black)
    p2_smlstraight = myfont.render(str(player2score[9]),True, black)
    p2_lrgstraight = myfont.render(str(player2score[10]),True, black)
    p2_yahtzee = myfont.render(str(player2score[11]),True, black)
    p2_chance = myfont.render(str(player2score[12]),True, black)
    p2_bonus = myfont.render(str(player2score[13]),True, black)
    #Player 3 render score
    p3_ace = myfont.render(str(player3score[0]),True, black)
    p3_two = myfont.render(str(player3score[1]),True, black)
    p3_three = myfont.render(str(player3score[2]),True, black)
    p3_four = myfont.render(str(player3score[3]),True, black)
    p3_five = myfont.render(str(player3score[4]),True, black)
    p3_six = myfont.render(str(player3score[5]),True, black)
    p3_threekind = myfont.render(str(player3score[6]),True, black)
    p3_fourkind = myfont.render(str(player3score[7]),True, black)
    p3_fullhouse = myfont.render(str(player3score[8]),True, black)
    p3_smlstraight = myfont.render(str(player3score[9]),True, black)
    p3_lrgstraight = myfont.render(str(player3score[10]),True, black)
    p3_yahtzee = myfont.render(str(player3score[11]),True, black)
    p3_chance = myfont.render(str(player3score[12]),True, black)
    p3_bonus = myfont.render(str(player3score[13]),True, black)
    #Player 4 render score
    p4_ace = myfont.render(str(player4score[0]),True, black)
    p4_two = myfont.render(str(player4score[1]),True, black)
    p4_three = myfont.render(str(player4score[2]),True, black)
    p4_four = myfont.render(str(player4score[3]),True, black)
    p4_five = myfont.render(str(player4score[4]),True, black)
    p4_six = myfont.render(str(player4score[5]),True, black)
    p4_threekind = myfont.render(str(player4score[6]),True, black)
    p4_fourkind = myfont.render(str(player4score[7]),True, black)
    p4_fullhouse = myfont.render(str(player4score[8]),True, black)
    p4_smlstraight = myfont.render(str(player4score[9]),True, black)
    p4_lrgstraight = myfont.render(str(player4score[10]),True, black)
    p4_yahtzee = myfont.render(str(player4score[11]),True, black)
    p4_chance = myfont.render(str(player4score[12]),True, black)
    p4_bonus = myfont.render(str(player4score[13]),True, black)
    p1x = 615
    p2x = 675
    p3x = 735
    p4x = 795
    #P1 Draw Score
    screen.blit(p1_ace,(p1x,132))
    screen.blit(p1_two,(p1x,158))
    screen.blit(p1_three,(p1x,184))
    screen.blit(p1_four,(p1x,210))
    screen.blit(p1_five,(p1x,236))
    screen.blit(p1_six,(p1x,262))
    screen.blit(p1_threekind,(p1x,385))
    screen.blit(p1_fourkind,(p1x,411))
    screen.blit(p1_fullhouse,(p1x,437))
    screen.blit(p1_smlstraight,(p1x,463))
    screen.blit(p1_lrgstraight,(p1x,489))
    screen.blit(p1_yahtzee,(p1x,515))
    screen.blit(p1_chance,(p1x,541))
    screen.blit(p1_bonus,(p1x,584))
    #P2 Draw Score
    screen.blit(p2_ace,(p2x,132))
    screen.blit(p2_two,(p2x,158))
    screen.blit(p2_three,(p2x,184))
    screen.blit(p2_four,(p2x,210))
    screen.blit(p2_five,(p2x,236))
    screen.blit(p2_six,(p2x,262))
    screen.blit(p2_threekind,(p2x,385))
    screen.blit(p2_fourkind,(p2x,411))
    screen.blit(p2_fullhouse,(p2x,437))
    screen.blit(p2_smlstraight,(p2x,463))
    screen.blit(p2_lrgstraight,(p2x,489))
    screen.blit(p2_yahtzee,(p2x,515))
    screen.blit(p2_chance,(p2x,541))
    screen.blit(p2_bonus,(p2x,584))
    #P3 Draw Score
    screen.blit(p3_ace,(p3x,132))
    screen.blit(p3_two,(p3x,158))
    screen.blit(p3_three,(p3x,184))
    screen.blit(p3_four,(p3x,210))
    screen.blit(p3_five,(p3x,236))
    screen.blit(p3_six,(p3x,262))
    screen.blit(p3_threekind,(p3x,385))
    screen.blit(p3_fourkind,(p3x,411))
    screen.blit(p3_fullhouse,(p3x,437))
    screen.blit(p3_smlstraight,(p3x,463))
    screen.blit(p3_lrgstraight,(p3x,489))
    screen.blit(p3_yahtzee,(p3x,515))
    screen.blit(p3_chance,(p3x,541))
    screen.blit(p3_bonus,(p3x,584))
    #P4 Draw Score
    screen.blit(p4_ace,(p4x,132))
    screen.blit(p4_two,(p4x,158))
    screen.blit(p4_three,(p4x,184))
    screen.blit(p4_four,(p4x,210))
    screen.blit(p4_five,(p4x,236))
    screen.blit(p4_six,(p4x,262))
    screen.blit(p4_threekind,(p4x,385))
    screen.blit(p4_fourkind,(p4x,411))
    screen.blit(p4_fullhouse,(p4x,437))
    screen.blit(p4_smlstraight,(p4x,463))
    screen.blit(p4_lrgstraight,(p4x,489))
    screen.blit(p4_yahtzee,(p4x,515))
    screen.blit(p4_chance,(p4x,541))
    screen.blit(p4_bonus,(p4x,584))
    pygame.display.update()
    flagger = True
    while flagger == True:
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
            if event.type == MOUSEBUTTONDOWN:
                flagger = False
        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            quit()


#handle end game logic
def end_game(player1score,player2score,player3score,player4score,players,screen):
    p1_grandtotal = 0
    p2_grandtotal = 0
    p3_grandtotal = 0
    p4_grandtotal = 0
    if players > 0:
        if player1score[13] == "":
            player1score[13] = 0
        p1_uppertotal = (player1score[0] + player1score[1] + player1score[2] + player1score[3] + player1score[4] + player1score[5])
        if p1_uppertotal > 63:
            p1_bonus_score = 30
        else:
            p1_bonus_score = 0
        p1_bonustotal = p1_uppertotal + p1_bonus_score
        p1_lowertotal = (player1score[6] + player1score[7] + player1score[8] + player1score[9] + player1score[10] + player1score[11] + player1score[12] + player1score[13])
        p1_grandtotal = p1_bonustotal + p1_lowertotal
    if players > 1:
        if player2score[13] == "":
            player2score[13] = 0
        p2_uppertotal =(player2score[0] + player2score[1] + player2score[2] + player2score[3] + player2score[4] + player2score[5])
        if p2_uppertotal > 63:
            p2_bonus_score = 30
        else:
            p2_bonus_score = 0
        p2_bonustotal = p2_uppertotal + p2_bonus_score
        p2_lowertotal = (player2score[6] + player2score[7] + player2score[8] + player2score[9] + player2score[10] + player2score[11] + player2score[12] + player2score[13])
        p2_grandtotal = p2_bonustotal + p2_lowertotal
    if players > 2:
        if player3score[13] == "":
            player3score[13] = 0
        p3_uppertotal = (player3score[0] + player3score[1] + player3score[2] + player3score[3] + player3score[4] + player3score[5])
        if p3_uppertotal > 63:
            p3_bonus_score = 30
        else:
            p3_bonus_score = 0
        p3_bonustotal = p3_uppertotal + p3_bonus_score
        p3_lowertotal = (player3score[6] + player3score[7] + player3score[8] + player3score[9] + player3score[10] + player3score[11] + player3score[12] + player3score[13])
        p3_grandtotal = p3_bonustotal + p3_lowertotal
    if players > 3:
        if player4score[13] == "":
            player4score[13] = 0
        p4_uppertotal = (player4score[0] + player4score[1] + player4score[2] + player4score[3] + player4score[4] + player4score[5])
        if p4_uppertotal > 63:
            p4_bonus_score = 30
        else:
            p4_bonus_score = 0
        p4_bonustotal = p4_uppertotal + p4_bonus_score
        p4_lowertotal = (player4score[6] + player4score[7] + player4score[8] + player4score[9] + player4score[10] + player4score[11] + player4score[12] + player4score[13])
        p4_grandtotal = p4_bonustotal + p4_lowertotal
    
    logo = pygame.image.load("yahtzee_logo.png").convert_alpha()
    background_image = pygame.image.load("background.jpg").convert_alpha()
    score_card = pygame.image.load("y_score_card.jpg").convert_alpha()
    black = 0,0,0
    myfont = pygame.font.Font(None,20)
    screen.blit(background_image,(0,0))
    screen.blit(logo,(0,0))
    screen.blit(score_card,(290,0))
    #Player 1 Render Score
    p1_ace = myfont.render(str(player1score[0]),True, black)
    p1_two = myfont.render(str(player1score[1]),True, black)
    p1_three = myfont.render(str(player1score[2]),True, black)
    p1_four = myfont.render(str(player1score[3]),True, black)
    p1_five = myfont.render(str(player1score[4]),True, black)
    p1_six = myfont.render(str(player1score[5]),True, black)
    p1_threekind = myfont.render(str(player1score[6]),True, black)
    p1_fourkind = myfont.render(str(player1score[7]),True, black)
    p1_fullhouse = myfont.render(str(player1score[8]),True, black)
    p1_smlstraight = myfont.render(str(player1score[9]),True, black)
    p1_lrgstraight = myfont.render(str(player1score[10]),True, black)
    p1_yahtzee = myfont.render(str(player1score[11]),True, black)
    p1_chance = myfont.render(str(player1score[12]),True, black)
    p1_bonus = myfont.render(str(player1score[13]),True, black)
    
    p1_upttl = myfont.render(str(p1_uppertotal),True,black)
    p1_bonus_final = myfont.render(str(p1_bonus_score),True,black)
    p1_bonusttl = myfont.render(str(p1_bonustotal),True,black)
    p1_lowerttl = myfont.render(str(p1_lowertotal),True,black)
    p1_grandttl = myfont.render(str(p1_grandtotal),True,black)
    
    #Player 2 render Score
    p2_ace = myfont.render(str(player2score[0]),True, black)
    p2_two = myfont.render(str(player2score[1]),True, black)
    p2_three = myfont.render(str(player2score[2]),True, black)
    p2_four = myfont.render(str(player2score[3]),True, black)
    p2_five = myfont.render(str(player2score[4]),True, black)
    p2_six = myfont.render(str(player2score[5]),True, black)
    p2_threekind = myfont.render(str(player2score[6]),True, black)
    p2_fourkind = myfont.render(str(player2score[7]),True, black)
    p2_fullhouse = myfont.render(str(player2score[8]),True, black)
    p2_smlstraight = myfont.render(str(player2score[9]),True, black)
    p2_lrgstraight = myfont.render(str(player2score[10]),True, black)
    p2_yahtzee = myfont.render(str(player2score[11]),True, black)
    p2_chance = myfont.render(str(player2score[12]),True, black)
    p2_bonus = myfont.render(str(player2score[13]),True, black)
    if players > 1:
        p2_upttl = myfont.render(str(p2_uppertotal),True,black)
        p2_bonus_final = myfont.render(str(p2_bonus_score),True,black)
        p2_bonusttl = myfont.render(str(p2_bonustotal),True,black)
        p2_lowerttl = myfont.render(str(p2_lowertotal),True,black)
        p2_grandttl = myfont.render(str(p2_grandtotal),True,black)
    #Player 3 render score
    p3_ace = myfont.render(str(player3score[0]),True, black)
    p3_two = myfont.render(str(player3score[1]),True, black)
    p3_three = myfont.render(str(player3score[2]),True, black)
    p3_four = myfont.render(str(player3score[3]),True, black)
    p3_five = myfont.render(str(player3score[4]),True, black)
    p3_six = myfont.render(str(player3score[5]),True, black)
    p3_threekind = myfont.render(str(player3score[6]),True, black)
    p3_fourkind = myfont.render(str(player3score[7]),True, black)
    p3_fullhouse = myfont.render(str(player3score[8]),True, black)
    p3_smlstraight = myfont.render(str(player3score[9]),True, black)
    p3_lrgstraight = myfont.render(str(player3score[10]),True, black)
    p3_yahtzee = myfont.render(str(player3score[11]),True, black)
    p3_chance = myfont.render(str(player3score[12]),True, black)
    p3_bonus = myfont.render(str(player3score[13]),True, black)
    if players > 2:
        p3_upttl = myfont.render(str(p3_uppertotal),True,black)
        p3_bonus_final = myfont.render(str(p3_bonus_score),True,black)
        p3_bonusttl = myfont.render(str(p3_bonustotal),True,black)
        p3_lowerttl = myfont.render(str(p3_lowertotal),True,black)
        p3_grandttl = myfont.render(str(p3_grandtotal),True,black)
    #Player 4 render score
    p4_ace = myfont.render(str(player4score[0]),True, black)
    p4_two = myfont.render(str(player4score[1]),True, black)
    p4_three = myfont.render(str(player4score[2]),True, black)
    p4_four = myfont.render(str(player4score[3]),True, black)
    p4_five = myfont.render(str(player4score[4]),True, black)
    p4_six = myfont.render(str(player4score[5]),True, black)
    p4_threekind = myfont.render(str(player4score[6]),True, black)
    p4_fourkind = myfont.render(str(player4score[7]),True, black)
    p4_fullhouse = myfont.render(str(player4score[8]),True, black)
    p4_smlstraight = myfont.render(str(player4score[9]),True, black)
    p4_lrgstraight = myfont.render(str(player4score[10]),True, black)
    p4_yahtzee = myfont.render(str(player4score[11]),True, black)
    p4_chance = myfont.render(str(player4score[12]),True, black)
    p4_bonus = myfont.render(str(player4score[13]),True, black)
    if players > 3:
        p4_upttl = myfont.render(str(p4_uppertotal),True,black)
        p4_bonus_final = myfont.render(str(p4_bonus_score),True,black)
        p4_bonusttl = myfont.render(str(p4_bonustotal),True,black)
        p4_lowerttl = myfont.render(str(p4_lowertotal),True,black)
        p4_grandttl = myfont.render(str(p4_grandtotal),True,black)
    
    p1x = 615
    p2x = 675
    p3x = 735
    p4x = 795
    #P1 Draw Score
    screen.blit(p1_ace,(p1x,132))
    screen.blit(p1_two,(p1x,158))
    screen.blit(p1_three,(p1x,184))
    screen.blit(p1_four,(p1x,210))
    screen.blit(p1_five,(p1x,236))
    screen.blit(p1_six,(p1x,262))
    screen.blit(p1_threekind,(p1x,385))
    screen.blit(p1_fourkind,(p1x,411))
    screen.blit(p1_fullhouse,(p1x,437))
    screen.blit(p1_smlstraight,(p1x,463))
    screen.blit(p1_lrgstraight,(p1x,489))
    screen.blit(p1_yahtzee,(p1x,515))
    screen.blit(p1_chance,(p1x,541))
    screen.blit(p1_bonus,(p1x,584))
    
    screen.blit(p1_upttl, (p1x,285))
    screen.blit(p1_bonus_final,(p1x,309))
    screen.blit(p1_bonusttl,(p1x,335))
    screen.blit(p1_lowerttl,(p1x,611))
    screen.blit(p1_bonusttl,(p1x,635))
    screen.blit(p1_grandttl,(p1x,661))
    #P2 Draw Score
    screen.blit(p2_ace,(p2x,132))
    screen.blit(p2_two,(p2x,158))
    screen.blit(p2_three,(p2x,184))
    screen.blit(p2_four,(p2x,210))
    screen.blit(p2_five,(p2x,236))
    screen.blit(p2_six,(p2x,262))
    screen.blit(p2_threekind,(p2x,385))
    screen.blit(p2_fourkind,(p2x,411))
    screen.blit(p2_fullhouse,(p2x,437))
    screen.blit(p2_smlstraight,(p2x,463))
    screen.blit(p2_lrgstraight,(p2x,489))
    screen.blit(p2_yahtzee,(p2x,515))
    screen.blit(p2_chance,(p2x,541))
    screen.blit(p2_bonus,(p2x,584))
    if players > 1:
        screen.blit(p2_upttl, (p2x,285))
        screen.blit(p2_bonus_final,(p2x,309))
        screen.blit(p2_bonusttl,(p2x,335))
        screen.blit(p2_lowerttl,(p2x,611))
        screen.blit(p2_bonusttl,(p2x,635))
        screen.blit(p2_grandttl,(p2x,661))

    #P3 Draw Score
    screen.blit(p3_ace,(p3x,132))
    screen.blit(p3_two,(p3x,158))
    screen.blit(p3_three,(p3x,184))
    screen.blit(p3_four,(p3x,210))
    screen.blit(p3_five,(p3x,236))
    screen.blit(p3_six,(p3x,262))
    screen.blit(p3_threekind,(p3x,385))
    screen.blit(p3_fourkind,(p3x,411))
    screen.blit(p3_fullhouse,(p3x,437))
    screen.blit(p3_smlstraight,(p3x,463))
    screen.blit(p3_lrgstraight,(p3x,489))
    screen.blit(p3_yahtzee,(p3x,515))
    screen.blit(p3_chance,(p3x,541))
    screen.blit(p3_bonus,(p3x,584))
    if players > 2:
        screen.blit(p3_upttl, (p3x,285))
        screen.blit(p3_bonus_final,(p3x,309))
        screen.blit(p3_bonusttl,(p3x,335))
        screen.blit(p3_lowerttl,(p3x,611))
        screen.blit(p3_bonusttl,(p3x,635))
        screen.blit(p3_grandttl,(p3x,661))

    #P4 Draw Score
    screen.blit(p4_ace,(p4x,132))
    screen.blit(p4_two,(p4x,158))
    screen.blit(p4_three,(p4x,184))
    screen.blit(p4_four,(p4x,210))
    screen.blit(p4_five,(p4x,236))
    screen.blit(p4_six,(p4x,262))
    screen.blit(p4_threekind,(p4x,385))
    screen.blit(p4_fourkind,(p4x,411))
    screen.blit(p4_fullhouse,(p4x,437))
    screen.blit(p4_smlstraight,(p4x,463))
    screen.blit(p4_lrgstraight,(p4x,489))
    screen.blit(p4_yahtzee,(p4x,515))
    screen.blit(p4_chance,(p4x,541))
    screen.blit(p4_bonus,(p4x,584))
    if players > 3:
        screen.blit(p4_upttl, (p4x,285))
        screen.blit(p4_bonus_final,(p4x,309))
        screen.blit(p4_bonusttl,(p4x,335))
        screen.blit(p4_lowerttl,(p4x,611))
        screen.blit(p4_bonusttl,(p4x,635))
        screen.blit(p4_grandttl,(p4x,661))

    pygame.display.update()
    flagger = True
    while flagger == True:
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
            if event.type == MOUSEBUTTONDOWN:
                flagger = False
        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            quit()
    return (p1_grandtotal,p2_grandtotal,p3_grandtotal,p4_grandtotal)

#Sets the winner and outputs a file of their score
def winner(p1_grandtotal,p2_grandtotal,p3_grandtotal,p4_grandtotal,players,screen):
    logo = pygame.image.load("yahtzee_logo.png").convert_alpha()
    background_image = pygame.image.load("background.jpg").convert_alpha()
    black = 0,0,0
    myfont = pygame.font.Font(None,60)
    screen.blit(background_image,(0,0))
    screen.blit(logo,(0,0))
    single_player = myfont.render("Congrats on a great game!",True, black)
    player1_wins = myfont.render("Player 1 Wins!!!",True, black)
    player2_wins = myfont.render("Player 2 Wins!!!",True, black)
    player3_wins = myfont.render("Player 3 Wins!!!",True, black)
    player4_wins = myfont.render("Player 4 Wins!!!",True, black)
    pygame.display.update()
    if players == 1:
        screen.blit(single_player,(550,310))
        pygame.display.update()
        winner_name = input("Enter Your Name: ")
        winner_score = p1_grandtotal
    elif players == 2:
        if p1_grandtotal > p2_grandtotal:
            screen.blit(player1_wins,(550,310))
            pygame.display.update()
            winner_name = input("Player 1, input your name: ")
            winner_score = p1_grandtotal
        else:
            screen.blit(player2_wins,(550,310))
            pygame.display.update()
            winner_name = input("Player 2, input your name: ")
            winner_score = p2_grandtotal
    elif players == 3:
        if p1_grandtotal > p2_grandtotal and p1_grandtotal > p3_grandtotal:
            screen.blit(player1_wins,(550,310))
            pygame.display.update()
            winner_name = input("Player 1, input your name: ")
            winner_score = p1_grandtotal
        elif p2_grandtotal > p1_grandtotal and p2_grandtotal > p3_grandtotal:
            screen.blit(player2_wins,(550,310))
            pygame.display.update()
            winner_name = input("Player 2, input your name: ")
            winner_score = p2_grandtotal
        else:
            screen.blit(player3_wins,(550,310))
            pygame.display.update()
            winner_name = input("Player 3, input your name: ")
            winner_score = p3_grandtotal
    else:
        if p1_grandtotal > p2_grandtotal and p1_grandtotal > p3_grandtotal and p1_grandtotal > p4_grandtotal:
            screen.blit(player1_wins,(550,310))
            pygame.display.update()
            winner_name = input("Player 1, input your name: ")
            winner_score = p1_grandtotal
        elif p2_grandtotal > p1_grandtotal and p2_grandtotal > p3_grandtotal and p2_grandtotal > p4_grandtotal:
            screen.blit(player2_wins,(550,310))
            pygame.display.update()
            winner_name = input("Player 2, input your name: ")
            winner_score = p2_grandtotal
        elif p3_grandtotal > p1_grandtotal and p3_grandtotal > p2_grandtotal and p3_grandtotal > p4_grandtotal:
            screen.blit(player3_wins,(550,310))
            pygame.display.update()
            winner_name = input("Player 3, input your name: ")
            winner_score = p3_grandtotal
        else:
            screen.blit(player4_wins,(550,310))
            pygame.display.update()
            winner_name = input("Player 4, input your name: ")
            winner_score = p4_grandtotal
    #print(winner_name,winner_score)
    waitforme= True
    while waitforme == True:
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
            if event.type == MOUSEBUTTONDOWN:
                waitforme = False
        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            quit()
    return winner_name,winner_score

#Allows the players to check all of the original high scores.
def hi_score():
    try:
        infile = open("hi_score.txt","r")
        for line in infile:
            print(line.rstrip())
    except:
        print("There is nothing to show yet")
        infile = open("hi_score.txt","w")
    infile.close()

'''def hi_score_final(winner_name,winner_score):
    recoup_list=[]
    winner_save = winner_name + (":") + str(winner_score)
    try:
        infile = open("hi_score.txt","r")
        for line in infile:
            recoup_list.append(line)
        recoup_list.append(winner_save)
        infile.close()
        outfile = open("hi_score.txt","w")
        #print(recoup_list)
        for i in range(len(recoup_list)):
            print(recoup_list[i], file=outfile)
        outfile.close()
    except:
        outfile = open("hi_score.txt","w")
        print(winner_save, file=outfile)
        outcile.close()'''
    
'''    

def score_finalizer():
    final_score_card()

def hi_score_checker():
    high_score_viewer()
'''
        
def main():
    #initialize score card for each player
    player1score = ["","","","","","","","","","","","","",""]
    player2score = ["","","","","","","","","","","","","",""]
    player3score = ["","","","","","","","","","","","","",""]
    player4score = ["","","","","","","","","","","","","",""]
    pygame.init()
    screen = pygame.display.set_mode((1280,720))
    pygame.display.set_caption("Yahtzee")
    players = title(screen)
    player1score,player2score,player3score,player4score = yahtzee(players,player1score, player2score, player3score, player4score,screen)
    p1_grandtotal,p2_grandtotal,p3_grandtotal,p4_grandtotal = end_game(player1score,player2score,player3score,player4score,players,screen)
    winner_name,winner_score = winner(p1_grandtotal,p2_grandtotal,p3_grandtotal,p4_grandtotal,players,screen)
    '''hi_score_final(winner_name,winner_score)'''
    main()
    

main()
    
    
