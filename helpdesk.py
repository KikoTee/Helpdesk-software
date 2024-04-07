
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
            new_password = self.staff_id[:2] + self.creator_name[:3]
            self.response = f"New password: {new_password}"
            self.status = "Closed"
            Ticket.open_tickets -= 1
            Ticket.closed_tickets += 1

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


def main():
    # Creating sample tickets
    ticket1 = Ticket("S123", "John Wick", "ilovemydog@example.com", "Password Change request")
    ticket2 = Ticket("S456", "Tom Smith", "tsmith@example.com", "Network connectivity issue")
    ticket3 = Ticket("S789", "Alice Lee", "alicelee@example.com", "Software installation problem")
    ticket4 = Ticket("S101", "Bob Rose", "bobbyrose@example.com", "Printer not working")
    ticket5 = Ticket("S202", "Emma Wayne", "emmawayne1991@example.com", "Email configuration issue")

    # Resolving password change request
    ticket1.resolve_password_change()

    # Providing response to ticket
    ticket2.provide_response("The network issue has been resolved.")

    # Reopening a ticket
    ticket3.reopen_ticket()

    # Displaying ticket information
    ticket1.display_ticket()
    ticket2.display_ticket()
    ticket3.display_ticket()
    ticket4.display_ticket()
    ticket5.display_ticket()

    # Displaying ticket statistics
    Ticket.ticket_stats()


if __name__ == "__main__":
    main()

