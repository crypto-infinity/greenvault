#GreenVault SalesManager

#Import section
import logging

class SalesManager():
    """
    Manages the store's products (Product.py) and their operations.

    """

    #Constants
    HANDLER_REF = None
    
    #Attributes
    sales = []

    #Methods

    def __init__(self, *args, ProgramHandlerInstance=None):
        self.HANDLER_REF = ProgramHandlerInstance
        self.sales = self.HANDLER_REF.database["sales"]

    def record_sale(self):
        """
        Record a sale in the store.
        """
        pass

    def list_sales(self):
        """
        List all sales in the store.
        """
        pass

    def calculate_gross_profit(self):
        """
        Calculate the gross profit of the store.
        """
        pass

    def calculate_net_profit(self):
        """
        Calculate the net profit of the store.
        """
        pass


    
        