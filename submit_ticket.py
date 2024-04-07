def submit_ticket():
    staff_id = input("Enter your staff ID: ")
    creator_name = input("Enter your name: ")
    contact_email = input("Enter your contact email: ")
    description = input("Enter the description of the issue: ")
    
    # Create a new ticket object
    new_ticket = Ticket(staff_id, creator_name, contact_email, description)
    print("Ticket submitted successfully!")
    print()


# Example usage:
submit_ticket()
