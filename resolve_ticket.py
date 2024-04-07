def resolve_ticket(ticket):
    ticket.resolve_password_change()  # For password change requests
    print("Ticket resolved successfully!")
    print()


# Example usage:
ticket_to_resolve = Ticket("S789", "Alice Johnson", "alice@example.com", "Password Change request")
resolve_ticket(ticket_to_resolve)
