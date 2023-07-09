
class Snack:
    def __init__(self, snack_id,name,price,availability):
        self.snack_id = snack_id
        self.name = name
        self.price = price
        self.availability = availability
    def __str__(self):
        return f"Snack ID: {self.snack_id}\nName: {self.name}\nPrice: {self.price}\nAvailability: {self.availability}"


class Inventory:
    def __init__(self):
        self.snacks = []

    
    def add_snacks(self,snack):
        self.snacks.append(snack)
    

    def remove_snack(self,snack_id):
        for snack in self.snacks:
            if snack.snack_id == snack_id:
                self.snacks.remove(snack)
                return True
        return True
    

    def update_snack_availability(self,snack_id,availability):
        for snack in self.snacks:
            if snack.snack_id == snack_id:
                snack.availability = availability
                return True
        return False
    

    def get_snack_by_id(self, snack_id):
        for snack in self.snacks:
            if snack.snack_id == snack_id:
                return snack
        return None
        
         
    def get_all_snacks(self):
        return self.snacks[:]


def display_menu():
    print("\n*** Snack Inventory Management ***")
    print("1. Add a snack")
    print("2. Remove a snack")
    print("3. Update snack availability")
    print("4. Sell a snack")
    print("5. View all snacks")
    print("0. Exit")


def get_menu_choice():
    while True :
        try:
            choice = int(input("Enter your choice: "))
            if 0 <= choice <= 5:
               return choice
            else:
                print("Invalid choice. Please enter a number from 0 to 5.")
        except ValueError:
            print("Invalid choice. Please enter a number.")



def add_snack_to_inventory(inventory):
    print("\n*** Add a Snack ***")
    snack_id = int(input("Enter snack ID: "))
    name = (input("Enter snack name: "))
    price = int(input("Enter snack price"))
    availability = input("Is the snack available (yes/no)? ").lower() == "yes"


    snack = Snack(snack_id,name,price,availability)
    inventory.add_snacks(snack)
    print("Snack added to inventory.")


def remove_snack_from_inventory(inventory):
    print("\n*** Remove a Snack ***")
    snack_id = int(input("Enter the ID of the snack to remove: "))
    if inventory.remove_snack(snack_id):
        print("Snack removed from inventory.")
    else:
        print("Snack not found in inventory.")


def update_snack_availability(inventory):
    print("\n*** Update Snack Availability")
    snack_id = int(input("Enter the ID of the snack to update: "))
    availability = input("Is the snack available (yes/no)?").lower() == "yes"

    if inventory.update_snack_availability(snack_id, availability):
         print("Snack availability update.")
    else:
        print("Snack not found in inventory.")


def sell_snack(inventory):
    print("\n*** Sell a Snack ***")
    snack_id = int(input("Enter the ID of the snack to sell: "))


    snack = inventory.get_snack_by_id(snack_id)
    if snack:
        if snack.availability:
            inventory.remove_snack(snack_id)
            print("f{snack.name}sold. Inventory updated.")
        else:
            print("Snack is not available for sale.")
    else:
        print("Snack not found in inventory.")


def view_all_snacks(inventory):
    print("\n *** All Snacks ***")
    snacks = inventory.get_all_snacks()
    if snacks:
        for snack in snacks:
            print(snack)
    else:
        print("No snack in inventory")


#Main program loop
def run_application():
    inventory = Inventory()



    while True:
        display_menu()
        choice = get_menu_choice()

        if choice == 0:
            print("Exiting the application. Goodbye!")
            break
        elif choice == 1:
            add_snack_to_inventory(inventory)
        elif choice == 2:
            remove_snack_from_inventory(inventory)
        elif choice == 3:
            update_snack_availability(inventory)
        elif choice == 4:
            sell_snack(inventory)
        elif choice == 5:
            view_all_snacks(inventory)



if __name__ == "__main__":
    run_application()
