import logging
import os
from datetime import datetime

LOG_FILE_NAME=f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"

LOGS_DIRECTORY = os.path.join(os.getcwd(),"logs")
os.makedirs(os.path.dirname(LOGS_DIRECTORY), exist_ok=True)

LOG_FILE_PATH = os.path.join(LOGS_DIRECTORY, LOG_FILE_NAME)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)