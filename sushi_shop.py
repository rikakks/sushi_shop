from PIL import Image
import sys


class Shop:
    def __init__(self):
        print("Welcome to Rikako's Sushi Shop.🍣")
        name = input("What is your name? ")
        print("Thank you for coming to our shop today, " + name + '!')
        return self.green_tea()

    def green_tea(self):
        if input("Here will be some green tea🍵 for you. Type y to continue: "
                 ).lower() == 'y':
            tea_image = Image.open("IMAGES/TEA.png")
            tea_image.show()
            return self.menu()
        else:
            return

    def menu(self):
        if input("Here is the menu. Type y to continue: ").lower() == 'y':
            menu_image = Image.open("IMAGES/MENU.png")
            menu_image.show()
            print("")
            return self.order()
        else:
            return

    def order(self):
        menu_list = {
            'AMAEBI': '1.96',
            'IKA': '1.96',
            'IKURA': '2.98',
            'SALMON': '1.96',
            'SHIMESABA': '2.96',
            'TAKO': '1.96',
            'TAMAGO': '1.96',
            'UNI': '4.98',
        }
        order_list = []
        order_bill = 0
        while True:
            cont_or_discont = input(
                "Type 'o' for order, 'b' for bill💵, 't' for more green tea🍵, and 's' for more soy sauce: "
            ).lower()
            if cont_or_discont == 'o' or cont_or_discont == "'o'":
                take_order = input("Which sushi would you like? ").upper()
                input("Wasabi? Type 'y' for yes, and 'n' for no: ")
                try:
                    sushi_image = Image.open(
                        "IMAGES/SUSHI/" + take_order + '.png')
                    order_list.append(take_order)
                    order_bill += float(menu_list[take_order])
                    sushi_image.show()
                except FileNotFoundError:
                    print("Sorry, but that menu is not available.")

            elif cont_or_discont == 'b' or cont_or_discont == "'b'":
                left_overs = input(
                    "Thank you for eating at Rikako's Sushi Shop!🍣 Did you have any leftovers for takeout? Type 'y' for yes, and 'n' for no: "
                )
                if left_overs == 'y' or left_overs == "'y'":
                    print("Okay, we will get you a take out box right away!")
                else:
                    pass
                print("Here is a summary of the plates you have ordered: " +
                      str(order_list))
                print("Your total is: " + str(round(order_bill, 2)) + " USD.")
                print("Tip Reference: 15% = " +
                      str(round((order_bill * 0.15), 2)) + ", 20% = " +
                      str(round((order_bill * 0.20), 2)) + ", 25% = " + str(
                          round((order_bill * 0.25), 2)))
                total = round(order_bill / 100 * (100 + int(
                    input(
                        "Please enter an integer between 0 - 100 for percentage of tip: "
                    ))), 2)
                method = [
                    '1. Credit/Debit Card💳',
                    '2. Cash💵',
                    '3. Venmo',
                    '4. Apple Pay🍎',
                ]
                print(method)
                method_selected = method[int(
                    input(
                        "Please type a number between 1-4 for method of payment: "
                    )) - 1]
                print("Thank you for your payment. A total of: " + str(total) +
                      " USD was charged to your " + str(method_selected) +
                      ". Please come again!")
                sys.exit()

            elif cont_or_discont == 't' or cont_or_discont == "'t'":
                tea_image = Image.open("IMAGES/TEA.png")
                tea_image.show()

            elif cont_or_discont == 's' or cont_or_discont == "'s'":
                tea_image = Image.open("IMAGES/SHOYU.png")
                tea_image.show()

            else:
                pass

    def leave(self):
        print(
            "Seems like you don't want to continue and want to leave. Please come again!"
        )
        sys.exit()


shop = Shop()
