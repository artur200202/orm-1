from models import Owners, session #Need the Users model to create and search for users
#need the sesssion to add users to our db



#Create Login function
def login():
    email = input("Enter email: ")
    password = input("Enter password: ")

    owner = session.query(Owners).filter_by(email=email).first()

    if owner is None:
        print("No user found with that email.")
        return None

    if owner.password != password:
        print("Incorrect password.")
        return None

    print(f"Welcome back, {owner.name}!")
    return owner
#get email and password from user
#check database for owner with the given email
#if you find an owner, check if the found owners password is the same as the given password
#if so return user


#Create Register function
def register():
    print("\n--- Create an Account ---")
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    password = input("Password: ")

    try:
        new_owner = Owners(
            name=name,
            phone=phone,
            email=email,
            password=password
        )
        session.add(new_owner)
        session.commit()
        print("Account created successfully!")
        return new_owner

    except Exception as e:
        session.rollback()
        print("Error: That email is already taken.")
        return None
#get all info required to create an owner from the user
#try and create an Owner from the info (will fail if email is already in user)
#if you succeed return user
#except error and print message


