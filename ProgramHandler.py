#GreenVault ProgramHandler

#Import section
import sys
import os

class ProgramHandler():
    """
    ProgramHandler class, manages the program's main loop.

    Creates an instance of Inventory and SalesManager to manage the store's products and sales.
    """

    #Attributes

    _inventory = None
    _sales_manager = None

    #Methods

    def __init__(self, *args):
        """
        Initialize the ProgramHandler class.

        """
        pass

    def check_for_file():
        """
        Check if the file exists and is readable.
        """
        pass

    def open_file():
        """
        Open file for reading and writing.
        """
        pass

    def close_file():
        """
        Close file stream.
        """
        pass

    def create_file():
        """
        Creates a new file if it does not exist.
        """
        pass

    def show_help():
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


    def exit_program():
        """
        Exits the program with a farewell message.
        """

        print("Arrivederci, e grazie per aver usato il programma!")
        sys.exit(0)

    def start_interaction():
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
                    ProgramHandler.show_help()

                elif cmd=="chiudi":
                    # saluta e interrompi il programma
                    ProgramHandler.exit_program()

                else:
                    # comando non valido
                    # mostra messaggio di aiuto
                    print("Comando non valido")
                    ProgramHandler.show_help()

        except Exception as e:
            print("Errore imprevisto: ", e)


    