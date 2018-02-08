#yahtzee.py
#A game of yahtzee for 1-4 players
#By: Josh Currier

#This program will be the opening for the users to see.
#It will rebresent itself graphically. After each game this program will
#return to this screen to allow the player to quit or play again.
def title(): #No Value to pass or Return
    #Show Yahtzee logo on Window
    #Show Start Button
    #Show Hi-Score Button
    #Show Quit Button
    #If start return to main to execute player turns
    #If Hi-score run Hi_Score_View()
    #If Quit run Quit()

#This will attempt to read a file called "Hi-Score.txt" if it finds it, it will
#print to the window the list of high scores. If it does not find anything it will
#run a default write file to create a "Hi-Score.txt"
#Ends by returning to the title screen
def Hi_Score_View():
    #Open "Hi-Score.txt" and save to variable
    #Print and center "Yahtzee Hall of Fame"
    #Read first line of variable with loop. If it finds it output each line.
    #If does not find run print out default hi-score list and save to "Hi-Score.txt
    #Use getmouse() to return to title()

#This will the ask the user if they would like to quit. If yes, close program.
#Otherwise return to title()
def Quit:
    #Ask user if they are sure
    #If yes close window
    #If no, return to title()

#This will ask the user how many players and what the names of the player is.
#Will return a list of the players name.
#Returns to main()
def player_count:
    #Draw player buttons (1-4 players)
    #Ask for a user name for each player

#This will handle the turn order, dice rolling, and scoring set of the game
#This will get each players score list
def yahtzee():
    #Run while loop to control turns
    while turn<13:
        #If player 1 is playing
        player1()
        #Check for player free turn
        #If player 2 is playing
        player2()
        #If player 3 is playing
        player3()
        #If player 4 is playing
        player4()
        #Increase turn by 1
        turn += 1

#This will control the flow of each players turn, including passing to the dice
#roll program, the score program, and will use the score list
def player1():
    #Draw Window that says "Player 1's turn" with Player 1 as a variable
    #Use get.mouse() when player is ready
    #Draw Dice Cup
    #Draw "Score Card Button"
    while turn_check == True:
        #If player picks dice cup:
            dice_roll()
            turn_check = False
        #If player picks "Score Card" button:
            show_score()
    #Place variable determines where to write score in list and score adds that to the score_list
    place, score = dice_roll()
    #assign place and score to player1 score list

#This will run a random function on each dice and add to dice list.
#There will be three dice rolls and player will be able to "lock" a dice to keep it from rolling.
#Sends dice list to score_checker()    
def dice_roll():
    #draw cup and dice (dice with default pips)
    #run a for loop to roll dice by iterating thru list
    #add while loop that continues until they are ready to roll again
    #Ask user if they would like to lock down dice
    #run a for loop to roll dice (check for lock flag at each iteration)
    #if i == 0 and first_dice == true:
        #Run random on list place 0
    #etc
    #run above code one more roll
    score_checker() #send dice list

#This will check the players dice and ask the player which score they would like
def score_checker():
    #sort dice list by smallest to largest
    #run if then statements checking for score criteria
    #if score == 0 and criteria above met, append to list for printing to screen
        #This list will contain the name of the score and points avaliable
    #at end of the list append "Take a zero" as an option
    #After player picks assign appropriate list place and score to variables
    #if player gets a yahtzee return free turn variable
    #return variables

#This will take all of the players score list and, using yahtzee rules, show and
#calculate players final score and show on paper
#Finish with a "player x" won! Statesment
#Return final score and player name
def score_finalizer():
    #add each players score and add to appropriate spot in each players list
    #draw and show final score card
    final_score_card()
    #check for highest score and print out "Player x has won"
    #getmouse to continue
    #return: player name, high score    

#This will compare the users results and see if they have a high score
def hi_score_checker():
    #open hi-score.txt and read to variable
    #check lowest hi score and compare to winning player
    #if player is higher then sort into appropriate area and show results
    high_score_viewer()

#Runs program and initializes score and player lists
#Running list of initialized variables to be passed
        #player1_score
        #player2_score
        #player3_score
        #player4_score
        #player_name_list
        #Dice_roll_list
        
def main():
    title()
    player_number = player_count()
    yahtzee()
    winner_name, winner_score = score_finalizer()
    hi-score_checker()
    
    
