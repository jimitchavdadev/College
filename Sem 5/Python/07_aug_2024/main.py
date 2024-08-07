from railway_ticket_reservation_system import RailwayTicketReservationSystem


def main():
    trains_file = 'trains.csv'
    passengers_file = 'passengers.csv'

    system = RailwayTicketReservationSystem(trains_file, passengers_file)
    print(system.generate_report_1())
    print(system.generate_report_2())

    # Book a ticket
    print(system.book_tickets('John Doe', 'T001', 2))

    # Generate updated reports
    with open("report1.txt","w") as file:
        file.write(system.generate_report_1())

    with open("report2.txt","w") as file:
        file.write(system.generate_report_2())


if __name__ == "__main__":
    main()
