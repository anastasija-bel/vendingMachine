# IMPORT LOCAL LIBRARIES
import constants as const


class vendingMachine():

    def __init__(self, parent=None):
        self.total_bottles_count = 500
        self.inventory = {"total": 0, "still": 0, "fizzy": 0}

    def init_default_settins(self):
        self.still_water_count = stillWater().count
        self.fizzy_water_count = fizzyWater().count
        self.still_water_cost = stillWater().price
        self.fizzy_water_cost = fizzyWater().price
        self.inventory = {"total": self.total_bottles_count, 
                          "still": {const.COUNT: self.still_water_count,
                                   const.COST: self.still_water_cost}, 
                          "fizzy": {const.COUNT: self.fizzy_water_count,
                                   const.COST: self.fizzy_water_cost}}
    
    def update_inventory(self, water_type):
        current_count = self.inventory[water_type][const.COUNT]
        current_total_count = self.inventory["total"]
        updated_count = current_count - 1
        updated_total_count = current_total_count - 1
        self.inventory[water_type][const.COUNT] = updated_count
        self.inventory["total"] = updated_total_count

    def get_current_inventory(self):
        return self.inventory
    
    def check_inventory(self, water_type):
        if self.inventory[water_type][const.COUNT]:
            return True
        print("Oh no! This option is out of stock. Please try a different option")


class stillWater(vendingMachine):

    def __init__(self):
        super(stillWater, self).__init__()
        self.count = int(2/5*self.total_bottles_count)
        self.price = 30


class fizzyWater(vendingMachine):

    def __init__(self):
        super(fizzyWater, self).__init__()
        self.count = int(3/5*self.total_bottles_count)
        self.price = 35