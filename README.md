# Vending Machine State Design Pattern in Python

A Python implementation of a vending machine using the State design pattern to manage different states: NoCoin, HasCoin, Dispensing, and SoldOut.

## 📝 Description

This project demonstrates how to use the State design pattern to model a vending machine's behavior based on its current state. Each state determines how the machine responds to user actions like inserting coins, selecting items, and dispensing items.

## 🏗️ State Diagram
[NoCoin] --insert_coin--> [HasCoin]
[HasCoin] --select_item--> [Dispensing] (if items available)
[HasCoin] --select_item--> [SoldOut] (if no items)
[Dispensing] --dispense_item--> [NoCoin] (if items remain)
[Dispensing] --dispense_item--> [SoldOut] (if last item)
[SoldOut] --refill--> [NoCoin]


## 🛠️ Implementation Details

The vending machine has four states:

1. **NoCoinState**: Initial state when no coin is inserted
2. **HasCoinState**: When coin is inserted but no item selected
3. **DispensingState**: When item is being dispensed
4. **SoldOutState**: When machine is out of items
