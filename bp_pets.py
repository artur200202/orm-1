from models import Pets, session

#view pets function
#Takes in current user
#Loops over all of the current users pets (use the .pets relationship attribute to get list of pets)
#prints the pets info
def view_pets(current_user):

    print("Your Pets:")
    for pet in current_user.pets:
        print(f"- Name: {pet.name}, Species: {pet.species}, Age: {pet.age}")

#Create pets function
#gets pets info from user
#create Pets() from the info
#print new pet
def create_pet(current_user):
    print("Add a New Pet")
    name = input("Enter pet's name: ")
    species = input("Enter pet's species: ")
    age = input("Enter pet's age: ")

    new_pet = Pets(name=name, species=species, age=age, owner_id=current_user.id)
    session.add(new_pet)
    session.commit()

    print(f"Pet '{new_pet.name}' added successfully!")

#Update pets function
#display current users pets
#allow them to select a pet BY NAME
#query that pet from the database
#get updated info from the user
#set that pets info to the new info
#commit changes
#print new pet info
def update_pet(current_user):
    view_pets(current_user)
    pet_name = input("Enter the name of the pet you want to update: ")

    pet = session.query(Pets).filter_by(name=pet_name, owner_id=current_user.id).first()
    if not pet:
        print(f"No pet found with name '{pet_name}'.")
        return

    print("Enter new info (leave blank to keep current value):")
    new_name = input(f"New name (current: {pet.name}): ") or pet.name
    new_species = input(f"New species (current: {pet.species}): ") or pet.species
    new_age = input(f"New age (current: {pet.age}): ") or pet.age

    pet.name = new_name
    pet.species = new_species
    pet.age = new_age
    session.commit()

    print(f"Pet '{pet.name}' updated successfully!")

#Delete pets function
#display current users pets
#allow them to select a pet BY NAME
#query that pet from the database
#Ask user if they are sure they want to delete this pet
#delete pet from the session
#commit changes
def delete_pet(current_user):
    view_pets(current_user)
    pet_name = input("Enter the name of the pet you want to delete: ")

    pet = session.query(Pets).filter_by(name=pet_name, owner_id=current_user.id).first()

    confirm = input(f"Are you sure you want to delete '{pet.name}'? (y/n): ")
    if confirm.lower() == "y":
        session.delete(pet)
        session.commit()
        print(f"Pet '{pet.name}' has been deleted.")
    else:
        print("Delete canceled.")