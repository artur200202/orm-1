from models import Owners, Pets, Vets, session, Appointments
from datetime import datetime

date_format = "%Y-%m-%d" #This will be used to format your date


today = datetime.strptime("2025-08-08", date_format)



def schedule_appointment(current_user):
    # Show pets
    print("\nYour Pets:")
    for pet in current_user.pets:
        print(f"- {pet.name} ({pet.species})")

    pet_name = input("Enter the pet's name for the appointment: ")
    pet = session.query(Pets).filter_by(name=pet_name, owner_id=current_user.id).first()

    if not pet:
        print("Pet not found.")
        return

    # Show vets
    vets = session.query(Vets).all()
    print("\nAvailable Vets:")
    for vet in vets:
        print(f"{vet.id}. {vet.name} ({vet.specialization})")

    vet_id = input("Enter the vet ID to schedule with: ")
    vet = session.query(Vets).filter_by(id=vet_id).first()

    if not vet:
        print("Vet not found.")
        return

    # Get appointment details
    date_str = input("Enter appointment date (YYYY-MM-DD): ")
    try:
        appointment_date = datetime.strptime(date_str, date_format).date()
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD.")
        return

    notes = input("Enter notes (optional): ")

    # Create appointment
    new_appointment = Appointments(
        pet_id=pet.id,
        veterinarian_id=vet.id,
        appointment_date=appointment_date,
        notes=notes,
        status="Scheduled"
    )
    session.add(new_appointment)
    session.commit()
    print(f"Appointment scheduled for {pet.name} with Dr. {vet.name} on {appointment_date}")


#view appts
def view_appointments(current_user):
    """View all appointments for the current user's pets."""
    if not current_user.pets:
        print("You don’t have any pets.")
        return

    print("Your Appointments:")
    for pet in current_user.pets:
        for appt in pet.appointments:
            vet = session.query(Vets).get(appt.veterinarian_id)
            print(f"ID: {appt.id} | Pet: {pet.name} | Vet: {vet.name} | Date: {appt.appointment_date} | Status: {appt.status}")
    print()


def reschedule_appointment(current_user):
    view_appointments(current_user)

    appt_id = input("Enter the appointment ID to reschedule: ")
    appt = session.query(Appointments).get(appt_id)

    if not appt:
        print("Appointment not found.")
        return

    new_date_str = input("Enter new appointment date (YYYY-MM-DD): ")
    try:
        new_date = datetime.strptime(new_date_str, date_format).date()
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD.")
        return

    appt.appointment_date = new_date
    session.commit()
    print(f"Appointment {appt.id} rescheduled to {new_date}")

#Complete appointments
#Show appointments with ids (Loop over current user pets, loop over each pets appointments e.g nested loop)
#query the appointment by id
#change appointment.status to 'complete"
#print success message
def complete_appointment(current_user):
    view_appointments(current_user)

    appt_id = input("Enter the appointment ID to mark as completed: ")
    appt = session.query(Appointments).get(appt_id)

    if not appt:
        print("Appointment not found.")
        return

    appt.status = "Completed"
    session.commit()
    print(f"Appointment {appt.id} marked as completed.")