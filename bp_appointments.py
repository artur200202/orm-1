from models import Owners, Pets, Vets, session
from datetime import datetime

DATE_FORMAT = "%Y-%m-%d"

def schedule_appointment(user):
    view_pets(user)
    pet_id = int(input("Select pet ID: "))
    pet = session.query(Pets).filter_by(id=pet_id, owner_id=user.id).first()
    if not pet:
        print("Invalid pet.")
        return
    print("\n--- Available Vets ---")
    vets = session.query(Vets).all()
    for v in vets:
        print(f"{v.id}) {v.name} - {v.specialization}")

    vet_id = int(input("Choose vet ID: "))
    vet = session.query(Vets).filter_by(id=vet_id).first()
    if not vet:
        print("Invalid vet.")
        return
    date_str = input("Appointment date (YYYY-MM-DD): ")
    appt_date = datetime.strptime(date_str, DATE_FORMAT).date()
    notes = input("Notes: ")
    new_appt = Appointments(

        pet_id=pet.id,
        veterinarian_id=vet.id,
        appointment_date=appt_date,
        notes=notes,
        status="Scheduled"
    )

    session.add(new_appt)
    session.commit()
    print("Appointment scheduled!")


def view_appointments(user):
    print("\n--- Your Appointments ---")
    found = False
    for pet in user.pets:
        for appt in pet.appointments:
            found = True
            print(f"""

    Appointment ID: {appt.id}
    Pet: {pet.name}
    Vet: {appt.vet.name}
    Date: {appt.appointment_date}
    Status: {appt.status}
    Notes: {appt.notes}
    """)
    if not found:
        print("No appointments.")

def reschedule_appointment(user):
    view_appointments(user)
    appt_id = int(input("Enter appointment ID to reschedule: "))
    appt = session.query(Appointments).join(Pets).filter(
        Appointments.id == appt_id,
        Pets.owner_id == user.id
    ).first()

    if not appt:
        print("Invalid appointment.")
        return
    new_date_str = input("New date (YYYY-MM-DD): ")
    new_date = datetime.strptime(new_date_str, DATE_FORMAT).date()
    appt.appointment_date = new_date
    session.commit()

    print("Appointment rescheduled!")

def complete_appointment(user):
    view_appointments(user)
    appt_id = int(input("Enter appointment ID to complete: "))
    appt = session.query(Appointments).join(Pets).filter(
        Appointments.id == appt_id,
        Pets.owner_id == user.id
    ).first()

    if not appt:
        print("Invalid appointment.")
        return
    
    appt.status = "Completed"
    session.commit()

    print("Appointment marked as completed!")

