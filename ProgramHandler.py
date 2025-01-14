#GreenVault ProgramHandler

#Import section

#GreenVault Classes

from FileHandler import FileHandler
from Inventory import Inventory
from SalesManager import SalesManager

#Standard library classes

import sys
import os
import logging
import json
import random
import string

from collections import defaultdict

# Class definition

class ProgramHandler():
    """
    ProgramHandler class, manages the program's main loop: loads file, execute the menu, handles operations.

    Creates an instance of Inventory and SalesManager to manage the store's products and sales.
    """
    #Constants

    #Attributes

    inventory = None # Inventory instance
    sales_manager = None # SalesManager istance
    file_handler = None # FileHandler class instance

    database = defaultdict()

    #Methods

    def __init__(self, *args):
        """
        Initialize the ProgramHandler class.

        Provides:
        - logging options
        - instances collection settings
        - database initialization settings
        """

        #Logging configuration

        logging.basicConfig(
            filename="app.log",
            encoding="utf-8",
            filemode="a",
            format="{asctime} - {levelname} - {message}",
            style="{",
            level=logging.DEBUG,
            datefmt="%Y-%m-%d %H:%M",
        )

        logging.debug("ProgramHandler started.")

        #Database initialization

        self.database = defaultdict()

        self.database["products"] = []
        self.database["sales"] = []
        self.database["gross_profits"] = 0.00
        self.database["net_profits"] = 0.00

        logging.debug("Database initialized.")

        #Instances creation and program start

        try:
            self.file_handler = FileHandler(ProgramHandlerInstance=self)
            self._inventory = Inventory(self)
            self._sales_manager = SalesManager(ProgramHandlerInstance=self)

            logging.debug("Instances FileHandler, Inventory and SalesManager created.")

            self.start_program()
            
        except Exception as e:
            logging.error(f"An error occured: {e}")
            self.exit_program_with_error()

    def start_program(self):
        """
        Starts the program by loading the inventory and starting the interaction.
        """
        try:
            self._load_inventory()
            self._start_interaction()
        except Exception as e:
            logging.error(f"An error occured: {e}")
            self.exit_program_with_error()

    def _load_inventory(self):
        """
        Check if the file exists and is readable, then opens it for streaming.

        If it does not exist or if it can't be decoded, a new file is created and the old renamed.
        """
        
        try:
            self.file_handler.load_file()

        except json.JSONDecodeError as e:
            logging.error("File JSON is not consistent.")
            logging.warning("Creating new file...")

            self.file_handler.close_file()
            self.file_handler.file_stream = None #reinitialize file handler
 
            self.file_handler.initialize_file()

        except FileNotFoundError as e:
            logging.info("File does not exist. Creating...")
            self.file_handler.initialize_file()

        except Exception as e:
            self.exit_program_with_error(exception=e)

    def show_help(self):
        """
        Show an help menu with all possible commands.
        """

        print("I comandi disponibili sono i seguenti:")
        print("• aggiungi: aggiungi un prodotto al magazzino")
        print("• elenca: elenca i prodotti in magazzino")
        print("• vendita: registra una vendita effettuata")
        print("• profitti: mostra i profitti totali")
        print("• aiuto: mostra i possibili comandi")
        print("• chiudi: esci dal programma")
        print("\n")


    def exit_program(self, message="Arrivederci, e grazie per aver usato il programma!"):
        """
        Exits the program with a farewell message, saving the file.

        Args:
        message (str): The farewell message to be displayed. Defaults to a sample.
        """
        self.file_handler.save_file()
        print(message)
        sys.exit(0)

    def exit_program_with_error(self, exception="Si è verificato un errore, uscita dall'app in corso.."):
        """
        Exits the program with an error message.
        """
        logging.critical(f"An error occured, stopping program: {exception}")
        self.exit_program(message=exception)

    def _create_random_string(length=8):
        """
        Creates a random string.
        """

        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        
        return result_str
    
    def _can_cast(self, source, dest_type):
        try:
            dest_type(source)
            return True
        
        except ValueError:
            return False
        
    def get_input_from_user(self, attribute):
        """
        Gets user input for specified attribute. 

        Args:
        attribute (str): The attribute to get.

        Returns:
        str: the user input, preprocessed if applicable.
        """

        try:
            if(attribute == "product_name"):

                product_name = input("Nome del prodotto: ")
                while(product_name == "" or product_name == None or str.isspace(product_name)):
                    logging.info("Product name is empty or not valid.")
                    print("Nome del prodotto non valido.")
                    product_name = input("Nome del prodotto: ")

                product_name = self._inventory.preprocess_item_name(product_name)
                return product_name
            
            if(attribute == "product_quantity"):

                product_quantity = input("Quantità: ")
                while(self._can_cast(product_quantity, int) == False):
                    logging.info("Product quantity is not an integer.")
                    print("La Quantità non è un numero valido!")
                    product_quantity = input("Quantità: ")            
                
                product_quantity = int(product_quantity)
                while(product_quantity <= 0):
                    logging.info("Product quantity is negative.")
                    print("La Quantità non può essere negativa o zero!")
                    product_quantity = input("Quantità: ")

                return product_quantity
            
            if(attribute == "product_purchase_price"):
                product_purchase_price = input("Prezzo di acquisto: ")
                while(self._can_cast(product_purchase_price, float) == False):
                    logging.info("Product quantity is not an integer.")
                    print("Il prezzo di acquisto non è un numero valido!")
                    product_purchase_price = input("Prezzo di acquisto: ")
                
                product_purchase_price = float(product_purchase_price)
                while(product_purchase_price < 0):
                    logging.info("Product quantity is negative.")
                    print("Il prezzo di acquisto non può essere negativo!")
                    product_purchase_price = input("Prezzo di acquisto: ")
                    #We'll accept the case where the purchase price is zero, as it may be a free sample or a gift.

                return product_purchase_price
            
            if(attribute == "product_sale_price"):
                product_sale_price = input("Prezzo di vendita: ")
                while(self._can_cast(product_sale_price, float) == False):
                    logging.info("Product quantity is not an integer.")
                    print("Il prezzo di vendita non è un numero valido!")
                    product_sale_price = input("Prezzo di vendita: ")
                
                product_sale_price = float(product_sale_price)
                while(product_sale_price <= 0):
                    logging.info("Product quantity is negative.")
                    print("Il prezzo di vendita non può essere negativo o zero!")
                    product_sale_price = float(product_sale_price)

                return product_sale_price

        except ValueError as e:
            print(e)

    def _start_interaction(self):
        """
        Starts the main loop of the program after file import or creation.
        """
        logging.info("Starting user interaction...")

        try:
            cmd = None
            print("Benvenuto in GreenVault, il tuo software di gestione per negozi di prodotti vegani!")

            while cmd != "chiudi":
                
                cmd = input("Inserisci un comando: ")

                if cmd=="vendita":
                    pass

                    # registra una vendita
                    # ...

                elif cmd=="profitti":
                    pass
                    # mostra profitti netti e lordi
                    # ...

                elif cmd=="aggiungi":
                    # aggiungi un prodotto al magazzino
                    try:             
                        product_name = self.get_input_from_user("product_name")

                        product_index = self._inventory.get_item_index_from_name(product_name)

                        if(product_index == None):
                            logging.info("Product does not exist, adding a new entry.")

                            product_quantity = self.get_input_from_user("product_quantity")
                            product_purchase_price = self.get_input_from_user("product_purchase_price")
                            product_sale_price = self.get_input_from_user("product_sale_price")                        
                        
                            self._inventory.add_product(product_name, product_quantity, product_purchase_price, product_sale_price)
                        else:
                            logging.info("Product already exists, updating quantity.")

                            product_quantity = self.get_input_from_user("product_quantity")
                            self._inventory.update_product(product_index, product_quantity)

                    except ValueError as e:
                        print(e)

                elif cmd=="elenca":
                    # elenca tutti i prodotti nel magazzino
                    self._inventory.list_products()

                elif cmd=="aiuto":
                    # mostra i possibili comandi
                    self.show_help()

                elif cmd=="chiudi":
                    # saluta e interrompi il programma
                    self.exit_program()

                else:
                    # comando non valido
                    # mostra messaggio di aiuto
                    print("Comando non valido")
                    self.show_help()

        except Exception as e:
            self.exit_program_with_error(exception=e)


    