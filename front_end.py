from bp_auth import login, register
from bp_owner import view_profile, update_profile, delete_profile
from bp_pets import view_pets, create_pet, update_pet, delete_pet
from bp_appointments import schedule_appointment, view_appointments, reschedule_appointment, complete_appointment

def welcome_menu():
    current_user = None
    while True:
        print("""
--------- Welcome to Pet Clinic --------
        1.) Login
        2.) Register
""")
        choice = input("select (1 or 2) or quit: ")
        if choice == '1':
            current_user = login()
            if current_user:
                return current_user

        elif choice == '2':
            current_user = register()
            if current_user:
                return current_user

        elif choice == 'quit':
            return 
        else:
            print("Invalid response please try again.")

def owner_menu(current_user):
    while True:
        print("""
    1.) View Profile
    2.) Update Profile
    3.) Delete Profile
    4.) Back""")
        choice = input("choose 1-3: ")
        if choice == '1':
            #view profile funtion should display the current users info
            view_profile(current_user)
        elif choice == '2':
            #update profile function, and returns the updated user
            #on success, should set current_user to the user that is returned
            current_user = update_profile(current_user)
        elif choice == '3':
            #delete the current users account
            current_user = delete_profile(current_user)
            main()
        elif choice == '4':
            return #Goes back to main menu
        else:
            print("Invalid Selection.")

def pets_menu(current_user):
    while True:
        print("""
1.) View my Pets
2.) Create Pet
3.) Update Pet
4.) Delete Pet
5.) Back""")
        choice = input("choose 1-5: ")
        if choice == '1':
            #function that displays the current user's pets
            view_pets(current_user)
        elif choice == '2':
            #function to create a new pet linked to the current user, add to db
            create_pet(current_user)
        elif choice == '3':
            #function to update a particular pet 
            update_pet(current_user)
        elif choice == '4':
            #function to delete a particuler pet
            delete_pet(current_user)
        elif choice == '5':
            return current_user 
        else:
            print("Invalid Selection.")

def appointments_menu(current_user):
    while True:
        print("""
1.) schedule appointment
2.) view appointments
3.) reschdule appointment
4.) Complete appointment
5.) Back
""")
        choice = input("choose 1-5: ")
        if choice == '1':
            schedule_appointment(current_user)
        elif choice == '2':
            view_appointments(current_user)
        elif choice == '3':
            reschedule_appointment(current_user)
        elif choice == '4':
            complete_appointment(current_user)
        elif choice =='5':
            return
        else:
            print("Invalid selection. Please try again.")


def main():
    
    current_user = welcome_menu() 

   
    
    if current_user:
        while True:
            print("""
        --------- Pet Clinic --------
        1.) Manage Profile
        2.) My Pets
        3.) My Appointments
        4.) Logout
        """)
            choice = input("choose 1-3: ")
            if choice == '1':
                owner_menu(current_user)
            elif choice == '2':
                pets_menu(current_user)
            elif choice == '3':
                appointments_menu(current_user)
            elif choice == '4':
                print("Logging out!")
                main()
            else:
                print("Invalid Selection.")
    

main()
    