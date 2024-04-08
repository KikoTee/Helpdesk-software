# Function to allow internal customers to submit a ticket for assistance
def submit_ticket():
    # Prompt the user to input ticket details
    staff_id = input("Enter your staff ID: ")
    creator_name = input("Enter your name: ")
    contact_email = input("Enter your contact email: ")
    description = input("Enter the description of the issue: ")
    
    # Create a new ticket object with the provided details
    new_ticket = Ticket(staff_id, creator_name, contact_email, description)
    
    # Confirm successful ticket submission
    print("Ticket submitted successfully!")
    print()

# Example usage:
submit_ticket()
