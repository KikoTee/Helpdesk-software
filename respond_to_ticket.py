def respond_to_ticket(ticket):
    response = input("Provide a response to the ticket: ")
    ticket.provide_response(response)
    print("Response provided successfully!")
    print()


# Example usage:
ticket_to_respond = Ticket("S123", "John Doe", "john@example.com", "Password Change request")
respond_to_ticket(ticket_to_respond)
