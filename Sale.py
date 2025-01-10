#GreenVault Sale

#Import section
import logging

class Sale():
    """
    Description
    """
    #Constants
    HANDLER_REF = None

    #Attributes
    product_name = ""
    quantity = 0
    total_price = 0.00

    #Methods

    def __init__(self, *args, ProgramHandlerClass=None):
        self.HANDLER_REF = ProgramHandlerClass

    def calculate_total_price():
        """
        Calculates the total price of a sale.
        """
        pass