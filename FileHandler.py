#GreenVault FileHandler

#Import section

    #Greenvault classes
import ProgramHandler

    #Standard library classes
import logging
import json

class FileHandler():
    """
    FileHandler class, manages the file stream for GreenVault.
    """

    #Constants

    FILE_NAME = "greenvault.json"
    FILE_INDENTATION = 4

    HANDLER_REF = None

    #Attributes

    file_stream = None

    #Methods

    def __init__(self, ProgramHandlerInstance):
        """
        Initializes the class and its reference to the ProgramHandler instance.
        """
        self.HANDLER_REF = ProgramHandlerInstance

    def load_file(self):
        """
        Open file for reading and writing, without truncating.

        Exception handling made in ProgramHandler.py.
        """

        self.file_stream = open(self.FILE_NAME, "r+")
        self.HANDLER_REF.database = json.load(self.file_stream)

        logging.debug(self.HANDLER_REF.database)
        logging.info("File JSON is consistent and loaded.")

    def initialize_file(self):
        """
        Creates a new file if it does not exist. Maintain previous files by renaming them.
        """
        try:

            logging.info("Creating new file...")

            self.file_stream = open(self.FILE_NAME, "w")

            self.save_file()
            self.close_file()

            logging.info("File created, file handler closed. Ready to reinitialize ProgramHandler.")
            
            self.HANDLER_REF.start_program()

        except Exception as e:
            self.HANDLER_REF.exit_program_with_error(exception=e)

    def close_file(self):
        """
        Close file stream.
        """
        logging.info("Closing file stream.")
        
        if(not self.file_stream == None):

            self.file_stream.close()
            logging.warning("File stream closed.")

        else:

            logging.warning("No file has been loaded")

    def save_file(self):
        """
        Dumps database (HANDLER_REF.database) into file_stream and flushes it into disk.
        """

        try:
            if(self.file_stream == None):
                logging.error("No file has been loaded.")
            
            else:
                self.file_stream.seek(0)
                json.dump(self.HANDLER_REF.database, self.file_stream, indent=self.FILE_INDENTATION)

                self.file_stream.truncate()
                self.file_stream.flush()

                logging.info("File saved.")

        except IOError as e:

            logging.error("File not saved.")
            self.HANDLER_REF.exit_program_with_error(exception=e)

        except Exception as e:

            self.HANDLER_REF.exit_program_with_error(exception=e)