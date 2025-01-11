#GreenVault Inventory

#Import section
import logging

class Inventory():
    """
    Manages the store's products (Product.py) and their functions.

    Name is the primary key for products. add_product() will not add a product with the same name as an existing one.
    """

    #Constants
    HANDLER_REF = None
    
    #Attributes

    #Methods

    def __init__(self, ProgramHandlerInstance):
        self.HANDLER_REF = ProgramHandlerInstance

    def add_product(self, name, quantity, purchase_price, sale_price):
        """
        Add a new product in the store.

        This functions assumes the product does not exist. Please verify before calling.

        Args:

        self (Inventory): Inventory instance.
        name (str): The name of the product.
        quantity (int): The quantity of the product.
        purchase_price (float): The purchase price of the product.
        sale_price (float): The sale price of the product

        Returns True if the product was correctly added.
        """

        logging.debug("User requested to add a product to the store.")

        #We assume products are only lowercases without leading and trailing whitespaces, for querying purposes.
        name = self.preprocess_item_name(name)

        #For instance, tofu and tofu2 are two different products. Same with tofu and tofus.

        new_product = {
            "name": name,
            "quantity": quantity,
            "purchase_price": purchase_price,
            "sale_price": sale_price
        }

        self.HANDLER_REF.database["products"].append(new_product)
        logging.info(f"Added product {name}.")

        print(f"AGGIUNTO: {name} X {quantity}")

        return True

    def remove_product(self, product_index):
        """
        Remove a product from the store.

        Args:
        product_index (int): The index of the product to be removed.

        Returns True if the product was removed, None if the product was not found.
        """

        logging.debug("User requested to remove a product.")

        if(product_index != None):

            self.HANDLER_REF.database["products"].pop(product_index)
            logging.info(f"Removed product.")

            return True
        
        else:
            logging.info("Product not found.")
            return None

    def list_products(self):
        """
        List all products in the store.

        Returns None if there are no products, True if there are products.
        """
        logging.debug("User requested to list products.")

        if(len(self.HANDLER_REF.database["products"]) == 0):
            print("Nessun prodotto trovato.")
            return None
        
        for index, product in enumerate(self.HANDLER_REF.database["products"]):

            if(index == 0):
                print(f"PRODOTTO QUANTITA' PREZZO\n")
 
            print(f"{str.capitalize(product['name'])}\t {product['quantity']}\t   €{product['sale_price']}")

        print("\n")
        return True

    def update_product(self, product_index, new_quantity):
        """
        Update a product in the store.

        Args:

        self (Inventory): Inventory instance.
        product_index (int): The index of the product to be updated.
        new_quantity (int): The new quantity of the product. If not set, won't be updated.

        Returns True if the product was updated, None if the product was not found.
        """

        logging.debug("User requested to update products.")

        if(new_quantity != None): 
            self.HANDLER_REF.database["products"][product_index]["quantity"] += new_quantity
            logging.info(f"Updated product with quantity {new_quantity}.")
            print(f"Aggiornato il prodotto con quantità {new_quantity}.")

            return True
        else:
            logging.info("Product not found.")
            return None

    def get_item_index_from_name(self, item_name):
        """
        Get an item from the store by name. 
        
        Args:
        item_name (str): The name of the item to be found

        Returns none if there's no item with that name.
        """
        item_name = self.preprocess_item_name(item_name)

        for index, product in enumerate(self.HANDLER_REF.database["products"]):
            if product["name"] == item_name:
                logging.debug(f"Product found at index {index}.")
                return index
        
        logging.info("Product not found.")
        return None

    def preprocess_item_name(self, item_name):
        """
        Preprocess item name for querying.

        Args:
        item_name (str): The name of the item to be preprocessed.

        Returns the preprocessed item name.
        """
        return str.lower(item_name).lstrip().rstrip()
    
        