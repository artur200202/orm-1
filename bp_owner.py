from models import Owners, session

def view_profile(current_user):
    print(f"""--- My Profile ---\n Name: {current_user.name} \n Phone: {current_user.phone}\n Email: {current_user.email}""")

#Update profile function
def update_profile(current_user):
    print("\n--- Update Profile ---")
    print("Leave field empty to keep current value.\n")

    new_name = input(f"Name ({current_user.name}): ") or current_user.name
    new_phone = input(f"Phone ({current_user.phone}): ") or current_user.phone
    new_email = input(f"Email ({current_user.email}): ") or current_user.email
    new_password = input("Password (leave empty to keep same): ") or current_user.password

    current_user.name = new_name
    current_user.phone = new_phone
    current_user.email = new_email
    current_user.password = new_password

    session.commit()

    print("\nProfile updated.\n")
    return current_user


def delete_profile(current_user):
    confirm = input("Are you sure you want to delete your account? (yes/no): ")
    if confirm.lower() == 'yes':
        session.delete(current_user)
        session.commit()
        print("Your account has been deleted.\n")
        return True
    return False
