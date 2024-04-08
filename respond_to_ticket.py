# Function to allow the IT department to respond to a ticket
def respond_to_ticket(ticket):
    # Prompt the user to provide a response
    response = input("Provide a response to the ticket: ")
    
    # Update the ticket with the provided response
    ticket.provide_response(response)
    
    # Confirm successful response submission
    print("Response provided successfully!")
    print()
