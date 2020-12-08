print("Welcome to my first game!")

name = input("What is your name? ")
age = int(input("What is your age? "))
print("Hello", name,"you are", age, "years old")

health = 10

if age >= 18:
    print("you are old enough to play")
    wants_play = input("Do you want to play? ").lower()
    if wants_play == "yes":
        print("Let's play!")
        print ("You are starting with", health, "health")
        left_or_right = input ("First choice... Left or Right (left/right)? ").lower()
        if left_or_right == "left":
            ans = input("Nice, you follow the path and reach a lake... Do you swim across or go around (across/around)?").lower()
            if ans == "around":
                print ("You went around and reached the other side of the lake")
            elif ans == "across":
                print ("You managed to get across, but were bit by a fish and lost 5 health")
                health -= 5          
            ans = input ("You notice a house and a river. Where do you go (house/river)? ").lower()
            if ans == "house":
                print ("You go to the house and are greted by the owner.. He doesn't like you and you lose 5 health")
                health -= 5
                if health <= 0:
                    print ("You now have 0 health and lost the game")
                else:
                    print ("you have survived, and you now won!")
            else:
                print ("You fell in the river and lost")       
        else:
            print("You fell down and lost")
    else:
        print("Cya...")
elif age>=14:
    print("you can play with supervision")
else:
    print("you are not old enough to play...")














# 4 DATA TYPES

#string "hello", 'hi' - a collection of characters
#int 8, -9 - any whole number
#float 6.0, -3.2 - any number with floating decimal
#boolean True, False - the capital T and F are essential 



# Conditions/ Arithmetic
'''* multiplication
/ division
+ addition
- subtraction
% remainder of division
// integer division 
** exponential
 

'''
