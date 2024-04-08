# Help Desk Ticketing System

This is a prototype of a Help Desk ticketing system developed in Python. The system allows internal customers to submit tickets for assistance, tracks ticket statistics, and provides functionality for the IT department to respond to and manage tickets.

## Features

- **Submitting Tickets**: Internal customers can submit tickets by providing their staff ID, name, contact email, and issue description.
- **Responding to Tickets**: The IT department can respond to tickets, mark them as resolved, or reopen them if necessary.
- **Password Change Requests**: If a ticket's description contains the phrase "Password Change", a new password is automatically generated based on specific rules.
- **Ticket Statistics**: The system keeps track of the number of submitted, resolved, and open tickets, and displays these statistics.

## Usage

1. **Submitting a Ticket**:
    - Run the `submit_ticket()` function to submit a new ticket.
  
2. **Responding to a Ticket**:
    - Use the `respond_to_ticket(ticket)` function to provide a response to an existing ticket.

3. **Displaying Ticket Information**:
    - Call the `display_ticket_info(ticket)` function to view detailed information about a ticket.
  
4. **Resolving a Ticket**:
    - Use the `resolve_ticket(ticket)` function to mark a ticket as resolved.

5. **Reopening a Ticket**:
    - Call the `reopen_ticket(ticket)` function to reopen a closed ticket.


## Contributions

Contributions to this project are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.
