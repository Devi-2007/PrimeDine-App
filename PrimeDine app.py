import random

class PrimeDine:
    menu = {
        'veg': {
            'margerita': 129,
            'cheese_and_corn': 169,
            'peppi_paneer': 260,
            'veg_loaded': 210,
            'tomato_tangi': 170
        },
        'non_veg': {
            'pepper_barbeque': 199,
            'non_veg_loaded': 169,
            'chicken_sausage': 200
        },
        'snacks': {
            'garlic_bread': 120,
            'zingy': 59,
            'chicken_cheese_balls': 170
        },
        'desserts': {
            'choco_lava': 100,
            'mousse cake': 169
        },
        'drinks': {
            'coke': 90,
            'pepsi': 78,
            'sprite': 50
        }
    }

    def __init__(self, name, email, phno):
        self.name = name
        self.email = email
        self.phno = phno
        self.login_status = False
        self.cart = {}

        while True:
            if not self.login_status:
                print("-" * 50)
                print("-----------------Welcome to PRIMEDINE🍕 app-------------")
                print("Login")
                ch = input("Do you want to Login? (y/n): ").lower()
                if ch == 'y':
                    self.login()
                else:
                    print("Login is required")
                    
            if self.login_status:
                print("-----------------Welcome to PRIMEDINE🍕 app-------------")
                print(f"User 👤: {self.name}")
                print("Enter 1: Order")
                print("Enter 2: Show cart")
                print("Enter 3: Logout")
                ch = int(input("Enter choice: "))
                if ch == 1:
                    self.order()
                elif ch == 2:
                    self.show_cart()
                elif ch == 3:
                    self.logout()
                else:
                    print("Invalid choice")

    @staticmethod
    def validate_otp(value):
        while True:
            print("-" * 50)
            og_otp = random.randint(1000, 9999)
            print(f"An otp has been sent to {value}...")
            print(f"Your PrimeDine otp is: {og_otp}")
            otp = int(input("Enter otp: "))
            if otp == og_otp:
                print("Login successful ✅")
                return True
            print("Invalid OTP, enter correct otp")
              
    def login(self):
        print("Enter 1: Login with Phone")
        print("Enter 2: Login with Email")
        ch = int(input("Enter choice: "))
        if ch == 1:
            phno = int(input("Enter phno: "))
            if phno == self.phno:
                otp = self.validate_otp(phno)
                self.login_status = otp
            else:
                print("Phone no doesn't exist")
        elif ch == 2:
            email = input("Enter Email: ")
            if email == self.email:
                otp = self.validate_otp(email)
                self.login_status = otp
            else:
                print("Email doesn't exist")
        else:
            print("Invalid choice")

    def logout(self):
        ch = input("Do you want to logout? (y/n): ").lower()
        if ch == 'y':
            self.login_status = False
        print("Thank you for using our app")
    
    def order(self):
        while True:
            print("--------MENU-------")
            for category in PrimeDine.menu:
                print(category)
            print('-' * 50)

            cat = input("Enter category: ").lower()
            if cat in PrimeDine.menu:
                for item in PrimeDine.menu[cat]:
                    print(f"{item} --------- Rs. {PrimeDine.menu[cat][item]}")
                item = input("Enter item name: ")
                if item in PrimeDine.menu[cat]:
                    q = int(input("Enter quantity: "))
                    price = q * PrimeDine.menu[cat][item]
                    if item in self.cart:
                        self.cart[item] += price
                    else:
                        self.cart[item] = price
                    print(f"{item} added to the cart")
                    choice = input("Do you want to add more? (y/n): ").lower()
                    if choice == 'n':
                        break
                else:
                    print(f"{item} not available")
            else:
                print(f"{cat} not available")

    def show_cart(self):
        print('---------PrimeDine Cart-----------')
        if self.cart != {}:
            total = 0
            for item in self.cart:
                price = self.cart[item]
                total += price
                print(f"{item} ----- Rs. {price}")
            print("Total Price: Rs.", total)

            ch = input("Place order? (y/n): ").lower()
            if ch == 'y':
                print("Thank you for placing the order")
                print("Your order will arrive soon")
                self.cart = {}
        else:
            print("Your cart is empty")
            


ob = PrimeDine("pedi", "pedi26@gmail.com", 9500504746)
