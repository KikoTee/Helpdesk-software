def reopen_ticket(ticket):
    ticket.reopen_ticket()
    print("Ticket reopened successfully!")
    print()


# Example usage:
ticket_to_reopen = Ticket("S101", "Bob White", "bob@example.com", "Printer not working")
reopen_ticket(ticket_to_reopen)
