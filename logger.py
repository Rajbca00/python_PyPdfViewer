import logging

def get_logging():
    #Config Logging
    logging.basicConfig(level=logging.DEBUG, filename=r"log.log",format="[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s", datefmt='%H:%M:%S', filemode='a+', force=True)
    return logging