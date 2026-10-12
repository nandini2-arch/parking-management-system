"""Parking Management System - console (menu-based) version."""
import parking_core as pc

USER, PASSWORD = "admin", "admin123"

MENU = """
===== PARKING MANAGEMENT SYSTEM =====
1. Park a vehicle
2. Display parked vehicles
3. Search vehicle
4. Vehicle exit (bill)
5. Update plate number
6. Delete wrong entry
7. Reports
8. Exit
"""


def show(rows):
    if not rows:
        print("No records.")
        return
    print(f"{'Slot':<5}{'Plate':<14}{'Type':<7}{'Entry':<21}{'Exit':<21}Fee")
    for r in rows:
        print(f"{r['slot']:<5}{r['plate']:<14}{r['type']:<7}{r['entry']:<21}{r['exit']:<21}{r['fee']}")


def login():
    for _ in range(3):
        if input("Username: ") == USER and input("Password: ") == PASSWORD:
            return True
        print("Wrong login.")
    return False


def main():
    if not login():
        print("Too many attempts.")
        return
    while True:
        print(MENU)
        choice = input("Choose (1-8): ").strip()
        try:
            if choice == "1":
                r = pc.park(input("Plate: "), input("Type (Bike/Car/Truck): ").title())
                print(f"Parked in slot {r['slot']}")
            elif choice == "2":
                show(pc.active(pc.load()))
            elif choice == "3":
                show(pc.search(input("Plate (or part): ")))
            elif choice == "4":
                r = pc.exit_vehicle(input("Plate: "))
                print(f"Bill for {r['plate']}: Rs {r['fee']}")
            elif choice == "5":
                pc.update_plate(input("Old plate: "), input("New plate: "))
                print("Updated.")
            elif choice == "6":
                pc.delete_entry(input("Plate: "))
                print("Deleted.")
            elif choice == "7":
                for k, v in pc.report().items():
                    print(f"{k.replace('_', ' ').title()}: {v}")
            elif choice == "8":
                print("Goodbye!")
                break
            else:
                print("Please choose 1 to 8.")
        except ValueError as e:
            print("Error:", e)


if __name__ == "__main__":
    main()
