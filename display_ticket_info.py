def display_ticket_info(ticket):
    print("Ticket Information:")
    ticket.display_ticket()


# Example usage:
ticket_to_display = Ticket("S456", "Jane Smith", "jane@example.com", "Network connectivity issue")
display_ticket_info(ticket_to_display)
