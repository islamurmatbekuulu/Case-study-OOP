class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price


class Customer:
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.shopping_cart = ShoppingCart()
        self.payment_method = None

    def add_to_cart(self, product):
        self.shopping_cart.add_product(product)

    def remove_from_cart(self, product):
        self.shopping_cart.remove_product(product)

    def set_payment_method(self, payment_method):
        self.payment_method = payment_method

    def checkout(self):
        if self.payment_method is None:
            raise ValueError("Payment method is not set.")
        
        total_amount = self.shopping_cart.calculate_total()
        self.payment_method.process_payment(total_amount)
        self.shopping_cart.clear()


class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def calculate_total(self):
        total = 0
        for product in self.products:
            total += product.price
        return total

    def clear(self):
        self.products = []


class PaymentMethod:
    def process_payment(self, amount):
        raise NotImplementedError("Subclasses must implement this method.")


class CreditCardPayment(PaymentMethod):
    def __init__(self, card_number, expiration_date, cvv):
        self.card_number = card_number
        self.expiration_date = expiration_date
        self.cvv = cvv

    def process_payment(self, amount):
        # Simulate credit card payment process
        print(f"Processing ${amount:.2f} payment with credit card ending in {self.card_number[-4:]}")


class BankAccountPayment(PaymentMethod):
    def __init__(self, account_number, routing_number):
        self.account_number = account_number
        self.routing_number = routing_number

    def process_payment(self, amount):
        # Simulate bank account payment process
        print(f"Processing ${amount:.2f} payment from bank account ending in {self.account_number[-4:]}")


# Örnek Kullanım
customer1 = Customer(1, "Islam", "itokoev@gmail.com")
product1 = Product("123", "Ürün 1", 100)
product2 = Product("456", "Ürün 2", 150)

customer1.add_to_cart(product1)
customer1.add_to_cart(product2)

credit_card = CreditCardPayment("1234567890123456", "12/25", "123")
customer1.set_payment_method(credit_card)

customer1.checkout()
