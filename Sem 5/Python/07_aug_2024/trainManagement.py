import csv

# Load Train Data from a CSV file with error handling
def load_train_data(filename):
    trains = {}
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                train_id = row['Train ID']
                # Convert 'Total Seats' to integer and handle potential conversion errors
                total_seats = int(row['Total Seats'])
                trains[train_id] = {
                    'Train Name': row['Train Name'],
                    'Source Station': row['Source Station'],
                    'Destination Station': row['Destination Station'],
                    'Total Seats': total_seats,
                    'Available Seats': total_seats,
                    'Revenue': 0  # Initialize revenue to 0
                }
            except ValueError as e:
                print(f"Error processing Train ID {row['Train ID']}: {e}. Skipping this train entry.")
    return trains

# Load Passenger Data from a CSV file with error handling
def load_passenger_data(filename):
    passengers = []
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                # Convert 'Number of Tickets' to integer and handle potential conversion errors
                num_tickets = int(row['Number of Tickets'])
                passengers.append({
                    'Passenger Name': row['Passenger Name'],
                    'Train ID': row['Train ID'],
                    'Number of Tickets': num_tickets
                })
            except ValueError as e:
                print(f"Error processing passenger {row['Passenger Name']}: {e}. Skipping this passenger entry.")
    return passengers

# Check if the requested number of seats is available on the given train
def check_seat_availability(trains, train_id, num_tickets):
    if train_id not in trains:
        raise ValueError("Invalid Train ID")  # If the train ID is invalid
    available_seats = trains[train_id]['Available Seats']
    if available_seats < num_tickets:
        raise ValueError(f"Insufficient Seats: Only {available_seats} seats available")  # If there aren't enough seats available
    return True

# Update the train's available seats and total revenue after a successful booking
def update_seat_availability(trains, train_id, num_tickets, fare):
    available_seats = trains[train_id]['Available Seats']
    if num_tickets > available_seats:
        # Inform the user about the maximum seats that can be booked
        print(f"Warning: Only {available_seats} seats available on Train ID {train_id}. Booking all available seats.")
        num_tickets = available_seats
    
    trains[train_id]['Available Seats'] -= num_tickets  # Decrease available seats by the number of tickets booked
    trains[train_id]['Revenue'] += fare  # Increase the train's revenue by the calculated fare

# Generate a report showing train details and available seats
def generate_report_1(trains):
    with open('report_1.txt', 'w') as file:
        file.write("Train Details and Available Seats:\n")
        for train_id, details in trains.items():
            file.write(
                f"Train ID: {train_id}, Train Name: {details['Train Name']}, Source: {details['Source Station']}, Destination: {details['Destination Station']}, Available Seats: {details['Available Seats']}\n")

# Generate a report showing the total revenue earned by each train and the total revenue from all trains
def generate_report_2(trains):
    total_revenue = sum(details['Revenue'] for details in trains.values())
    with open('report_2.txt', 'w') as file:
        file.write("Total Revenue Earned from Each Train:\n")
        for train_id, details in trains.items():
            file.write(f"Train ID: {train_id}, Train Name: {details['Train Name']}, Revenue: {details['Revenue']}\n")
        file.write(f"\nTotal Revenue from All Trains: {total_revenue}\n")

# Calculate the fare based on the number of tickets (Example: Flat rate per ticket)
def calculate_fare(num_tickets):
    return num_tickets * 100  # Example fare rule: 100 currency units per ticket

# Paths for .csv files
trains = load_train_data('/home/rebel/Roger/College/Sem 5/Python/07_aug_2024/trains.csv')  # Load train data from CSV
passengers = load_passenger_data('/home/rebel/Roger/College/Sem 5/Python/07_aug_2024/passengers.csv')  # Load passenger data from CSV

# Main block

for passenger in passengers:
    train_id = passenger['Train ID']
    num_tickets = passenger['Number of Tickets']
    try:
        # Check if seats are available and proceed with booking if they are
        if check_seat_availability(trains, train_id, num_tickets):
            fare = calculate_fare(num_tickets)  
            update_seat_availability(trains, train_id, num_tickets, fare)
            print(f"Booking confirmed for {passenger['Passenger Name']} on Train ID {train_id} for {num_tickets} tickets. Total Fare: {fare}")
    except ValueError as e:
        print(f"Error for {passenger['Passenger Name']}: {e}")

generate_report_1(trains)  
generate_report_2(trains)
