
inventory = {'carrot': {'qty': 30, 'price': 5.0},'tomato   ':{'qty':50,'price':3.0}}
users = {}
sales_report = []

def owner_menu():
    while True:
        print('\n**** OWNER MENU ****')
        print('1. Add items')
        print('2. Remove items')
        print('3. Update items')
        print('4. View inventory')
        print('5. View users')
        print('6. View report')
        print('7. Exit')

        ch = input('Enter your choice: ')

        if ch == '1':
            item = input("Enter item name: ")
            qty = int(input('Enter quantity: '))
            price = float(input('Enter price: '))
            inventory[item] = {'qty': qty, 'price': price}
            print(f"{item} added successfully!")

        elif ch == '2':
            item = input("Enter item name to remove: ")
            if item in inventory:
                inventory.pop(item)
                print(f"{item} removed from inventory.")
            else:
                print("Item not found.")

        elif ch == '3':
            item = input("Enter item name to update: ")
            if item in inventory:
                qty = int(input('Enter new quantity: '))
                price = float(input('Enter new price: '))
                inventory[item] = {'qty': qty, 'price': price}
                print(f"{item} updated successfully.")
            else:
                print("Item not found.")

        elif ch == '4':
            print('\n--- Inventory ---')
            for item, details in inventory.items():
                print(f"{item}: Qty={details['qty']}, Price={details['price']}")

        elif ch == '5':
            print('\n--- Users ---')
            for user, cart in users.items():
                print(f"{user}: {cart}")

        elif ch == '6':
            print('\n--- Sales Report ---')
            total_revenue = sum(entry['total'] for entry in sales_report)
            for entry in sales_report:
                print(entry)
            print(f"Total Revenue: ${total_revenue:.2f}")

        elif ch == '7':
            print("Exiting Owner Menu...")
            break

        else:
            print('Invalid choice, please try again.')

def user_menu(username):
    cart = {}

    while True:
        print('\n**** USER MENU ****')
        print('1. Add to cart')
        print('2. Remove from cart')
        print('3. Modify quantity')
        print('4. View cart')
        print('5. Billing')
        print('6. Exit')

        ch = input('Enter your choice: ')

        if ch == '1':
            item = input('Enter item to add: ')
            if item in inventory:
                qty = int(input('Enter quantity: '))
                if qty <= inventory[item]['qty']:
                    cart[item] = cart.get(item, 0) + qty
                    print(f"{item} added to cart.")
                else:
                    print('Not enough stock.')
            else:
                print('Item not found.')

        elif ch == '2':
            item = input('Enter item to remove quantity from: ')
            if item in cart:
                remove_qty = int(input('Enter quantity to remove: '))
                if remove_qty >= cart[item]:
                    cart.pop(item)
                    print(f"All of {item} removed from cart.")
                else:
                    cart[item] -= remove_qty
                    print(f"{remove_qty} of {item} removed from cart. Remaining: {cart[item]}")
            else:
                print('Item not in cart.')

        elif ch == '3':
            item = input('Enter item to modify: ')
            if item in cart:
                qty = int(input('Enter new quantity: '))
                if qty <= inventory[item]['qty']:
                    cart[item] = qty
                    print(f"{item} quantity updated.")
                else:
                    print('Not enough stock.')
            else:
                print('Item not in cart.')

        elif ch == '4':
            print('\n--- Cart ---')
            for item, qty in cart.items():
                print(f"{item}: Qty={qty}")

        elif ch == '5':
            if not cart:
                print("Cart is empty!")
                continue

            total = 0
            for item, qty in cart.items():
                price = inventory[item]['price']
                total += price * qty
                inventory[item]['qty'] -= qty

            print(f"Total bill: ${total:.2f}")
            sales_report.append({'user': username, 'cart': cart.copy(), 'total': total})
            users[username] = cart.copy()
            cart.clear()

        elif ch == '6':
            print("Exiting User Menu...")
            break

        else:
            print('Invalid choice, try again.')

def main():
    while True:
        print('\n==== INVENTORY MANAGEMENT SYSTEM ====')
        print('1. Owner')
        print('2. User')
        print('3. Exit')

        role = input('Select role: ')

        if role == '1':
            owner_menu()
        elif role == '2':
            username = input('Enter your name: ')
            user_menu(username)
        elif role == '3':
            print("Goodbye!")
            break
        else:
            print('Invalid selection, try again.')

main()