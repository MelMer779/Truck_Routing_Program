# WGUPS Delivery Program
# Melissa Mercado Student ID: 011584997
# This program uses the nearest neighbor approach to deliver all packages


from delivery_system import truck_one, truck_two, truck_three, package_table, distance_between
from hashtable import HashTable
from imported_data import *
from datetime import timedelta


# Displays the details of package
def get_package_details(package):
    truck_info = f"Truck {package.truck}" if package.truck else "Not assigned"

    return (f"Assigned to: {truck_info}|"
            f"Package ID: {package.package_id}|"
            f"Address: {package.address}|"
            f"City: {package.city}|"
            f"State: {package.state}|"
            f"Zip Code: {package.zip_code}|"
            f"Deadline: {package.deadline}|"
            f"Status: {package.status}|")


# Generates package report at a given time, including truck milage
def package_report_at_time(time_input):

    hours, minutes = map(int, time_input.split(":"))
    lookup_time = timedelta(hours=hours, minutes=minutes)

    print(f"\nPACKAGE REPORT AT TIME: {time_input}")

    # Track truck mileage at the given time
    trucks = [truck_one, truck_two, truck_three]
    for truck in trucks:
        truck_mileage = 0.0
        truck_time = truck.depart_time  # Start from truck's departure time
        truck_location = truck.start_address  # Start location of truck

        # Calculates mileage at any given time
        for package_id in truck.delivered:
            package = package_table.search(package_id)

            if package.delivered_time <= lookup_time:  # If package was delivered before input time
                distance = distance_between(truck_location, package.address)  # calculating distance
                truck_mileage += distance
                truck_time += timedelta(hours=distance / truck.speed)  # Adjust truck time
                truck_location = package.address  # Update truck location

        # Display truck details
        print(f"Truck {truck.truck_id}: {truck_mileage:.2f} miles driven by {time_input}")
    #Display Package Status Report
    print("\nPACKAGE STATUS REPORT:")
    for package_id in range(1, 41):  # Assuming package IDs are from 1 to 40
        package = package_table.search(package_id)

        if package:
            status_report = package.package_status(lookup_time)
            print(status_report)

# This function searches for a package by its ID in the package table.
# If found, it prompts the user to enter a time (HH:MM format) to check the package's status.
# The status is determined on where the package is: at the hub, en route, or delivered.
# If the input format for the time or package ID is invalid, an error message is displayed.
def lookup_package(package_table, package_id):
    try:
        package_id = int(package_id)
        package = package_table.search(package_id)
        # Checks if the package was found
        if package:
            time_input = input("\nEnter time (HH:MM in 24-hour format) to check status: ")
            try:
                hours, minutes = map(int, time_input.split(':'))
                lookup_time = timedelta(hours=hours, minutes=minutes)

                # Check package status at the given time
                if package.delivered_time and lookup_time >= package.delivered_time:
                    package.status = f"Delivered at {package.delivered_time}"
                elif package.departure_time and package.delivered_time and package.departure_time <= lookup_time < package.delivered_time:
                    package.status = "En Route"
                elif package.departure_time and lookup_time < package.departure_time:
                    package.status = "At Hub"

                status_report = package.package_status(lookup_time)

                print("\nPackage Found:")
                print("-" * 50)
                print(status_report)

            except ValueError:
                print("Invalid time format. Please use HH:MM format (24-hour).")
        else:
            print(f"\nNo package found with ID {package_id}")
    except ValueError:
        print("Invalid package ID. Please enter a number.")


def main():
    # Creates hash table and insert packages
    package_table = HashTable()
    for package in packages:
        package_table.insert(package)


    # UI for user input
    while True:
        print("\nWGUPS Package Tracking System")
        print("1. Report for All Packages")
        print("2. Single Package Search")
        print("3. Exit Program")

        choice = input("\nSelect an option (1-3): ")

        if choice == '1':
            time_input = input("\nEnter time (HH:MM in 24-hour format): ")
            package_report_at_time(time_input)

        elif choice == '2':
            package_id = input("\nEnter package ID: ")
            lookup_package(package_table, package_id)

        elif choice == '3':
            print("\nThank you for using this program! K Byeeeeeeee")
            break

        else:
            print("\nInvalid option. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()