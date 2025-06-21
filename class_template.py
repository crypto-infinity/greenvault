#GreenVault class_template

#Import section
import logging

class TestClass():
    """
    Description
    """
    #Constants
    HANDLER_REF = None

    #Attributes

    #Methods

    def __init__(self, ProgramHandlerClass):
        """
        Initializes class and its reference to ProgramHandler instance.
        """
        self.HANDLER_REF = ProgramHandlerClass