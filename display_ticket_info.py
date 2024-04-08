# Function to display detailed information about a ticket
def display_ticket_info(ticket):
    print("Ticket Information:")
    
    # Call the display_ticket() method of the Ticket class to print ticket details
    ticket.display_ticket()

# Example usage:
ticket_to_display = Ticket("S456", "Jane Smith", "jane@example.com", "Network connectivity issue")
display_ticket_info(ticket_to_display)
