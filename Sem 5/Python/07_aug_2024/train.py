class Train:
    def __init__(self, train_id, name, source, destination, total_seats):
        self.train_id = train_id
        self.name = name
        self.source = source
        self.destination = destination
        self.total_seats = total_seats
        self.available_seats = total_seats

    def book_seats(self, num_tickets):
        if num_tickets <= self.available_seats:
            self.available_seats -= num_tickets
            return True
        return False

    def __str__(self):
        return (f"Train ID: {self.train_id}, Train Name: {self.name}, "
                f"Source: {self.source}, Destination: {self.destination}, "
                f"Total Seats: {self.total_seats}, Available Seats: {self.available_seats}")
