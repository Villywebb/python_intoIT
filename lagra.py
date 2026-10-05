import sys
class User():
    def __init__ (self, username:str, password:str,items:list[str]):
        self.username = username
        self.password = password
        self.items = items

    def is_valid(self,username,password):
        return username == self.username and password == self.password
    
def print_start():
    print("\nWelcome to Lagra (TM)")

def ask_user_choice(letters_options:dict[str,str])->str:
    #prints a list of options and returns user choice
    #letter is key, option is value
    user_input = ""
    while True:
        print()
        for letter,option in letters_options.items():
            print(f"  {letter}) {option}")
        user_input = input("\nOption: ").lower()
        for letter in letters_options:
            if user_input == letter:
                return user_input
        print("Choose one of the options!\n")

def ask_user_question(question:str)->str:
    #returns user answer to question
    return input(f"\n{question}: ")

def list_items(user:User):
    print()
    for i,item in enumerate(user.items,start=1):
        print(f"{i}) {item}")

def main_menu():
    print_start()
    match ask_user_choice({"l":"Log in","q":"Quit"}):
        case "l":
            return "LOGIN"
        case "q":
            sys.exit("Lagra avslutat")
   
def login_menu(users:list[User])->tuple[str, User]:
    while True:
        username = ask_user_question("Username").lower()
        password = ask_user_question("Password")
        for user in users:
            if user.is_valid(username,password):
                print(f"\nWelcome {username}")
                return "DASHBOARD",user
        print("Invalid username or password")
        if ask_user_choice({"r":"Try again","q":"Quit"}) == "q":
            sys.exit("Lagra avslutat")
            
def dashboard(user)->str:
    print("\nThese are your items")
    list_items(user)
    print("\nSelect an action")
    match ask_user_choice({"a":"Add item","l":"List items","q":"Log out"}):
        case "a":
            user.items.append(ask_user_question("Add item"))
            return "DASHBOARD"
        case "l":
            list_items(user)
            return "DASHBOARD"
        case "q":
            return "MAIN"
    return ""

def app_runner(users:list[User]):
    state = "MAIN"
    logged_in_user = None
    while True:
        match state:
            case "MAIN":
                state = main_menu()        
            case "LOGIN":
                state,user = login_menu(users)
                logged_in_user = user
            case "DASHBOARD":
                state = dashboard(logged_in_user)
                if state == "MAIN":
                    logged_in_user = None

#prototype code, should be file import or something
users = []
users.append(User("vilmer","ICA",["Banan","Citron","Kiwi","Melon"]))
users.append(User("bernie","test",["Jacka","Mössa","Skor"]))
           
app_runner(users)