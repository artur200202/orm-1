from models import Pets, session

def view_pets(user):
    print("\n--- Your Pets ---")
    if not user.pets:
        print("No pets found.")
        return
    for pet in user.pets:
        print(f"{pet.id}) {pet.name} - {pet.species}, {pet.breed}, Age: {pet.age}")

def create_pet(user):
    name = input("Pet Name: ")
    species = input("Species: ")
    breed = input("Breed: ")
    age = int(input("Age: "))
    new_pet = Pets(name=name, species=species, breed=breed, age=age, owner_id=user.id)
    session.add(new_pet)
    session.commit()
    print("Pet added successfully!")

def update_pet(user):

    view_pets(user)
    pet_id = int(input("Enter pet ID to update: "))
    pet = session.query(Pets).filter_by(id=pet_id, owner_id=user.id).first()

    if not pet:
        print("Invalid pet selection.")
        return
    pet.name = input(f"Name ({pet.name}): ") or pet.name
    pet.species = input(f"Species ({pet.species}): ") or pet.species
    pet.breed = input(f"Breed ({pet.breed}): ") or pet.breed
    age_input = input(f"Age ({pet.age}): ")
    pet.age = int(age_input) if age_input else pet.age
    session.commit()
    print("Pet updated!")

def delete_pet(user):
    view_pets(user)
    pet_id = int(input("Enter pet ID to delete: "))
    pet = session.query(Pets).filter_by(id=pet_id, owner_id=user.id).first()
    if not pet:
        print("Invalid pet ID.")
        return
    confirm = input("Delete this pet? (yes/no): ")
    if confirm.lower() == "yes":
        session.delete(pet)
        session.commit()
        print("Pet deleted.")
    else:
        print("Cancelled.")







