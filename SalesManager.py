#GreenVault SalesManager

#Import section
import logging
from collections import defaultdict

class SalesManager():
    """
    Manages the store's sales and specifies profits for each of them.
    """

    #Constants
    HANDLER_REF = None
    
    #Attributes

    #Methods

    def __init__(self, ProgramHandlerInstance):
        """
        Initializes the class and its reference to the ProgramHandler instance.
        """
        self.HANDLER_REF = ProgramHandlerInstance

    def record_sale(self, product_list, product_quantities, product_indexes):
        """
        Records a sale in the store.

        Args:
        product_list (list of str): list of products to be added.
        product_quantities (list of int): list of quantities of specified index in product_list to be added to the sell manager.
        product_indexes (list of int): a list containing the specific indexes of product_list, in the same order.

        Returns True if the sale has been saved, False otherwise.
        """

        logging.debug("User requested to record a sale.")

        try:
            product_sale = defaultdict()

            product_sale["product"] = product_list
            product_sale["quantity"] = product_quantities
            product_sale["total_gross_sell_value"] = 0.00
            product_sale["net_profit"] = 0.00
            
            print("VENDITA REGISTRATA\n")

            for i, item in enumerate(product_sale["product"]):
                current_item_price = self.HANDLER_REF.database["products"][product_indexes[i]]["sale_price"] * product_sale["quantity"][i]
                current_item_cost = self.HANDLER_REF.database["products"][product_indexes[i]]["purchase_price"] * product_sale["quantity"][i]

                product_sale["total_gross_sell_value"] += current_item_price

                #A negative Profit is considered a loss in the specified sale.
                product_sale["net_profit"] += current_item_price - current_item_cost

                print(f" • {product_sale['quantity'][i]} X {product_sale['product'][i]} : €{current_item_price:.2f}")

                remaining_quantity = self.HANDLER_REF.database["products"][product_indexes[i]]["quantity"] - product_sale["quantity"][i]
                
                if(remaining_quantity == 0):
                    self.HANDLER_REF.database["products"].pop(product_indexes[i])
                else:
                    self.HANDLER_REF.database["products"][product_indexes[i]]["quantity"] = remaining_quantity


            self.HANDLER_REF.database["sales"].append(product_sale)
            self.HANDLER_REF.database["gross_profits"] += product_sale["total_gross_sell_value"]
            self.HANDLER_REF.database["net_profits"] += product_sale["net_profit"]

            print("\n")
            print(f"Totale: €{product_sale['total_gross_sell_value']:.2f}\n")

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

            print(f"Valore totale della vendita: €{sale['total_gross_sell_value']}")    

        print("\n")
        return True

    def gross_profit(self):
        """
        Calculate the gross profit of the store.

        Returns the dictionary key gross_profits of self.HANDLER_REF.database.
        """

        return self.HANDLER_REF.database["gross_profits"]

    def net_profit(self):
        """
        Calculate the net profit of the store.

        Returns the dictionary key net_profits of self.HANDLER_REF.database.
        """

        return self.HANDLER_REF.database["net_profits"]


    
        