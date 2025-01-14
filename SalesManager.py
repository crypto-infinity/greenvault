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

    def record_sale(self, product_list, product_quantities, product_indexes):
        """
        Record a sale in the store.

        Args:
        product_list (list of str): list of products to be added.
        product_quantities (list of int): list of quantities of specified index in product_list to be added to the sell manager.

        Returns True if Sales has been saved, False otherwise.
        """

        try:
            product_sale = defaultdict()

            product_sale["product"] = product_list
            product_sale["quantity"] = product_quantities
            product_sale["total_price"] = 0.00
            
            print("VENDITA REGISTRATA\n")

            for i, item in enumerate(product_sale["product"]):
                current_item_price = self.HANDLER_REF.database["products"][product_indexes[i]]["sale_price"] * product_sale["quantity"][i]
                product_sale["total_price"] += current_item_price

                print(f"{product_sale['quantity'][i]} X {product_sale['product'][i]} : €{current_item_price}")

                remaining_quantity = self.HANDLER_REF.database["products"][product_indexes[i]]["quantity"] - product_sale["quantity"][i]
                
                if(remaining_quantity == 0):
                    self.HANDLER_REF.database["products"].pop(product_indexes[i])
                else:
                    self.HANDLER_REF.database["products"][product_indexes[i]]["quantity"] = remaining_quantity


            self.HANDLER_REF.database["sales"].append(product_sale)

            print(f"Totale: €{product_sale['total_price']}\n")

            self.HANDLER_REF.file_handler.save_file()
            return True

        except Exception as e:
            logging.error(f"An error occurred: {e}")
            return False

    def list_sales(self):
        """
        List all sales in the store.

        Returns None if there are no sales, True if there are sales.
        """
        logging.debug("User requested to list sales.")

        if(len(self.HANDLER_REF.database["sales"]) == 0):
            print("Nessuna vendita trovata.")
            return None
        
        for index, sale in enumerate(self.HANDLER_REF.database["sales"]):

            if(index == 0):
                print(f"PRODOTTI\tQUANTITA'\n")

            for i, item in enumerate(sale["product"]):
                print(f"{str.capitalize(item[i])}", end="")

            for i, item in enumerate(sale["quantity"]):
                print(f" {item[i]}")

            print(f"Valore totale della vendita: €{sale['total_price']}")    

        print("\n")
        return True

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


    
        