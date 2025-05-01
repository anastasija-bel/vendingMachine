# IMPORT LOCAL LIBRARIES
import vending_machine as vm
import constants as const


def choose_drink(vending_machine, total_coins):

    drink_chosen = False
    change = 0

    if not total_coins:
        print("\nPlease insert money to buy a drink")
        return change

    print("\nChoose your drink")
    print("| 1 - Still Water (30) | 2 - Fizzy Water (35) | 3 - Cancel |")

    while not drink_chosen:
        water_option = input()

        if water_option not in const.WATER.keys():
            print("\nPlease choose your drink from available options")
            continue

        water_type = const.WATER[water_option]
        # cancel if a user chooses 3rd ("Cancel") option
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
        drink_chosen = True

    return total_coins


def main():

    vending_machine = vm.vendingMachine()
    vending_machine.init_default_settins()

    total_coins = 0
    done = False

    print("\nPlease choose an option to add a coin")

    while not done:
        vending_machine.show_current_inventory()
        print("| 1 - 1c | 2 - 2c | 3 - 5c | 4 - 10c | 5 - Next | 6 - Cancel |")

        print("Total: ", total_coins)
        option = input()

        if option not in const.COINS.keys():
            print("Please choose the available option")
            continue

        coin_added = const.COINS[option]

        if not coin_added:
            print("Here is your change: ", total_coins)
            done = True

        if isinstance(coin_added, str):
            total_coins = choose_drink(vending_machine, total_coins)
        else:
            total_coins += coin_added


if __name__ == "__main__":
    main()