#GreenVault Product

#Import section
import logging

class Product():
    """
    Product class, represents a product in the store.
    """
    #Constants
    HANDLER_REF = None

    #Attributes
    name = ""
    quantity = 0
    purchase_price = 0.00
    sale_price = 0.00

    #Methods

    def __init__(self, *args, ProgramHandlerClass=None):
        self.HANDLER_REF = ProgramHandlerClass

    def update_quantity():
        """
        Updates the quantity of a product in the inventory.
        """
        pass

    def calculate_profit():
        """
        Calculates the profit of a product in the inventory.
        """
        pass