#GreenVault SalesManager

#Import section
import logging
from collections import defaultdict

class SalesManager():
    """
    Manages the store's products (Product.py) and their operations.

    """

    #Constants
    HANDLER_REF = None
    
    #Attributes

    #Methods

    def __init__(self, ProgramHandlerInstance):
        self.HANDLER_REF = ProgramHandlerInstance

    def record_sale(self):
        """
        Record a sale in the store.

        Returns True if Sales has been saved, False otherwise.
        """

        product_sale = defaultdict()
        product_sale["product"] = []
        product_sale["quantity"] = []

        user_key = "si"

        while(user_key != "no"):
            product_name = self.HANDLER_REF.get_user_input(acquire_prices=False, acquire_name_only=True)

            product_index = self.HANDLER_REF.inventory.get_item_index_from_name(product_name)

            if(product_index == None):
                logging.info(f"Product not available in store.")
                print(f"Il prodotto {product_name} non è disponibile a magazzino, perciò non è possibile procedere con la vendita.")

                return False
            
            product_quantity= self.HANDLER_REF.get_user_input(acquire_prices=False, acquire_name_only=False, acquire_remaining_info=True)
            
            if(product_quantity > self.HANDLER_REF.database["products"][product_index]):
                logging.info(f"Product does not have enough quantity for specified sell.")
                print(f"Il prodotto {product_name} non possiede a magazzino sufficienti scorte, perciò non è possibile procedere con la vendita.")

                return False

            logging.info(f"Product {product_name} available for sell for quantity {product_quantity}")

            product_sale["product"].append(product_name)
            product_sale["quantity"].append(product_quantity)

            user_key = input("Aggiungere un altro prodotto ? (si/no): ")

            if(user_key != "si" or user_key != "no"):
                print("Comando non valido.")
                user_key = input("Aggiungere un altro prodotto ? (si/no): ")
        
        self.HANDLER_REF.database["sales"].append(product_sale)

        return True

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


    
        