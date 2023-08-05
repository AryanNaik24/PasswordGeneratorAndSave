#imports
import random
from time import sleep

# Lists for different characters and symbols
specialCharacters = ["!","@","$","%","&"]
numbers = ['1','2','3','4','5','6','7','8','9','0']
capitalAlphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Password list
password = []
def main():
    # Inputs for length of password and type of password
    length = int(input("What should be the length of password?\n"))
    print("1 - only alphabets and numbers\n2 - alphabets numbers and symbols\n")
    type = int(input("which type of password do you want?\n"))


    #identifies type of password
    if type == 2:
        for i in range(0,length):
            
            #chooses a random number
            kay = random.choice(range(1,5))
            
            #depending on the number random password letter/symbol/number is appended to the main password list
            if kay == 1:
                password.append(random.choice(alphabets))
            elif kay == 2: 
                password.append(random.choice(specialCharacters))
            elif kay == 3: 
                password.append(random.choice(capitalAlphabets))
            else:
                password.append(random.choice(numbers))
    elif type == 1:
        for i in range(0,length):
            
            jay = random.choice(range(1,4))
            
            if jay == 1:
                password.append(random.choice(alphabets))
            elif jay == 2: 
                password.append(random.choice(capitalAlphabets))
            else:
                password.append(random.choice(numbers))
    #If user put in a non valid answer        
    else : 
        print("invalid input")
        main()
    
    #prints password list as a single line
    savePassword = ''.join(password)
    print(savePassword)
    
    #waits for 3 sec before asking if to save
    sleep(3)
    save = int(input("Do you wish to save the password?\n1 <= Yes\n2 <= NO\n"))
    
    if save == 1:
        
        #opens the txt file and writes into it
        fileName = input("What name do you want to save it under?\n")
        fileObject = open(r"definatlynotpass.txt","w+")
        fileObject.write(savePassword+" - "+fileName)    
        fileObject.close()
        
        print("password saved successfully")
        
    else :
        print("didnt save the password")
        

#executes main function when called
if __name__ == '__main__':
    main()

#Step 1 = take length and type of characters and symbols as input - done
#step 2 = store them in a list - done
#step 4 = use a loop to generate random passwords and append to password list - done
#step 5 = print password - done
#step 5 = store password in txt file for future reference - done
