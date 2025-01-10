#GreenVault Inventory

#Import section
import logging

class Inventory():
    """
    Manages the store's products (Product.py) and their operations.
    """

    #Constants
    HANDLER_REF = None
    
    #Attributes
    products = []

    #Methods

    def __init__(self, *args, ProgramHandlerInstance=None):
        self.HANDLER_REF = ProgramHandlerInstance
        self.products = self.HANDLER_REF.database["products"]

    def add_product(self):
        """
        Add a product in the store.
        """
        pass

    def remove_product(self):
        """
        Remove a product from the store.
        """
        pass

    def list_products(self):
        """
        List all products in the store.
        """
        pass

    def search_product(self):
        """
        Search for a product in the store.
        """
        pass

    def update_product(self):
        """
        Update a product in the store.
        """
        pass

    
        