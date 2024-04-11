class Ticket:
    counter = 2000
    open_tickets = 0
    closed_tickets = 0

    def __init__(self, staff_id, creator_name, contact_email, description):
        self.ticket_number = Ticket.counter
        Ticket.counter += 1
        self.staff_id = staff_id
        self.creator_name = creator_name
        self.contact_email = contact_email
        self.description = description
        self.response = "Not Yet Provided"
        self.status = "Open"
        Ticket.open_tickets += 1

    def resolve_password_change(self):
        if "Password Change" in self.description:
            new_password = self.generate_password()
            self.response = f"New password: {new_password}"
            self.status = "Closed"
            Ticket.open_tickets -= 1
            Ticket.closed_tickets += 1
            return new_password
        return None

    def provide_response(self, response):
        self.response = response
        self.status = "Closed"
        Ticket.open_tickets -= 1
        Ticket.closed_tickets += 1

    def reopen_ticket(self):
        self.status = "Reopened"
        Ticket.open_tickets += 1
        Ticket.closed_tickets -= 1

    def display_ticket(self):
        print(f"Ticket Number: {self.ticket_number}")
        print(f"Creator Name: {self.creator_name}")
        print(f"Staff ID: {self.staff_id}")
        print(f"Contact Email: {self.contact_email}")
        print(f"Description: {self.description}")
        print(f"Response: {self.response}")
        print(f"Status: {self.status}")
        print()

    @staticmethod
    def ticket_stats():
        print(f"Number of Tickets Submitted: {Ticket.counter - 2000}")
        print(f"Number of Resolved Tickets: {Ticket.closed_tickets}")
        print(f"Number of Open Tickets: {Ticket.open_tickets}")

    def generate_password(self):
        return self.staff_id[:2] + self.creator_name[:3]


def submit_ticket():
    staff_id = input("Enter your staff ID: ")
    creator_name = input("Enter your name: ")
    contact_email = input("Enter your contact email: ")

    password_change = input("Is this a password change request? (yes/no): ")
    if password_change.lower() == "yes":
        description = "Password Change"
    else:
        description = input("Enter the description of the issue: ")
        
    new_ticket = Ticket(staff_id, creator_name, contact_email, description)
    new_password = new_ticket.resolve_password_change()  # Resolve password change requests upon submitting a ticket
    print("Ticket submitted successfully!")
    if new_password:
        print(f"New password generated: {new_password}")
    print()

    # Add the new ticket to the sample tickets
    sample_tickets.append(new_ticket)


def respond_to_ticket():
    ticket_number = int(input("Enter ticket number: "))
    ticket = get_ticket_by_number(ticket_number)
    if ticket:
        response = input("Provide a response to the ticket: ")
        ticket.provide_response(response)
        print("Response provided successfully!")
    else:
        print("Ticket not found.")
    print()


def display_ticket_info():
    ticket_number = int(input("Enter ticket number: "))
    ticket = get_ticket_by_number(ticket_number)
    if ticket:
        print("Ticket Information:")
        ticket.display_ticket()
    else:
        print("Ticket not found.")
    print()


def reopen_ticket():
    ticket_number = int(input("Enter ticket number: "))
    ticket = get_ticket_by_number(ticket_number)
    if ticket:
        ticket.reopen_ticket()
        print("Ticket reopened successfully!")
    else:
        print("Ticket not found.")
    print()


def show_tickets():
    print("List of Tickets:")
    for ticket in sample_tickets:
        ticket.display_ticket()
    print()


def display_ticket_stats():
    Ticket.ticket_stats()
    print()


def main():
    while True:
        print("\nHelp Desk Ticketing System")
        print("1. Submit a ticket")
        print("2. Show all tickets")
        print("3. Display ticket information")
        print("4. Respond to a ticket")
        print("5. Reopen a ticket")
        print("6. Display ticket statistics")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            submit_ticket()
        elif choice == "2":
            show_tickets()
        elif choice == "3":
            display_ticket_info()
        elif choice == "4":
            respond_to_ticket()
        elif choice == "5":
            reopen_ticket()
        elif choice == "6":
            display_ticket_stats()
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")


def get_ticket_by_number(ticket_number):
    # This function retrieves a ticket object based on its ticket number
    # You can implement your own logic to retrieve tickets from a database or list
    # For this example, we'll create a dummy list of tickets
    for ticket in sample_tickets:
        if ticket.ticket_number == ticket_number:
            return ticket
    return None


if __name__ == "__main__":
    # Creating sample tickets
    ticket1 = Ticket("F321", "John Wick", "ilovemydog@example.com", "Password Change request")
    ticket2 = Ticket("F101", "Tom Smith", "tsmith@example.com", "Network connectivity issue")
    ticket3 = Ticket("F456", "Alice Lee", "alicelee@example.com", "Software installation problem")
    ticket4 = Ticket("F678", "Bob Rose", "bobbyrose@example.com", "Printer not working")
    ticket5 = Ticket("F890", "Emma Wayne", "emmawayne1991@example.com", "Email configuration issue")
    
    sample_tickets = [ticket1, ticket2, ticket3, ticket4, ticket5]

    main()
