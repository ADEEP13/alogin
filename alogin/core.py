def create_account():
    user_name = None
    user_email = None
    user_password = None

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
        break

    while True:
        user_password = input("Enter the password: ")
        if not user_password.strip():
            print("Password cannot be empty")
            continue

        re_user_password = input("Re-enter your password: ")

        if user_password == re_user_password:
            print("Account created successfully")
            break
        else:
            print("Passwords do not match")

    return {
        "name": user_name,
        "email": user_email,
        "password": user_password
    }
