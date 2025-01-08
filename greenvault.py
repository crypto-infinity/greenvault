# Version: 1.0
# Author: Gabriele Scorpaniti
# Date: 2024-01-08

#GreenVault

#Description: 
# GreenVault is a management software for vegan product stores. 
# It allows you to register new products, list available products, record sales, 
# calculate gross and net profits, and offers a help menu. 
# It is command-line based for simple and efficient management.


#Import section
import Inventory
import Sale
import Product
import SalesManager

#Main function

def main():
    """
    Python Main Function, executes program's main loop.
    """
    try:
        cmd = None

        while cmd!="chiudi":

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
                pass
                # mostra i possibili comandi
                # ...
            elif cmd=="chiudi":
                pass
                # saluta e interrompi il programma
                # ...
            else:
                pass
                # comando non valido
                # mostra messaggio di aiuto
                # ...
    except Exception as e:
        print("Errore imprevisto: ", e)

if __name__ == "__main__":
    main()





