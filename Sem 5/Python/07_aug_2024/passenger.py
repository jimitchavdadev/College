class Passenger:
    def __init__(self, name, train_id, num_tickets):
        self.name = name
        self.train_id = train_id
        self.num_tickets = num_tickets

    def __str__(self):
        return f"Passenger Name: {self.name}, Train ID: {self.train_id}, Number of Tickets: {self.num_tickets}"
