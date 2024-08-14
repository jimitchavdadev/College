import csv

# Load Train Data from a CSV file
def load_train_data(filename):
    trains = {}
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            train_id = row['Train ID']
            # Store train details including name, source, destination, total seats, available seats, and initial revenue
            trains[train_id] = {
                'Train Name': row['Train Name'],
                'Source Station': row['Source Station'],
                'Destination Station': row['Destination Station'],
                'Total Seats': int(row['Total Seats']),
                'Available Seats': int(row['Total Seats']),
                'Revenue': 0  # Initialize revenue to 0
            }
    return trains

# Load Passenger Data from a CSV file
def load_passenger_data(filename):
    passengers = []
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Store each passenger's name, train ID, and the number of tickets they want to book
            passengers.append({
                'Passenger Name': row['Passenger Name'],
                'Train ID': row['Train ID'],
                'Number of Tickets': int(row['Number of Tickets'])
            })
    return passengers

# Check if the requested number of seats is available on the given train
def check_seat_availability(trains, train_id, num_tickets):
    if train_id not in trains:
        raise ValueError("Invalid Train ID")  # Raise an error if the train ID is invalid
    if trains[train_id]['Available Seats'] < num_tickets:
        raise ValueError("Insufficient Seats")  # Raise an error if there aren't enough seats available
    return True

# Update the train's available seats and total revenue after a successful booking
def update_seat_availability(trains, train_id, num_tickets, fare):
    trains[train_id]['Available Seats'] -= num_tickets  # Decrease available seats by the number of tickets booked
    trains[train_id]['Revenue'] += fare  # Increase the train's revenue by the calculated fare

# Generate a report showing train details and available seats
def generate_report_1(trains):
    with open('report_1.txt', 'w') as file:
        file.write("Train Details and Available Seats:\n")
        for train_id, details in trains.items():
            file.write(f"Train ID: {train_id}, Train Name: {details['Train Name']}, Source: {details['Source Station']}, Destination: {details['Destination Station']}, Available Seats: {details['Available Seats']}\n")

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

trains = load_train_data('/home/rebel/Roger/College/Sem 5/Python/07_aug_2024/trains.csv')  # Load train data from CSV
passengers = load_passenger_data('/home/rebel/Roger/College/Sem 5/Python/07_aug_2024/passengers.csv')  # Load passenger data from CSV

for passenger in passengers:
    train_id = passenger['Train ID']
    num_tickets = passenger['Number of Tickets']
    try:
        # Check if seats are available and proceed with booking if they are
        if check_seat_availability(trains, train_id, num_tickets):
            fare = calculate_fare(num_tickets)  # Calculate the total fare
            update_seat_availability(trains, train_id, num_tickets, fare)  # Update seat availability and revenue
            print(f"Booking confirmed for {passenger['Passenger Name']} on Train ID {train_id} for {num_tickets} tickets. Total Fare: {fare}")
    except ValueError as e:
        print(f"Error for {passenger['Passenger Name']}: {e}")  # Handle errors, such as invalid train ID or insufficient seats

generate_report_1(trains)  # Generate the first report (train details and available seats)
generate_report_2(trains)  # Generate the second report (total revenue earned)
