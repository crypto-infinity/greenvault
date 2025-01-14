#GreenVault FileHandler

#Import section

#Greenvault classes
import ProgramHandler

#Standard library classes
import logging
import os
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
        self.HANDLER_REF = ProgramHandlerInstance

    def load_file(self):
        """
        Open file for reading and writing, without truncating.
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
            ProgramHandler.ProgramHandler.exit_program_with_error(self.HANDLER_REF, exception=e)
                
        #do not duplicate file if it already exists

    def close_file(self):
        """
        Close file stream.
        """
        if(not self.file_stream == None):
            self.file_stream.close()
            logging.warning("File stream closed.")
        else:
            logging.warning("No file has been loaded")

    def save_file(self):
        """
        Dump file_data into file_stream and save it.
        """
        try:
            if(self.file_stream == None):
                logging.error("No file has been loaded.")
            
            else:
                self.file_stream.seek(0)
                json.dump(self.HANDLER_REF.database, self.file_stream, indent=self.FILE_INDENTATION)
                self.file_stream.truncate() #servirà?
                self.file_stream.flush()
                logging.info("File saved.")

        except IOError as e:
            logging.error("File not saved.")
            ProgramHandler.ProgramHandler.exit_program_with_error(exception=e)

        except Exception as e:
            ProgramHandler.ProgramHandler.exit_program_with_error(exception=e)