def get_user_info():
    users = {}
    email = input("Email: ")
    while email != "":
        name = get_name(email)
        check_name = f"Is your name {name}? (Y/n)"
        choice = input(check_name).strip().lower()
        while choice not in {"Y","y","n","no",""}:
            choice = input(check_name).strip().lower()
        if choice in {"n","no"}:
            name = input("Name: ")
        users[email]= name
        email = input("Email: ")
    return users

def get_name(email):
    parts = email.split("@")
    name = parts[0]
    name = name.replace("."," ")
    name = name.title()
    return name

def print_user_info(users):
    for email, name in users.items():
        print(f"{name} ({email})")

users = get_user_info()
print()
print_user_info(users)