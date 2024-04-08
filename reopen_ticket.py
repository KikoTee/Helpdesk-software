# Function to reopen a closed ticket
def reopen_ticket(ticket):
    # Mark the ticket as reopened
    ticket.reopen_ticket()
    
    # Confirm successful ticket reopening
    print("Ticket reopened successfully!")
    print()

# Example usage:
ticket_to_reopen = Ticket("S101", "Bob White", "bob@example.com", "Printer not working")
reopen_ticket(ticket_to_reopen)
