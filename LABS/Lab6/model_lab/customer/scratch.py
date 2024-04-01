from customer.models import Customer, Order
from datetime import date

# Create customers
customer1 = Customer.objects.create(name="John Doe", email="john@example.com")
customer2 = Customer.objects.create(name="Jane Smith", email="jane@example.com")

# Create orders
order1 = Order.objects.create(customer=customer1, total_price=100.50, total_items=3, order_date=date.today())
order2 = Order.objects.create(customer=customer2, total_price=75.25, total_items=2, order_date=date.today())
