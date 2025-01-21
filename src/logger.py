import logging
import os
from datetime import datetime

# Define log file name
log_file=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define directory for logs
logs_path=os.path.join(os.getcwd(), "logs",log_file)
os.makedirs(logs_path, exist_ok=True)  

# Full path for the log file
log_file_path=os.path.join(logs_path,log_file)


# Configure logging
logging.basicConfig(
    filename=log_file_path,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


'''
# Test logging
if __name__ == "__main__":
    logging.info("Logging has started")
'''