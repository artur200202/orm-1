from models import Owners, session

#View profile function
def view_profile(current_user):
    print(f"Name: {current_user.name}\nPhone: {current_user.phone}\nEmail: {current_user.email}")


#Update profile function
#dsiplays current user info
#allows user to update any of the fields
#commits changes 
#shows changes and returns update current_user
def update_profile(current_user):
    print("Update Profile: (leave blank to keep current)")
    current_user.name = input(f"New name: ") or current_user.name
    current_user.phone = input(f"New phone: ") or current_user.phone
    current_user.email = input(f"New email: ") or current_user.email
    current_user.password = input("New password: ") or current_user.password
    session.commit()
    print("Profile updated successfully!")
    return current_user

def delete_profile(current_user):
    confirm = input("Are you sure you want to delete your account? (y or n): ")
    if confirm.lower() == 'y':
        session.delete(current_user)
        session.commit()
        print("Your account has been deleted.")
        return None
    return current_user


