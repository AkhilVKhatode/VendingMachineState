from abc import ABC, abstractmethod

# State Interface
class VendingMachineState(ABC):
    @abstractmethod
    def insert_coin(self, machine):
        pass
    
    @abstractmethod
    def select_item(self, machine):
        pass
    
    @abstractmethod
    def dispense_item(self, machine):
        pass

# Concrete States
class NoCoinState(VendingMachineState):
    def insert_coin(self, machine):
        print("Coin inserted")
        machine.set_state(machine.has_coin_state)
    
    def select_item(self, machine):
        print("Please insert a coin first")
    
    def dispense_item(self, machine):
        print("Please insert a coin first")

class HasCoinState(VendingMachineState):
    def insert_coin(self, machine):
        print("Coin already inserted")
    
    def select_item(self, machine):
        if machine.item_count > 0:
            print("Item selected")
            machine.set_state(machine.dispensing_state)
        else:
            print("Item out of stock")
            machine.set_state(machine.sold_out_state)
    
    def dispense_item(self, machine):
        print("Please select an item first")

class DispensingState(VendingMachineState):
    def insert_coin(self, machine):
        print("Please wait, item is being dispensed")
    
    def select_item(self, machine):
        print("Please wait, item is being dispensed")
    
    def dispense_item(self, machine):
        machine.item_count -= 1
        print("Item dispensed")
        if machine.item_count > 0:
            machine.set_state(machine.no_coin_state)
        else:
            machine.set_state(machine.sold_out_state)

class SoldOutState(VendingMachineState):
    def insert_coin(self, machine):
        print("Machine is sold out, cannot accept coins")
    
    def select_item(self, machine):
        print("Machine is sold out")
    
    def dispense_item(self, machine):
        print("Machine is sold out")

# Context
class VendingMachine:
    def __init__(self, item_count):
        # Initialize states
        self.no_coin_state = NoCoinState()
        self.has_coin_state = HasCoinState()
        self.dispensing_state = DispensingState()
        self.sold_out_state = SoldOutState()
        
        self.item_count = item_count
        self.current_state = self.no_coin_state if item_count > 0 else self.sold_out_state
    
    def set_state(self, state):
        self.current_state = state
    
    def insert_coin(self):
        self.current_state.insert_coin(self)
    
    def select_item(self):
        self.current_state.select_item(self)
    
    def dispense_item(self):
        self.current_state.dispense_item(self)
    
    def refill(self, item_count):
        self.item_count = item_count
        self.set_state(self.no_coin_state)
        print(f"Machine refilled with {item_count} items")

# Usage example
if __name__ == "__main__":
    vending_machine = VendingMachine(3)  # Machine starts with 3 items
    
    # Test the vending machine
    vending_machine.select_item()  # No coin
    vending_machine.insert_coin()  # Insert coin
    vending_machine.select_item()  # Select item
    vending_machine.dispense_item()  # Dispense item
    
    print("\nSecond cycle:")
    vending_machine.insert_coin()
    vending_machine.select_item()
    vending_machine.dispense_item()
    
    print("\nThird cycle:")
    vending_machine.insert_coin()
    vending_machine.select_item()
    vending_machine.dispense_item()  # Now sold out
    
    print("\nAfter sold out:")
    vending_machine.insert_coin()
    vending_machine.select_item()
    
    print("\nAfter refill:")
    vending_machine.refill(2)
    vending_machine.insert_coin()
    vending_machine.select_item()
    vending_machine.dispense_item()
