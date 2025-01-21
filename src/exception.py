import sys  # Importing the 'sys' module to work with system-specific parameters and functions.
from src.logger import logging

# Function to extract and format detailed error messages
def error_message_detail(error,error_detail:sys):
    # Extract traceback information about the exception, This gives (type, value, traceback). We focus on the traceback.
    _,_, exc_tb=error_detail.exc_info()  
    file_name=exc_tb.tb_frame.f_code.co_filename  # Get the filename where the exception occurred
    # Construct a detailed error message with file name, line number, and error description
    error_message="error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error))      
        
    return error_message
        
# Custom exception class that extends Python's built-in Exception class
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        """
        Constructor for CustomException.
        - error_message: Short description of the error.
        - error_detail: Detailed system information about the error.
        """
        super().__init__(error_message)  # Initialize the base Exception class.

         # Generate a detailed error message using the helper function
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
 
    def __str__(self):
         # Define what gets returned when the exception is converted to a string (e.g., print(exception)).
        return self.error_message
    
'''
# Test exceptional handling
if __name__ == "__main__":
    try:
        a=1/0
    except Exception as e:
        logging.info("A division by zero occurred")
        raise CustomException(e,sys)
'''
