import os 
import sys 
import logging
from rich.logging import RichHandler

# # setup the loggins string format 
logging_str = "[%(asctime)s : %(levelname)s : %(module)s : %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level="NOTSET", format=logging_str, datefmt="[%X]", handlers=[
        RichHandler(),
        logging.FileHandler(log_filepath),
                                                                  ]
)  # set level=20 or logging.INFO to turn off debug
log = logging.getLogger(__name__)
