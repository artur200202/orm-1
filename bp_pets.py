from models import Pets, session

def view_pets(current_user):
    pets = session.query(Pets).filter_by(owner_id=current_user.id).all()
    if not pets:
        print("You have no pets.\n")
        return []
    print("\n--- Your Pets ---")
    for p in pets:
        print(f"{p.id}) {p.name} - {p.species} - Breed: {p.breed or 'N/A'} - Age: {p.age if p.age is not None else 'N/A'}")
    print("")
    return pets

def create_pet(current_user):
    print("\n--- Add New Pet ---")
    name = input("Pet name: ").strip()
    species = input("Species (e.g., Dog, Cat): ").strip()
    breed = input("Breed (optional): ").strip() or None
    age_input = input("Age (integer, optional): ").strip()
    age = None
    if age_input:
        try:
            age = int(age_input)
        except ValueError:
            print("Invalid age input. Setting age to None.")
            age = None
    new_pet = Pets(name=name, species=species, breed=breed, age=age, owner_id=current_user.id)
    try:
        session.add(new_pet)
        session.commit()
        print(f"Pet '{new_pet.name}' added.\n")
    except Exception as e:
        session.rollback()
        print("Failed to add pet:", e)

def update_pet(current_user):
    pets = view_pets(current_user)
    if not pets:
        return
    pet_id = choose_from_list_by_id(pets, "pet")
    if pet_id is None:
        return
    pet = session.query(Pets).filter_by(id=pet_id, owner_id=current_user.id).first()
    if not pet:
        print("Pet not found or does not belong to you.\n")
        return
    print("\n--- Update Pet (leave blank to keep current) ---")
    pet.name = input(f"Name ({pet.name}): ").strip() or pet.name
    pet.species = input(f"Species ({pet.species}): ").strip() or pet.species
    pet.breed = input(f"Breed ({pet.breed or 'N/A'}): ").strip() or pet.breed
    age_input = input(f"Age ({pet.age if pet.age is not None else 'N/A'}): ").strip()
    if age_input:
        try:
            pet.age = int(age_input)
        except ValueError:
            print("Invalid age input - keeping previous value.")
    try:
        session.commit()
        print("Pet updated.\n")
    except Exception as e:
        session.rollback()
        print("Failed to update pet:", e)

def delete_pet(current_user):
    pets = view_pets(current_user)
    if not pets:
        return
    pet_id = choose_from_list_by_id(pets, "pet")
    if pet_id is None:
        return
    pet = session.query(Pets).filter_by(id=pet_id, owner_id=current_user.id).first()
    if not pet:
        print("Pet not found or does not belong to you.\n")
        return
    confirm = input(f"Are you sure you want to delete '{pet.name}'? (yes/no): ").strip().lower()
    if confirm == 'yes':
        try:
            session.delete(pet)
            session.commit()
            print("Pet deleted.\n")
        except Exception as e:
            session.rollback()
            print("Failed to delete pet:", e)
    else:
        print("Delete cancelled.\n")




