import random
import string
from time import sleep

def generate_password(length, include_symbols):
    #Generates a random password based on user specifications.
    characters = string.ascii_letters + string.digits
    if include_symbols:
        characters += "!@$%&"
    
    return ''.join(random.choices(characters, k=length))

def save_password(password):
    #Saves the generated password to a text file.
    file_name = input("Enter a name to save the password under: ")
    with open("definatlynotpass.txt", "a") as file:
        file.write(f"{password} - {file_name}\n")
    print("Password saved successfully.")

def main():
    try:
        length = int(input("Enter the length of the password: "))
        if length <= 0:
            raise ValueError("Password length must be greater than zero.")
        
        print("\n1 - Only alphabets and numbers\n2 - Alphabets, numbers, and symbols\n")
        choice = input("Choose password type (1 or 2): ")
        
        if choice not in ('1', '2'):
            raise ValueError("Invalid choice! Please enter 1 or 2.")
        
        password = generate_password(length, include_symbols=(choice == '2'))
        print(f"\nGenerated Password: {password}")
        
        sleep(2)
        save_option = input("Do you want to save the password? (y/n): ").strip().lower()
        
        if save_option == 'y':
            save_password(password)
        else:
            print("Password not saved.")
    
    except ValueError as e:
        print(f"Error: {e}")
        main()

if __name__ == '__main__':
    main()


#Step 1 = take length and type of characters and symbols as input - done
#step 2 = crete function to generate passwords - done
#step 4 = create function to save the passwords - done
#step 5 = print password - done


#future steps 
#   build gui