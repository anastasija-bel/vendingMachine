'''A base implementation of a vending machine settings and its inventory behaviour.'''
# IMPORT LOCAL LIBRARIES
import constants as const


class vendingMachine():
    '''Vending machine with its inventory.'''
    def __init__(self, parent=None):
        self.total_bottles_count = 500
        self.inventory = {const.TOTAL: 0, const.STILL: 0, const.FIZZY: 0}

    def init_default_settings(self):
        '''Initialize default inventory of a vending machine.'''
        self.still_water_count = stillWater().count
        self.fizzy_water_count = fizzyWater().count
        self.still_water_cost = stillWater().price
        self.fizzy_water_cost = fizzyWater().price
        self.inventory = {const.TOTAL: self.total_bottles_count, 
                          const.STILL: {const.COUNT: self.still_water_count,
                                   const.COST: self.still_water_cost}, 
                          const.FIZZY: {const.COUNT: self.fizzy_water_count,
                                   const.COST: self.fizzy_water_cost}}
    
    def update_inventory(self, water_type):
        '''Update current inventory after drink purchase.'''
        current_count = self.inventory[water_type][const.COUNT]
        current_total_count = self.inventory[const.TOTAL]
        updated_count = current_count - 1
        updated_total_count = current_total_count - 1
        self.inventory[water_type][const.COUNT] = updated_count
        self.inventory[const.TOTAL] = updated_total_count

    def get_current_inventory(self):
        '''dict{str: {str: int}}: Get currently available inventory of a vending machine.'''
        return self.inventory
    
    def show_current_inventory(self):
        '''Show a user currently available inventory of a vending machine.'''
        print("\n| Inventory : Total - %s | Still Water - %s | Fizzy - %s |" % (
            self.inventory[const.TOTAL], 
            self.inventory[const.STILL][const.COUNT], 
            self.inventory[const.FIZZY][const.COUNT]))
    
    def check_inventory(self, water_type):
        '''bool or None: Check if the inventory is empty.'''
        if self.inventory[water_type][const.COUNT]:
            return True
        print("Oh no! This option is out of stock. Please try a different option")


class stillWater(vendingMachine):
    '''A bottle of still water in a vending machine.'''
    def __init__(self):
        super(stillWater, self).__init__()
        self.count = int(2/5*self.total_bottles_count)
        self.price = 30


class fizzyWater(vendingMachine):
    '''A bottle of fizzy water in a vending machine.'''
    def __init__(self):
        super(fizzyWater, self).__init__()
        self.count = int(3/5*self.total_bottles_count)
        self.price = 35