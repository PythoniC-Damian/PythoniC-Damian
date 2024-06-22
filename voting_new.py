"DAMI VOTING APP"
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('voting_data.db')
cursor = conn.cursor()

def create_profile(name, age, gender,):
    # Insert a new voter profile into the 'voters' table
    cursor.execute("INSERT INTO voters (name, age, gender, address) VALUES (?, ?, ?, ?)", (name, age, gender,))
    # Commit the transaction
    conn.commit()
    print("Profile created successfully!")

print("WELCOME TO DAMI VOTING CENTRE")
def sign_up():
    
  global user_name # username
  global pins  # password
  global choose #
#SIGNING UP OR LOGIN FUNCTIONS
listmenu = ("1 : SIGN UP","2 : LOGIN")
for list in listmenu: 
            print(list) # print(list) would print the values in list 
            
choose = int(input("Pick the number of your choice : "))
Sign_up = 0
Login = 0
if choose == 1:
 first_name = input("Enter yout first name: ")
last_name = input("Enter your last name  : ")
name = first_name + last_name
user_name=input("Creat a username : ") 
def get_pin():
    max_attempts
    while True:
        pin1 = int(input("Create your Pin: "))
        pin2 = int(input("Re-enter your Pin: "))
        if pin1 == pin2:
            print("Pin confirmed. Proceeding to vote...")
            break
        else:
            print("The Pins do not match. Please try again.")  
            
max_attempts = 3
attempts = 0

# Flag to track if age verification was successful
age_verified = False  # Flag to track if age verification was successful
while attempts < max_attempts:
    age = int(input("Enter your age: "))
    if age >=18:
        print("You are eligible to vote")
        print("Welcome to the voting system!")
        age_verified = True  # Set the flag to True as age is verified
        break
    else:
        print("You must be at least 18 years old to vote.")
        attempts += 1
        if attempts == max_attempts:
            print("No more attempts allowed.")
            print("Exiting the program due to age restriction.")
            exit()

# Check if age was verified before proceeding
if age_verified:
    # Proceed with PIN creation
    # ... (rest of the code for PIN creation)
    pass


def main_voting_function():
    # Placeholder for the main voting logic
    pass

# Start the process
pin = get_pin()
sign_up()

    

# age = get_age()
if age >= 18:
        # Your voting logic here
    voting_centre =print( user_name.upper() ,"WELCOME TO DAMI VOTING CENTRE" )
    print(name.upper() ,"WOULD YOU LIKE TO VOTE ","Enter your pin to login")

print("Would you like to vote")
listmenu2 =["1-Yes", "2-No"]
for list in listmenu2:
    print(list)
choose = int(input("Pick the number of your choice : "))
yes = 0
no = 0
if choose == 1:
    print("Pick the political party you would like to vote for")
    parties_menu =["1-APC", "2-PDP","3-PVC","4-NPC","5-NDPP","6-OPC","7-DP"]
    for parties in parties_menu:
      print(parties)     
elif choose == 2:
    print("Goodbye")
    exit()
else:
    print("Invalid choice")

# Start the process
# pin = get_pin()
# main_voting_function()
# parties_menu =("1 : APC","2 : PDP",)
# for list in parties_menu:
#     print(list)
    



