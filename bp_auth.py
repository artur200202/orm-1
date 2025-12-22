from models import Owners, session 
#Need the Users model to create and search for users
#need the sesssion to add users to our db



def login():
    email = input("Enter email: ")
    password = input("Enter password: ")
    user = session.query(Owners).filter_by(email=email).first()
    if not user:
        print("Email not found")
        return None
    if user.password != password:
        print("Incorrect password.")
        return None
    return user



def register():
    name = input("Enter your name: ")
    phone = input("Enter your phone number: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    user = Owners(name=name, phone=phone, email=email, password=password)
    session.add(user)
    session.commit()
    print(f"Registration successful! Welcome, {user.name}.")
    return user

