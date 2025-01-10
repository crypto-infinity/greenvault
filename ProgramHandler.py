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

# Class definition

class ProgramHandler():
    """
    ProgramHandler class, manages the program's main loop: loads file, execute the menu, handles operations.

    Creates an instance of Inventory and SalesManager to manage the store's products and sales.
    """
    #Constants

    SAMPLE_DICTIONARY = {
        "products" : [],
        "sales" : [],
        "gross_profits": 0.00,
        "net_profits": 0.00
    }

    #Attributes

    inventory = None # Inventory instance
    sales_manager = None # SalesManager istance
    file_handler = None # FileHandler class instance

    database = SAMPLE_DICTIONARY

    #Methods

    def __init__(self, *args):
        """
        Initialize the ProgramHandler class.

        Provides:
        - logging options
        - instances collection
        """

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

        try:
            self.file_handler = FileHandler(ProgramHandlerInstance=self)
            self._inventory = Inventory(ProgramHandlerInstance=self)
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
        Exits the program with a farewell message.
        """

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

    def _start_interaction(self):
        """
        Starts the main loop of the program after file import or creation.
        """
        logging.info("Starting user interaction...")

        try:
            cmd = None

            while cmd != "chiudi":

                print("Benvenuto in GreenVault, il tuo software di gestione per negozi di prodotti vegani!")
                cmd = input("Inserisci un comando: ")

                if cmd=="vendita":
                    self._inventory.test()
                    pass
                    # registra una vendita
                    # ...

                elif cmd=="profitti":
                    pass
                    # mostra profitti netti e lordi
                    # ...

                elif cmd=="aggiungi":
                    pass
                    # aggiungi un prodotto al magazzino
                    # ...

                elif cmd=="elenca":
                    pass
                    # elenca tutti i prodotti nel magazzino
                    # ...

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


    