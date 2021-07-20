import logging
import os

from config import APP_DIR

logs_dir = os.path.join(APP_DIR, "logs")
file_name = os.path.join(logs_dir, "distance_api.log")

logging.basicConfig(filename=file_name,
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)

log = logging.getLogger(name="distance_api")