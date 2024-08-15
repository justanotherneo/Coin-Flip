#Head or Tails Program

#import random module
import random 

#ascii H/T art
print(r'''/
                                                                                                                   
 _______        ________           ___  _____________________
|       |       |       |         /  / |                     |                              
|       |       |       |        /  /  |______         ______|
|       |       |       |       /  /          |       |                                                          
|       |_______|       |      /  /           |       |                                                          
|                       |     /  /            |       |                                                            
|         ______        |    /  /             |       |                                                                  
|        |      |       |   /  /              |       |
|        |      |       |  /  /               |       |                                                               
|________|      |_______| /__/                |_______|                                                                                    
                                                                                                                 
                                                                                                                
                     by: CRZYMike 
            (YT, FB, SC, TT, IG): CRZYCYBR
            services@crzycybersecurity.com
                                                                                                                    
''')

#welcome statement and program instructions
print('Welcome to the CRZYCYBR Coin Flip Program. To flip the coin, type \'yes\' when prompted. \n To quit, type \'exit\'')

#set game over value to false 
game_over = False

#while loop that asks user for input, that selects random number and therefor 'heads' or 'tails, and continues the program until user quits, handles invalid input
while game_over == False:

    prompt = input('Would you like to flip the coin? Type yes or no.').lower()

    if prompt == 'yes':
        choice = random.choice(range(1, 3))
        if choice == 1:
            print('The coin landed on tails')
        else:
            print('The coin landed on heads')
    
    elif prompt == 'no':
        game_over = True
        break
    
    else:
        print('That was an invalid input. You must enter \'yes\' or \'no\'')

