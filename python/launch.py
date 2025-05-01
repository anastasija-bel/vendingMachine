'''A base implementation of logic for buying a bottle of water from a vending machine.'''
# IMPORT LOCAL LIBRARIES
import vending_machine as vm
import constants as const


def choose_drink(vending_machine, total_coins):
    '''Choose a drink from available options in a vending machine.
        
        Args:
            vending_machine (vending_machine.vendingMachine): 
                Vending machine object with available information and actions for inventory and its cost/count.
            total_coins (int):
                All coins added to a vending machine for buying a drink.

        Returns:
            int: Change after purchasing a drink (or all coins if cancelled)
    '''
    drink_chosen = False
    change = 0

    if not total_coins:
        print("\nPlease insert money to buy a drink")
        return change

    print("\nChoose your drink")

    while not drink_chosen:
        print("| 1 - Still Water (30) | 2 - Fizzy Water (35) | 3 - Cancel |")
        water_option = input()

        if water_option not in const.WATER.keys():
            print("\nPlease choose your drink from available options")
            continue

        water_type = const.WATER[water_option]
        # Return to adding coins if a user chooses 3rd ("Cancel") option
        if not isinstance(water_type, str):
            break
        
        inventory = vending_machine.get_current_inventory()
        water_cost = inventory[water_type][const.COST]

        if not vending_machine.check_inventory(water_type):
            break
        
        print("Drink cost: ", water_cost)
        if water_cost > total_coins:
            print("\nPlease add more money")
        else:
            change = total_coins - water_cost
            print("Change: ", change)
            total_coins = change
            vending_machine.update_inventory(water_type)
            vending_machine.show_current_inventory()
            
        drink_chosen = True

    return total_coins


def main():
    # Initialise default settings for a vending machine
    vending_machine = vm.vendingMachine()
    vending_machine.init_default_settings()

    total_coins = 0
    done = False

    vending_machine.show_current_inventory()
    print("\nPlease choose an option to add a coin")

    while not done:
        print("| 1 - 1c | 2 - 2c | 3 - 5c | 4 - 10c | 5 - Next | 6 - Cancel |")

        print("Total: ", total_coins)
        option = input()

        if option not in const.COINS.keys():
            print("Please choose the available option")
            continue

        coin_added = const.COINS[option]

        # Stop if a user chooses 6th ("Cancel") option
        if not coin_added:
            print("Here is your change: ", total_coins)
            done = True

        # Continue to selecting a drink when a user chooses 5th ("Next") option
        if isinstance(coin_added, str):
            total_coins = choose_drink(vending_machine, total_coins)
        else:
            total_coins += coin_added


if __name__ == "__main__":
    main()