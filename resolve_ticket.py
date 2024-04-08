# Function to mark a ticket as resolved
def resolve_ticket(ticket):
    # Check if the ticket is a password change request
    ticket.resolve_password_change()
    
    # Confirm successful ticket resolution
    print("Ticket resolved successfully!")
    print()

# Example usage:
ticket_to_resolve = Ticket("S789", "Alice Johnson", "alice@example.com", "Password Change request")
resolve_ticket(ticket_to_resolve)
