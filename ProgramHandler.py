#GreenVault ProgramHandler

#Import section
import sys
import os
import logging
import json

class ProgramHandler():
    """
    ProgramHandler class, manages the program's main loop.

    Creates an instance of Inventory and SalesManager to manage the store's products and sales.
    """
    #Constants

    FILE_NAME = "greenvault.json"

    #Attributes

    _inventory = None # Inventory instance
    _sales_manager = None # SalesManager istance
    _file_handler = None # file stream
    file_data = None

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
            self.load_file()
            self.start_interaction()
        except Exception as e:
            logging.error(f"An error occured: {e}")
            self.exit_program()

    def load_file(self):
        """
        Check if the file exists and is readable, then opens it for streaming.
        """

        if os.path.exists(self.FILE_NAME):
            logging.info("File JSON found.")
            try:
                self._open_file()
            except json.JSONDecodeError as e:  
                logging.error("File JSON is not consistent: ", e)
                logging.warning("Creating new file...")
                sys.exit(0) #Exiting since _create_file() is not implemented yet
                self._create_file()
            except Exception as e:
                logging.critical(f"An error occured, stopping program: {e}")
                self.exit_program(message="Si è verificato un errore, uscita dall'app in corso...")
        else:
            logging.warning("File not found, creating new file...")
            self._create_file()

    def _open_file(self):
        """
        Open file for reading and writing, without truncating. Exception handling made by load_file().
        """
    
        self._file_handler = open(self.FILE_NAME, "a+")
        self.file_data = json.load(self._file_handler) #error
        logging.debug(self.file_data)
        logging.info("File JSON is consistent and loaded.")

    def _close_file(self):
        """
        Close file stream.
        """
        pass

    def _create_file(self):
        """
        Creates a new file if it does not exist.
        """

        #do not duplicate file if it already exists
        pass

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


    def exit_program(self, message="Arrivederci, e grazie per aver usato il programma!"):
        """
        Exits the program with a farewell message.
        """

        print(message)
        sys.exit(0)

    def start_interaction(self):
        """
        Starts the main loop of the program after file import or creation.
        """
        try:
            cmd = None

            while cmd != "chiudi":

                print("Benvenuto in GreenVault, il tuo software di gestione per negozi di prodotti vegani!")
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
            print("Errore imprevisto: ", e)


    