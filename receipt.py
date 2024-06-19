from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

def create_receipt(transaction_id, date, items, subtotal, tax, total, customer_name, customer_address):
    c = canvas.Canvas(f"receipt_{transaction_id}.pdf", pagesize=letter)
    width, height = letter

    
    c.setFont("Helvetica-Bold", 20)
    c.drawString(2 * inch, height - inch, "Payment Receipt")

    
    c.setFont("Helvetica", 12)
    c.drawString(1 * inch, height - 1.5 * inch, f"Transaction ID: {transaction_id}")
    c.drawString(1 * inch, height - 1.75 * inch, f"Date: {date}")

    c.drawString(1 * inch, height - 2.25 * inch, f"Customer Name: {customer_name}")
    c.drawString(1 * inch, height - 2.5 * inch, f"Customer Address: {customer_address}")

    
    c.drawString(1 * inch, height - 3 * inch, "Items:")
    y_position = height - 3.25 * inch
    for item, price in items.items():
        c.drawString(1.5 * inch, y_position, f"{item}: Rs{price:.2f}")
        y_position -= 0.25 * inch

   
    c.drawString(1 * inch, y_position - 0.5 * inch, f"Subtotal: Rs{subtotal:.2f}")
    c.drawString(1 * inch, y_position - 0.75 * inch, f"Tax: Rs{tax:.2f}")
    c.drawString(1 * inch, y_position - 1 * inch, f"Total: Rs{total:.2f}")

    
    c.drawString(1 * inch, y_position - 2 * inch, "Thank you for your business!")

    c.showPage()
    c.save()


transaction_id = "123456"
date = "2024-06-19"
items = {
    "Item A": 500.00,
    "Item B": 250.00,
    "Item C": 1000.00
}
subtotal = sum(items.values())
tax = subtotal * 0.07  
total = subtotal + tax
customer_name = "Urmila Devi"
customer_address = "vijaynagar,Indore,India"

create_receipt(transaction_id, date, items, subtotal, tax, total, customer_name, customer_address)