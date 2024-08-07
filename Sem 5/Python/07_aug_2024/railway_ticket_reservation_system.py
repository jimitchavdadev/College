import csv
from train import Train
from passenger import Passenger


class RailwayTicketReservationSystem:
    def __init__(self, trains_file, passengers_file):
        self.trains_file = trains_file
        self.passengers_file = passengers_file
        self.trains = {}
        self.passengers = []

        self.load_train_data()
        self.load_passenger_data()

    def load_train_data(self):
        with open(self.trains_file, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                train_id = row['Train ID']
                train = Train(train_id, row['Train Name'], row['Source Station'],
                              row['Destination Station'], int(row['Total Seats']))
                self.trains[train_id] = train

    def load_passenger_data(self):
        with open(self.passengers_file, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                try:
                    passenger_name = row['Passenger Name']
                    train_id = row['Train ID']
                    num_tickets = int(row['Number of Tickets'])

                    if not passenger_name or not train_id or not num_tickets:
                        raise ValueError("Missing data")

                    passenger = Passenger(passenger_name, train_id, num_tickets)
                    self.passengers.append(passenger)
                except ValueError:
                    print(f"Skipping invalid passenger data: {row}")

    def check_seat_availability(self, train_id, num_tickets):
        if train_id in self.trains:
            return self.trains[train_id].available_seats >= num_tickets
        return False

    def book_tickets(self, passenger_name, train_id, num_tickets):
        if train_id not in self.trains:
            return "Invalid Train ID"

        if not self.check_seat_availability(train_id, num_tickets):
            return "Insufficient seats available"

        self.trains[train_id].book_seats(num_tickets)
        total_fare = self.calculate_fare(train_id, num_tickets)

        # Add the passenger to the list
        self.passengers.append(Passenger(passenger_name, train_id, num_tickets))

        return f"Booking confirmed. Total fare: {total_fare}"

    def calculate_fare(self, train_id, num_tickets):
        # Implement your fare rules here
        # For simplicity, let's assume a flat rate of $10 per ticket
        return num_tickets * 10

    def generate_report_1(self):
        report = "Train Report:\n"
        for train in self.trains.values():
            report += str(train) + '\n'
        return report

    def generate_report_2(self):
        total_revenue = 0
        for passenger in self.passengers:
            total_revenue += self.calculate_fare(passenger.train_id, passenger.num_tickets)

        report = f"Total Revenue: {total_revenue}\n"
        return report
