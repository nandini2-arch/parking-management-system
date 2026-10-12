# Product 24: Parking Management System

## Problem Statement
Parking lots often track vehicles on paper. This causes wrong bills, lost records and no idea which slots are free. This product records every vehicle, gives it a slot, and bills it when it leaves.

## Objectives
- Park and release vehicles quickly
- Never give one slot to two vehicles
- Calculate fees automatically
- Save all data in a file so nothing is lost
- Show simple reports

## Users
Parking attendant (admin) and parking owner.

## Requirements
**Functional:** login, park vehicle, display parked vehicles, search, exit and bill, update plate, delete wrong entry, save/load CSV, reports.

**Non-functional:** easy menu, wrong input never crashes the program, data survives restart.

**Input:** plate number, vehicle type. **Output:** slot number, bill, reports.

## Rules
| Vehicle | Rate per hour |
| --- | --- |
| Bike | Rs 10 |
| Car | Rs 20 |
| Truck | Rs 40 |

- Hours are rounded up, minimum 1 hour
- Total slots: 10 (change `TOTAL_SLOTS`)
- Plate: 4 to 12 letters/digits, no duplicates
- Login: `admin` / `admin123`

## Modules
Login, Park, Display, Search, Exit & Bill, Update, Delete, File Handling (CSV), Exception Handling, Reports.

## Menu
1. Park a vehicle
2. Display parked vehicles
3. Search vehicle
4. Vehicle exit (bill)
5. Update plate number
6. Delete wrong entry
7. Reports
8. Exit

## Flowchart (main idea)
Start → Login → (wrong 3 times → stop) → Show menu → Choose option → Do task → back to menu → Option 8 → End

## 10-Lab Plan
| Lab | Work | Deliverable |
| --- | --- | --- |
| 1 | Requirements | Problem statement, module list |
| 2 | Flowchart and menu | Flowchart, menu design |
| 3 | Login + main menu | Running menu |
| 4 | Park and display | Add, Display, Search |
| 5 | Update and delete | Working CRUD |
| 6 | CSV file handling | Save and load |
| 7 | Exception handling | Input checks |
| 8 | Reports | Summary report |
| 9 | Testing and documentation | Test cases, manual |
| 10 | Demo and viva | Final product |

## Team Roles (5 students)
1. Leader: requirements, flowchart
2. Menu, functions, park/exit
3. Search, update, delete, reports
4. CSV and exception handling
5. Testing, documentation, presentation

## Test Cases
| Test | Input | Expected |
| --- | --- | --- |
| Park car | AP39AB1234, Car | Slot 1 given |
| Same plate again | AP39AB1234 | "already parked" |
| Bad plate | A1 | "4-12 letters/digits" |
| Wrong type | Cycle | "Type must be..." |
| Lot full | 11th vehicle | "Parking is full" |
| Exit after 30 min (car) | AP39AB1234 | Rs 20 |
| Exit after 2h 10m (car) | AP39AB1234 | Rs 60 |
| Unknown plate exit | ZZ9999 | "Vehicle not found" |
| Wrong login x3 | bad password | Program stops |

## Viva Questions
- Why use a CSV file?
- How do you stop two cars sharing a slot?
- Why do we use try/except?
- How is the fee calculated?

## How to Run
**Console:** `python main.py`

**Website:** `pip install flask`, then `python app.py`, open http://127.0.0.1:5000

## Files
- `parking_core.py` – all logic and file handling
- `main.py` – console menu
- `app.py` – website
- `parking.csv` – created automatically
