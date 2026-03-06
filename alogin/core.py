import json
import hashlib

def load_users():
    try:
        with open("user_db.json", "r") as file:
            return json.load(file)
    except:
        return []


def save_user(user):
    users = load_users()
    users.append(user)

    with open("user_db.json", "w") as file:
        json.dump(users, file, indent=4)


def email_exists(email):
    users=load_users()

    for user in users:
        if user["email"] == email:
            return True
    
    return False

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def create_account():
    while True:
        user_name = input("Enter your name: ")
        if not user_name.strip():
            print("Username cannot be empty")
            continue
        break

    while True:
        user_email = input("Enter your E-mail id: ")
        if not user_email.strip():
            print("Email cannot be empty")
            continue
        if '@' not in user_email or '.' not in user_email:
            print("Invalid Email format")
            continue
        
        if email_exists(user_email):
            print("Account with this email already exists")
            continue
        break

    while True:
        user_password = input("Enter the password: ")
        hashed_password = hash_password(user_password)
        if not user_password.strip():
            print("Password cannot be empty")
            continue

        re_user_password = input("Re-enter your password: ")

        if user_password == re_user_password:
            print("Account created successfully")
            break
        else:
            print("Passwords do not match")

    user = {
        "name": user_name,
        "email": user_email,
        "password": hashed_password
    }

    save_user(user)

    return user


def login_account():
    users = load_users()

    while True:
        user_email_2 = input("Enter your E-mail: ")
        if not user_email_2.strip():
            print("E-mail cannot be empty")
            continue
        break

    while True:
        user_password_2 = input("Enter your password: ")
        hashed_input = hash_password(user_password_2)
        if not user_password_2.strip():
            print("Password cannot be empty")
            continue
        break

    for user in users:
        if user["email"] == user_email_2 and user["password"] == hashed_input :
            print("Login successful")
            return

    print("Invalid email or password")


if __name__ == "__main__":
    create_account()
    login_account()
