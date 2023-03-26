"""
get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""
def main():
    name = input("Enter name: ")
    menu = get_menu()
    choose = input(">>> ").upper()
    while choose != "Q":
        if choose == "H":
            print(f"Hello {name}")
            menu = get_menu()
            choose = input(">>> ").upper()
        elif choose == "G":
            print(f"Goodbye {name}")
            menu = get_menu()
            choose = input(">>> ").upper()
        else:
            print("Invalid choice")
            choose = input(">>> ").upper()
    print("Finished")

def get_menu():
    print("(H)ello\n(G)oodbye\n(Q)uit")

main()