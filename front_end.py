from bp_auth import login, register
from bp_owner import view_profile , update_profile , delete_profile
from bp_pets import view_pets , create_pet , update_pet , delete_pet
from bp_appointments schedule_appointment, view_appointments,  reschedule_appointment, complete_appointment
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
            #login function
            current_user= login()
            

        elif choice == '2':
            #register function
            current_user= register()
            #should set the current user on successful register
           
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
            view_profile()
        elif choice == '2':
            update_profile()
        elif choice == '3':
            delete_profile()
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
           view_pets()
        elif choice == '2':
            create_pet()
        elif choice == '3':
            update_pet()
        elif choice == '4':
            delete_pet()
        elif choice == '5':
            return
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
            schedule_appointment()
        elif choice == '2':
            view_appointments()
        elif choice == '3':
            reschedule_appointment()
        elif choice == '4':
            complete_appontment()
        elif choice =='5':
            return


def main():
    
    current_user = welcome_menu() 

    #After you test you login and register functions, it might be more efficient
    #to set current_user to a user in your db so you don't have to log in everytime
    #you want to test something.
    
    if current_user:
        while True:
            print("""
        --------- Pet Clinic --------
        1.) Manage Profile
        2.) My Pets
        3.) My Appointments
        """)
            choice = input("choose 1-3: ")
            if choice == '1':
                owner_menu(current_user)
            elif choice == '2':
                pets_menu(current_user)
            elif choice == '3':
                appointments_menu(current_user)
            else:
                print("Invalid Selection.")
    

main()
    
