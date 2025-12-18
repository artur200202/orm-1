from bp_auth import login, register
from bp_owner import view_profile , update_profile , delete_profile
from bp_pets import view_pets , create_pet , update_pet , delete_pet
from bp_appointments import schedule_appointment, view_appointments,  reschedule_appointment, complete_appointment

def welcome_menu():

    while True:

        print("""

--------- Welcome to Pet Clinic --------

1.) Login

2.) Register

Type 'quit' to exit

""")

        ch = input("Choose: ")



        if ch == "1":

            user = login()

            if user:

                return user

        elif ch == "2":

            user = register()

            if user:

                return user

        elif ch == "quit":

            exit()

        else:

            print("Invalid choice.")





def owner_menu(user):

    while True:

        print("""

----- Manage Profile -----

1.) View Profile

2.) Update Profile

3.) Delete Profile

4.) Back

""")

        c = input("Choose: ")



        if c == "1":

            view_profile(user)

        elif c == "2":

            user = update_profile(user)

        elif c == "3":

            delete_profile(user)

        elif c == "4":

            return

        else:

            print("Invalid choice.")





def pets_menu(user):

    while True:

        print("""

----- My Pets -----

1.) View Pets

2.) Add Pet

3.) Update Pet

4.) Delete Pet

5.) Back

""")

        c = input("Choose: ")



        if c == "1":

            view_pets(user)

        elif c == "2":

            create_pet(user)

        elif c == "3":

            update_pet(user)

        elif c == "4":

            delete_pet(user)

        elif c == "5":

            return

        else:

            print("Invalid choice.")





def appointments_menu(user):

    while True:

        print("""

----- Appointments -----

1.) Schedule Appointment

2.) View Appointments

3.) Reschedule Appointment

4.) Complete Appointment

5.) Back

""")

        c = input("Choose: ")



        if c == "1":

            schedule_appointment(user)

        elif c == "2":

            view_appointments(user)

        elif c == "3":

            reschedule_appointment(user)

        elif c == "4":

            complete_appointment(user)

        elif c == "5":

            return

        else:

            print("Invalid choice.")





# -----------------------------

# MAIN PROGRAM

# -----------------------------

def main():

    print("\nStarting Pet Clinic System...\n")

    current_user = welcome_menu()



    while True:

        print("""

--------- Pet Clinic ---------

1.) Manage Profile

2.) My Pets

3.) My Appointments

""")

        choice = input("Choose: ")



        if choice == "1":

            owner_menu(current_user)

        elif choice == "2":

            pets_menu(current_user)

        elif choice == "3":

            appointments_menu(current_user)

        else:

            print("Invalid input.")





main()