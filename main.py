from random import randint

def generate_random_number():
    while True:
        s = ""
        for i in range(1,5):            #generates the number
            s = s + str(randint(1,9))
            
        if duplicate_checker(s) == True:
            continue
                                        #checks if the "number" has duplicate digits
        else:
            break
    return s
               
            
def input_user_number(text):
    while True:
        try:
            x = input(text)                                        #we TRY TO make a variable that points to the integer part of x in order to cover the 3rd case of invalid input
            y = int(x)
            if duplicate_checker(x) == True or len(list(x)) != 4 :  #the input from the user cant be with 1.Duplicate Digits or 2.with over four digits or 3. a combination of integers and characters(that is covered above)
                print("Input a number with 4 different digits\n")
                continue
                                            #checks if the "number" has duplicate digits
            else:
                break
        except:
            print("Invalid Input\n")
            continue
    return x
            
def duplicate_checker(a_list):
    
    a_set = set(a_list)
    
    if len(a_set) == len(a_list):
        return False
    else:
        return True
    
def cow_bulls(human_guess, number):
    human_guess = list(human_guess)
    number = list(number)
    
    cows = 0
    bulls = 0
    
    
    for i in range(0, len(human_guess)):
        
        if human_guess[i] in number:                #checks the case of both cow and bulls (that a digit in number justs exists, in whatever index, in the human_guess)
            if human_guess[i] == number[i]:
                cows += 1
                
            else:
                bulls += 1
        else:
            continue
        
    score = [cows, bulls]                                           #the cow_bulls function returns a list with 2 elements consisting of the cows and bulls
    return score
        
log = 0

while True:
    if log == 0:
        print("Welcome to Cow and Bulls game!\n")
              
    b = generate_random_number()

    while True:
        
        a = input_user_number("Guess a number: ")
        log +=1                                     
        
        score = cow_bulls(b, a)
        
        
        if score[0] == 4:
            print(f"You won!!!\nYou won by guessing {log} times")
            log = 0
            break
        else:
            print(f"Wrong! Cows:{score[0]}, Bulls:{score[1]}")
            continue
