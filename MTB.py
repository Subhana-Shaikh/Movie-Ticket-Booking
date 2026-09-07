# Movie Ticket Booking System - Version 1.0
#Feature : Book and Cancel Tickets
def book_ticket(ticket_id, user_id) :
  print("Ticket", ticket_id, "Confirmed Ticket of", user_id)
def cancel_ticket(ticket_id) :
  print("Ticket", ticket_id, "Cancelled")
     
def calculate_refund(days_late, rate = 5):
  refund= days_late*rate
  print("Refund=Rs.", refund)
  return refund
