from models import Owners, session

def view_profile(user):
        print(f"""
    --- Profile Info ---
    Name: {user.name}
    Phone: {user.phone}
    Email: {user.email}
    """)

def update_profile(user):

    print("Update Profile (leave blank to skip)")
    new_name = input(f"Name ({user.name}): ") or user.name
    new_phone = input(f"Phone ({user.phone}): ") or user.phone
    new_pass = input("Password (leave blank to keep same): ") or user.password
    user.name = new_name
    user.phone = new_phone
    user.password = new_pass
    session.commit()
    print("Profile updated successfully!")
    return user

def delete_profile(user):

    confirm = input("Are you sure you want to delete your profile? (yes/no): ")
    if confirm.lower() == "yes":
        session.delete(user)
        session.commit()
        print("Profile deleted. Restart program.")
        exit()
    else:
        print("Cancelled.")



