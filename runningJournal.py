import datetime

def new_journal_entry(entry_filename, entry_day, entry_day_of_month, entry_month, entry_year):
    with open(entry_filename, 'w') as entry_file:
        entry_file.write(f"Running entry for {entry_day} {entry_day_of_month} {entry_month} {entry_year}.\n")

        print("How long in minutes did you run for?")
        time_in_minutes = input()
        entry_file.write(f"Today's run took {time_in_minutes} minutes.\n")

        print("How far in miles did you run?")
        distance_in_miles = input()
        entry_file.write(f"I ran {distance_in_miles} miles.\n")

        distance_in_km = float(distance_in_miles) * 1.60934
        print(f"You ran {distance_in_km} km, this is saved in your entry.")
        entry_file.write(f"I ran {distance_in_km} km\n")

        pace(time_in_minutes, distance_in_miles, entry_file, distance_in_km)

def pace(time_in_minutes, distance_in_miles, entry_file, distance_in_km):
    while True:
        pace_unit = input("Would you like your pace to be worked out in miles or km? (miles/km) ")
        if pace_unit == "miles":
            pace_in_miles = float(time_in_minutes) / float(distance_in_miles)
            entry_file.write(f"I ran at a pace of {pace_in_miles} min/mile. ")
            break
        elif pace_unit == "km":
            pace_in_km = float(time_in_minutes) / float(distance_in_km)
            entry_file.write(f"I ran at a pace of {pace_in_km} min/km. ")
            break
        else: 
            print("That is not a valid answer. Please select again.")

def main():
    print("Welcome to your Daily Running Journal!")

    today = datetime.date.today()
    entry_date = today.strftime("%d_%m_%Y")
    entry_filename = f"{entry_date}'s Entry.txt"
    entry_day = today.strftime("%a")
    entry_day_of_month = today.strftime("%d")
    entry_month = today.strftime("%B")
    entry_year = today.strftime("%Y")

    while True:
        print("\nMenu:")
        print("1. Write a new journal entry")
        print("2. Quit")

        choice = input("Select an option: ")

        if choice == '1':
            new_journal_entry(entry_filename, entry_day, entry_day_of_month, entry_month, entry_year)
            print(f"New running entry saved to {entry_filename}")
        elif choice == '2':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()