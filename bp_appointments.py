from models import Owners, Pets, Vets, session
from datetime import datetime

#IMPORTANT when creating an appointment, it is required to convert the date string
# "YYYY-MM-DD" int a python date object

date_format = "%Y-%m-%d" #This will be used to format your date


today = datetime.strptime("2025-08-08", date_format)

def schedule_appointment(current_user):
    print("\n--- Schedule Appointment ---")
    pets = session.query(Pets).filter_by(owner_id=current_user.id).all()
    if not pets:
        print("You have no pets. Add a pet first.\n")
        return
    print("Select a pet:")
    pet_id = choose_from_list_by_id(pets, "pet")
    if pet_id is None:
        return
    pet = session.query(Pets).filter_by(id=pet_id, owner_id=current_user.id).first()
    if not pet:
        print("Invalid pet selection.\n")
        return

    vets = session.query(Vets).all()
    if not vets:
        print("No vets available. Contact admin or add vets to the DB.\n")
        return
    print("Select a vet:")
    vet_id = choose_from_list_by_id(vets, "vet")
    if vet_id is None:
        return
    vet = session.query(Vets).filter_by(id=vet_id).first()
    if not vet:
        print("Invalid vet selection.\n")
        return

    appt_date = parse_date_input("Appointment date (YYYY-MM-DD): ")
    notes = input("Notes (optional): ").strip() or None

    appt = Appointments(pet_id=pet.id, veterinarian_id=vet.id, appointment_date=appt_date, notes=notes, status="Scheduled")
    try:
        session.add(appt)
        session.commit()
        print(f"Appointment scheduled for {pet.name} with {vet.name} on {appt_date}.\n")
    except Exception as e:
        session.rollback()
        print("Failed to schedule appointment:", e)

def view_appointments(current_user):
    print("\n--- My Appointments ---")
    appts = session.query(Appointments).join(Pets).filter(Pets.owner_id == current_user.id).order_by(Appointments.appointment_date).all()
    if not appts:
        print("You have no appointments.\n")
        return []
    for a in appts:
        print(f"ID {a.id}) Pet: {a.pet.name} | Vet: {a.vet.name} | Date: {a.appointment_date} | Status: {a.status} | Notes: {a.notes or 'N/A'}")
    print("")
    return appts

def reschedule_appointment(current_user):
    appts = view_appointments(current_user)
    if not appts:
        return
    try:
        appt_id = int(input("Enter Appointment ID to reschedule: ").strip())
    except ValueError:
        print("Invalid ID.\n")
        return
    appt = session.query(Appointments).join(Pets).filter(Appointments.id == appt_id, Pets.owner_id == current_user.id).first()
    if not appt:
        print("Appointment not found or doesn't belong to you.\n")
        return
    new_date = parse_date_input("New appointment date (YYYY-MM-DD): ")
    appt.appointment_date = new_date
    try:
        session.commit()
        print("Appointment rescheduled.\n")
    except Exception as e:
        session.rollback()
        print("Failed to reschedule appointment:", e)

def complete_appointment(current_user):
    appts = view_appointments(current_user)
    if not appts:
        return
    try:
        appt_id = int(input("Enter Appointment ID to mark as completed: ").strip())
    except ValueError:
        print("Invalid ID.\n")
        return
    appt = session.query(Appointments).join(Pets).filter(Appointments.id == appt_id, Pets.owner_id == current_user.id).first()
    if not appt:
        print("Appointment not found or doesn't belong to you.\n")
        return
    appt.status = "Completed"
    try:
        session.commit()
        print("Appointment marked as completed.\n")
    except Exception as e:
        session.rollback()
        print("Failed to update appointment status:", e)

