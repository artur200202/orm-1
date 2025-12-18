from models import Owners, session

def login():
    email = input("Enter Email: ")
    password = input("Enter Password: ")
    user = session.query(Owners).filter_by(email=email).first()
    if not user:
        print("User not found.")
        return None
    if user.password != password:
        print("Incorrect password.")
        return None
    print(f"Welcome back, {user.name}!")
    return user


def register():
    print("Register New Account")
    try:
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        password = input("Password: ")
        new_user = Owners(name=name, phone=phone, email=email, password=password)
        session.add(new_user)
        session.commit()
        print("Registration successful!")
        return new_user
    
    except Exception:
        session.rollback()
        print("Error creating account. Email may already exist.")
        return None





