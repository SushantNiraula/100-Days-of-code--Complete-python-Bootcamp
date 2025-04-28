'''
                               /^L_      ,."\
           /~\       __       /~    \   ./    \
          /   _\   _/  \     /T~\|~\_\ / \_  /~|          _^
        / \ /W  \ / V^\/X  /~         T  . \/   \    ,v-./
 ,'`-. /~   ^     H  ,  . \/    ;   .   \      `. \-'   /
     M      ~     | . ;  /         ,  _   :  .    ~\_,-'
    /    ~    .    \    /   :                   '   \   ,/`
   I o. ^    oP     '98b         -      _  9.`       `\9b.
 8oO888.  oO888P  d888b9bo. .8o 888o.       8bo.  o     988o.
 88888888888888888888888888bo.98888888bo.    98888bo. .d888P
 88888888888888888888888888888888888888888888888888888888888
 88888888888888P"   "" "   """9888P" P" "8P"   ""*9888888888
 
 '''

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("\tYou are at a crossroad. Where do you want to go? Type 'left' or 'right'")
choice1= input().lower()
if choice1 == "left":
    print("\tYou come to a lake. There is an island in the middle of the lake.")
    print("\tType 'wait' to wait for a boat. Type 'swim' to swim across.")
    choice2= input().lower()
    if choice2 == "wait":
        print("\tYou arrive at the island unharmed.")
        print("\tThere is a house with three doors. One red, one yellow and one blue.")
        print("\tWhich color do you choose?")
        choice3= input().lower()
        if choice3 == "red":
            print("\tIt's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("\tYou found the treasure! You Win!")
        elif choice3 == "blue":
            print("\tYou enter a room of beasts. Game Over.")
        else:
            print("\tYou chose a door that doesn't exist. Game Over.")
    else: #if choice2 is swim 
        print("\tYou get attacked by an angry trout. Game Over.")

else:
    print("\tWrong Decision Mate! Game over")